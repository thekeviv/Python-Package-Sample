#using pytest here
#to run the test, go to the work directory and in a terminal window type pytest
#to run only in one file, run pytest tests/name_of_file.py
#name of the test must start with 'test'
from package_name import a_class

#method names also start with test
def test_method():
	assert a==some_value