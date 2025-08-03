# 🧾 Invoice Extractor

A smart AI-powered mini project that allows users to upload **invoice images or PDFs** and ask questions like "What is the total amount?" or "Who is the vendor?" using OCR and LLM technology.

---

## 📂 Folder Structure

```
Mini Project 1-Invoice Extractor/
│
├── app/                            # Your main application code
│   └── app.py                      # Main Streamlit or Flask app file
├── mini/                           # Possibly additional resources/modules
├── .env                            # Environment variables
├── requirement                     # Text file listing required packages
├── hindi_960.jpg                   # Sample invoice image
├── sample-invoice-*.png            # Another sample invoice
└── README.md                       # This file
```

---

## 🚀 Features

- Upload invoice in **PNG**, **JPG**, or **PDF**
- Extracts text using **OCR**
- Ask questions like:
  - "What is the invoice number?"
  - "What is the total amount?"
  - "When is the due date?"
- Uses **LLM (Large Language Model)** to provide natural language answers

---

## ⚙️ Setup Instructions

### 1. Create & activate environment (Conda recommended)

```bash
conda create --name invoiceextractor python=3.11
conda activate invoiceextractor
```

### 2. Install dependencies

```bash
pip install -r requirement
```

> 💡 If you're using `pytesseract`, make sure [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) is installed and added to your system PATH.

### 3. Run the app

For Streamlit:
```bash
streamlit run app/app.py
```

For Flask:
```bash
python app/app.py
```

---

## 🧠 How It Works

1. The user uploads an invoice image or PDF.
2. OCR (Optical Character Recognition) extracts all visible text.
3. Extracted text is sent to an LLM (like GPT) to process natural language queries.
4. The app returns accurate answers from invoice data.

---

## ❓ Example Questions You Can Ask

- "What is the total amount due?"
- "What is the invoice date?"
- "Who issued this invoice?"
- "What are the purchased items?"

---

## 📦 Dependencies

- `pytesseract` or `easyocr`
- `pdf2image`, `fitz` (`PyMuPDF`)
- `streamlit` or `flask`
- `openai`, `langchain` or `transformers`
- `dotenv`, `uuid`, etc.

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

---

## ✨ Future Improvements

- Multi-invoice batch processing
- Export parsed results to CSV
- Highlight answer in invoice
- Multi-language OCR support

---

## 📬 Contact

For support or feedback, contact lakshyahidau2005@gmail.com or open an issue in the GitHub repo.

