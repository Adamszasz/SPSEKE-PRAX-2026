
    
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