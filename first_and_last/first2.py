def clean_username(value):
    if not value:
        return ""
    
    return value.strip().lower().replace(" ", "_")