from data_parser import get_duplicate_count

# Note: For demo purpose, we just generate
#       data on run time and assert not None
#
#       If this test case run in CI/CD environment
#       it should open a input_data file and assert
#       expect_ouput_file
def test_large_volume_data():
    import random
    test_data = ''.join(random.choice("ABCD") for _ in range(1000000))
    get_duplicate_count(test_data) is not None