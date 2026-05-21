

    
from Pipelines.utils.string_utils import concat_strings


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
