from starter import report


def clean_text(text):
    text = text.strip()
    text = text.lower()
    text = text.replace("!", "")
    return text


if __name__ == "__main__":
    report(clean_text)
