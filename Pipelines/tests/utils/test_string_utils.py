
    
from Pipelines.utils.string_utils import concat_strings
from Pipelines.utils.string_utils import clean_to_title_case


class TestConcatStrings:
    
    def test_valid_input(self):
        result = concat_strings("Hello, ", "World!")
        assert result == "Hello, World!"

    def test_empty_strings(self):
        result = concat_strings("", "")
        assert result == ""

    def test_invalid_input(self): 
        result = concat_strings("Hello, ", 123)
        assert result == None

class TestCleanToTitleCase:
    
    def test_valid_input(self):
        result = clean_to_title_case("  hello world  ")
        assert result == "Hello World"

    def test_empty_string(self):
        result = clean_to_title_case("")
        assert result == ""

    def test_invalid_input(self):
        result = clean_to_title_case(123)
        assert result == None

    def test_messy_input(self):
        result = clean_to_title_case("  hELLO wORLD  ")
        assert result == "Hello World"

    def test_already_title_case(self):
        result = clean_to_title_case("Hello World")
        assert result == "Hello World"

    def test_mixed_case(self):
        result = clean_to_title_case("  it's a beautiful day  ")
        assert result == "It's A Beautiful Day"
