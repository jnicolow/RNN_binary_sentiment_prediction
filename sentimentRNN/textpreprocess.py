import re

def remove_html_tags(text):
    # Regular expression to remove anything between < and >
    clean_text = re.sub(r'<.*?>', '', text)
    return clean_text

def clean_text(text):
    text = remove_html_tags(text)


    text = text.lower() # all same case

    # remove punctuation (anything thats not a character)
    text = re.sub(r"[^a-zA-Z\s]", "", text)

    return text