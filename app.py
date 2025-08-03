import google.generativeai as genai
from dotenv import load_dotenv
import os
import streamlit as st
from PIL import Image
import PyPDF2

load_dotenv()   # Load environment variables from .env file

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input, image, prompt):
    model = genai.GenerativeModel('gemini-2.5-flash-lite')
    response = model.generate_content([input, image, prompt])
    return response.text

def input_image_setup(uploaded_file):
    byte_data = uploaded_file.getvalue()
    image_parts = [
        {
            "mime_type": uploaded_file.type,
            "data": byte_data,
        }
    ]
    return image_parts

def extract_pdf_text(uploaded_file):
    pdf_reader = PyPDF2.PdfReader(uploaded_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text() or ""
    return text

st.set_page_config(page_title="Invoice Extractor", page_icon=":page_facing_up:", layout="wide")

with st.sidebar:
    st.title("Invoice Extractor")
    st.markdown("Upload an **image** or **PDF** of your invoice and get insights instantly!")
    st.info("Supported formats: jpg, jpeg, png, pdf")

st.header("📄 Invoice Extractor")
input = st.text_input("Ask a question about your invoice:", key="input")
uploaded_file = st.file_uploader("Upload an Invoice (Image or PDF)", type=["jpg", "jpeg", "png", "pdf"])

col1, col2 = st.columns([1,2])

file_type = None
if uploaded_file is not None:
    if uploaded_file.type == "application/pdf":
        file_type = "pdf"
        with col1:
            st.write("**PDF Uploaded**")
        with col2:
            pdf_text = extract_pdf_text(uploaded_file)
            st.write("**Extracted PDF Text:**")
            st.write(pdf_text[:1000])  # Show first 1000 chars
    else:
        file_type = "image"
        image = Image.open(uploaded_file)
        with col1:
            st.image(image, caption="Uploaded Image", use_column_width=True)
        with col2:
            st.write("**Image Uploaded**")

submit = st.button("🔎 Extract Invoice Data")

input_prompt = """
You are an expert in understanding invoices.
You will receive an invoice (image or extracted PDF text).
Answer questions based on the provided input.
"""

if submit and uploaded_file is not None:
    if file_type == "image":
        image_data = input_image_setup(uploaded_file)
        response = get_gemini_response(input_prompt, image_data[0], input)
    elif file_type == "pdf":
        response = get_gemini_response(input_prompt, extract_pdf_text(uploaded_file), input)
    else:
        st.error("Unsupported file type.")
        response = None

    if response:
        st.subheader("💡 Extracted Information")
        st.write(response)