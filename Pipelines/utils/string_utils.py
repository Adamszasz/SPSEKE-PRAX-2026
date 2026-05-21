import re

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

    if not isinstance(email, str):
        return False
    if "@" not in email:
        return False
    local, domain = email.split("@") #rozdeli email na local a domain = [local@domain]
    if not local or not domain:
        return False
    if domain.startswith("."):
        return False
    if not re.search(r'\.[a-zA-Z]{2,}$', domain): #re.search hlada ci je v domain .com .sk atd...
        return False
    return True