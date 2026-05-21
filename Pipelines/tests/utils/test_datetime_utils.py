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