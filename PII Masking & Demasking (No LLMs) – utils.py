def mask_pii(text: str):
    # Example masking logic (expand per entity type)
    matches = []
    masked_text = text

    email_pattern = re.compile(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+")
    for match in email_pattern.finditer(text):
        masked_text = masked_text.replace(match.group(), "[email]")
        matches.append({
            "position": [match.start(), match.end()],
            "classification": "email",
            "entity": match.group()
        })

    return masked_text, matches
