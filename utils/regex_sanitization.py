from re import sub


def sanitization(raw):
    return sub(r'\W', ' ', sub(r'\s+', ' ', raw)).lower().strip()