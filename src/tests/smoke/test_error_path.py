from data_parser import get_duplicate_count

def test_error_mix_characters():
    test_data = "ABC123D"
    assert get_duplicate_count(test_data) is None

def test_error_digt_string():
    test_data = "1234566"
    assert get_duplicate_count(test_data) is None

def test_error_spcial_charcters():
    test_data = "_@$#$%"
    assert get_duplicate_count(test_data) is None

def test_error_space_input():
    test_dataA = "AAAA"
    test_dataN = "BBBB"
    test_dataC_with_prefix_space = " CDDD"
    conact_string = test_dataA + test_dataN + test_dataC_with_prefix_space
    assert get_duplicate_count(conact_string) is None

def test_error_not_support_characters():
    test_data = "J"
    assert get_duplicate_count(test_data) is None

