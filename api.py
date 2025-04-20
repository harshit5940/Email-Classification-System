from fastapi import FastAPI
from pydantic import BaseModel
from utils import mask_pii
from models import classify_email

app = FastAPI()

class EmailRequest(BaseModel):
    input_email_body: str

@app.post("/classify")
def classify(req: EmailRequest):
    masked_email, entities = mask_pii(req.input_email_body)
    category = classify_email(masked_email)

    return {
        "input_email_body": req.input_email_body,
        "list_of_masked_entities": entities,
        "masked_email": masked_email,
        "category_of_the_email": category
    }
