# Run all the tests
# Pytest automatically finds files named test_*.py or
# *_test.py and looks for test functions.
pytest

# Run a certain file
pytest tests/test_my_file.py

# -s to show print statements (although they are quite out of place_)
pytest -s tests/test_my_file.py

# ---------------------------------------------------------------------------------------------

# Run a test once with one variable, then again with another variable
@pytest.mark.parametrize("some_variable", [True, False])
def test_publish_something(some_variable):
    print(some_variable)
    assert 1 == 0

# Printing stuff
# Prints only show up when a test failes, so best is to throw a raise() somewhere
# and then your prints will show up

# Mock a function
def test_publish_something_true(mocker):   # This mocker variable is magically available when using pytest
    mocker.patch("my_module.SomeClass.query", return_value=True)

    from my_module import SomeClass
    instance = SomeClass()
    print(instance.query("whatever arguments"))  # Will return what we set up above
    assert 1 == 0