# Run all the tests
# Pytest automatically finds files named test_*.py or
# *_test.py and looks for test functions.
pytest

# Run a certain file
pytest tests/test_my_file.py

# -s to show print statements (although they are quite out of place_)
pytest -s tests/test_my_file.py