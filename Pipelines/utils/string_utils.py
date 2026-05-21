
import string

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
    
    if not isinstance(text, str):
        return None
    
    cleaned_text = text.strip()
    return string.capwords(cleaned_text)