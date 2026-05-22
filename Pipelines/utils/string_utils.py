import re
import string

EMAIL_REGEX = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

def concat_strings(str1: str, str2: str) -> str|None:
    """Concatenates two strings.

    Args:
        str1 (str): string to concatenate
        str2 (str): string to concatenate

    Returns:
        str|None: concatenated string
    """ 
    if not isinstance(str1, str) or not isinstance(str2, str):
        return None
    return str1 + str2

def clean_to_title_case(text: str) -> str|None:
    """Cleans a string by stripping leading and trailing whitespace and converting it to title case.

    If the string contains an email address, it will be converted to lowercase. If the string contains a word with numbers, it will be left as is.
    Otherwise, it will be converted to title case.

    Args:
        text (str): string to clean

    Returns:
        str|None: cleaned string
    """
    if not isinstance(text, str):
        return None
    
    cleaned_text = text.strip()
    
    
    words = cleaned_text.split()
    processed_words = []

    for word in words:
        if re.match(EMAIL_REGEX, word):
            processed_words.append(word.lower())
    
        elif any(char.isdigit() for char in word):
            processed_words.append(word)

        else:
            processed_words.append(string.capwords(word))

    return " ".join(processed_words)

def is_valid_email(email: str) -> bool:
    """Validates email format using regex pattern.

    Args:
        email (str): email address to validate

    Returns:
        bool: True if email is valid, False otherwise
    """
    if not isinstance(email, str):
        return False
    return bool(re.fullmatch(EMAIL_REGEX, email))
