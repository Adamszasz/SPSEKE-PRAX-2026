import re

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