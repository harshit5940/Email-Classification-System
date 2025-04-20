# Email Support Classifier API

This project masks PII from support emails and classifies them into categories such as Billing, Technical Support, etc.

## Features

- Regex-based PII Masking (No LLMs)
- Email Classification using TF-IDF + Logistic Regression
- FastAPI-based API
- Hugging Face Spaces Deployment Ready

## How to Run

```bash
pip install -r requirements.txt
python app.py
