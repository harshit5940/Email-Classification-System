import re

ENTITY_PATTERNS = {
    "email": r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+",
    "phone_number": r"\b\d{10}\b",
    "aadhar_num": r"\b\d{4}\s\d{4}\s\d{4}\b",
    "credit_debit_no": r"\b(?:\d[ -]*?){13,16}\b",
    "cvv_no": r"\b\d{3}\b",
    "expiry_no": r"\b(0[1-9]|1[0-2])\/?([0-9]{2})\b",
    "dob": r"\b\d{2}[/-]\d{2}[/-]\d{4}\b",
    "full_name": r"\b([A-Z][a-z]+(?:\s[A-Z][a-z]+)+)\b"
}

def mask_pii(text):
    masked_text = text
    entities = []

    for entity, pattern in ENTITY_PATTERNS.items():
        for match in re.finditer(pattern, text):
            original = match.group()
            start, end = match.span()
            masked_text = masked_text.replace(original, f"[{entity}]")
            entities.append({
                "position": [start, end],
                "classification": entity,
                "entity": original
            })

    return masked_text, entities
