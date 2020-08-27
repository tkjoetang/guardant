# guardant (Demo only)

## Structure of this repository
Under src directory
- We have data_parser.py which has one method
Under src/tests direcotry
- We have test cases to test the data_parser

## Structure of test cases
Under tests/smoke, we have two testing files
- Happy path test cases
- Error path test cases

Under test/load, we have one testing file
- Generate a data, staring with one million choose characters, to 
  test.
  
# How to start:
Clone this repository, run the following command on your Terminal
or using any Github desktop tool. (We assume git command already installed on your
system)
```
git clone https://github.com/tkjoetang/guardant.git
```

Once it is clone, run the following command by copying and pasting to your terminal again
```
cd guardant && pip3 install -r requirement.txt  && export PYTHONPATH="$PWD/src"
```

Now you should be ready to test on your Terminal

Example to run just the smoke test suites:
```
pytest -v -s src/tests/smoke/
```
Above command should give you the following results
```
src/tests/smoke/test_error_path.py::test_error_mix_characters Input data is not valid ABC123D
PASSED
src/tests/smoke/test_error_path.py::test_error_digt_string Input data is not valid 1234566
PASSED
src/tests/smoke/test_error_path.py::test_error_spcial_charcters Input data is not valid _@$#$%
PASSED
src/tests/smoke/test_error_path.py::test_error_space_input Input data is not valid AAAABBBB CDDD
PASSED
src/tests/smoke/test_error_path.py::test_error_not_support_characters Input data is empty
PASSED
src/tests/smoke/test_happy_path.py::test_valid_input [('A', 4), ('B', 3), ('C', 2), ('D', 3)]
PASSED
src/tests/smoke/test_happy_path.py::test_repeact_input [('A', 4), ('B', 3), ('C', 2), ('D', 3), ('A', 6), ('B', 1), ('C', 1), ('A', 3), ('D', 3), ('A', 2)]
PASSED
src/tests/smoke/test_happy_path.py::test_single_char [('A', 1)]
PASSED
src/tests/smoke/test_happy_path.py::test_accept_characters [('A', 1), ('B', 1), ('C', 1), ('D', 1)]
PASSED
src/tests/smoke/test_happy_path.py::test_empty_input Input data is empty
PASSED
```

Example to run the full test suites:
```
pytest -v -s
```

Example to run the load test suites:
```
pytest -v -s src/tests/load/
```