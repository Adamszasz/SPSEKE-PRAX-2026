import pytest
from datetime import datetime
from Pipelines.utils.datetime_utils import parse_to_datetime

def test_valid_iso_format():
    """Testuje validný ISO formát ("2026-05-20", "14:30:00")"""
    result = parse_to_datetime("2026-05-20", "14:30:00")
    
    assert result is not None
    assert result == datetime(2026, 5, 20, 14, 30, 0)

def test_valid_european_format():
    """Testuje validný európsky formát ("20.05.2026", "14:30:00")"""
    result = parse_to_datetime("20.05.2026", "14:30:00")
    
    assert result is not None
    assert result == datetime(2026, 5, 20, 14, 30, 0)

def test_invalid_format_input():
    """Testuje neplatný formát (mal by vrátiť None)"""

    assert parse_to_datetime("2026/05/20", "14:30:00") is None
    
    
    assert parse_to_datetime("neplatny-datum", "14:30:00") is None
    
    assert parse_to_datetime("32.05.2026", "14:30:00") is None
    