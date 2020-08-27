from data_parser import get_duplicate_count

def test_valid_input():
    test_data = "AAAABBBCCDDD"
    assert get_duplicate_count(test_data) == "A4B3C2D3"

def test_repeact_input():
    test_data = "AAAABBBCCDDDAAAAAABCAAADDDAA"
    assert get_duplicate_count(test_data) == "A4B3C2D3A6B1C1A3D3A2"

def test_single_char():
    test_data = "A"
    assert get_duplicate_count(test_data) == "A1"

def test_accept_characters():
    test_data = "ABCD"
    assert get_duplicate_count(test_data) == "A1B1C1D1"

def test_empty_input():
    test_data = ""
    assert get_duplicate_count(test_data) == ""
