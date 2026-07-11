import re

def standardizer_name(raw_name):
    cleaned = re.sub(r'[-\s.]+','_',raw_name).strip().lower()
    cleaned = re.sub(r'[^a-z0-9_]','', cleaned)
    cleaned = re.sub(r'_+','_', cleaned)

    if not cleaned or cleaned == '_':
        return "Unknown Column"
    cleaned = cleaned.strip('_')
    if not cleaned:
        return "Unknown Column"
    if cleaned[0].isdigit():
        cleaned = "col" + cleaned
    return cleaned
