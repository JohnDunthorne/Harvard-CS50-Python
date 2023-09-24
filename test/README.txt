to be sure that *pytest test*
works in the command prompt

Make sure 'test' subdirectory folder has

__init__.py in the folder

files that start with test_*

for example test_file

all tests within the files are labelled

test_*
or
*_test

for example:
def test_hello_name_input():
    assert hello_name("John") == "Hello, John"
