

    
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

    def test_word_with_numbers(self):
        result = clean_to_title_case(" 1A version 2 m2m  ")
        assert result == "1A Version 2 m2m"

    def test_string_with_email(self):
        result = clean_to_title_case(" EmAil: peter@Skola.sk  ")
        assert result == "Email: peter@skola.sk"
from Pipelines.utils.string_utils import is_valid_email

class TestIsValidEmail:
    
    def test_valid_email(self):
        result = is_valid_email("user@example.com")
        assert result == True
    
    def test_missing_symbol(self):
        result = is_valid_email("userexample.com")
        assert result == False
    
    def test_missing_domain_extension(self):
        result = is_valid_email("user@example")
        assert result == False
    
    def test_domain(self):
        result = is_valid_email("user@.com")
        assert result == False
