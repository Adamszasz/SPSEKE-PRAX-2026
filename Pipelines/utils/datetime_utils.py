from datetime import datetime
from typing import Optional

def parse_to_datetime(date_str: str, time_str: str) -> Optional[datetime]:
    """
    Spojí date_str a time_str do jedného objektu datetime.
    Podporuje formáty 'YYYY-MM-DD' a 'DD.MM.YYYY'.
    Ak je formát nesprávny, vráti None.
    """
    
    combined_str = f"{date_str} {time_str}"
    
    try:
        return datetime.strptime(combined_str, "%Y-%m-%d %H:%M:%S")
    except ValueError:
        pass  

    
    try:
        return datetime.strptime(combined_str, "%d.%m.%Y %H:%M:%S")
    except ValueError:
        pass  

    return None