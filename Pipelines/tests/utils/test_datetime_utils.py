import pytest
from datetime import datetime
from Pipelines.utils.datetime_utils import round_to_whole_hour


class TestRoundToWholeHour:

    def test_standard_truncation(self):
        dt = datetime(2024, 6, 15, 14, 35, 12)
        result = round_to_whole_hour(dt)
        assert result == datetime(2024, 6, 15, 14, 0, 0)

    def test_midnight_edge_case(self):
        dt = datetime(2024, 6, 15, 0, 5, 0)
        result = round_to_whole_hour(dt)
        assert result == datetime(2024, 6, 15, 0, 0, 0)

    def test_already_whole_hour(self):
        dt = datetime(2024, 6, 15, 15, 0, 0)
        result = round_to_whole_hour(dt)
        assert result == datetime(2024, 6, 15, 15, 0, 0)

    def test_microseconds_truncated(self):
        dt = datetime(2024, 6, 15, 9, 45, 30, 999999)
        result = round_to_whole_hour(dt)
        assert result == datetime(2024, 6, 15, 9, 0, 0, 0)

    def test_date_preserved(self):
        dt = datetime(2024, 12, 31, 23, 59, 59)
        result = round_to_whole_hour(dt)
        assert result.date() == dt.date()
        assert result.hour == 23

    def test_invalid_input_string(self):
        with pytest.raises(TypeError, match="Expected datetime object, got str instead"):
            round_to_whole_hour("2024-06-15 14:30:00")

    def test_invalid_input_int(self):
        with pytest.raises(TypeError, match="Expected datetime object, got int instead"):
            round_to_whole_hour(12345)

    def test_invalid_input_none(self):
        with pytest.raises(TypeError, match="Expected datetime object, got NoneType instead"):
            round_to_whole_hour(None)

    def test_invalid_input_dict(self):
        with pytest.raises(TypeError, match="Expected datetime object, got dict instead"):
            round_to_whole_hour({"year": 2024, "month": 6})