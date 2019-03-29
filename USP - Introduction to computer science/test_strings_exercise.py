import pytest 
from strings_exercise import ListOfStrings

class Test_order_first_string:

    def test_input_uppercase(self):
        my_input = ListOfStrings(['zé', 'maria', 'Alice'])
        assert my_input.order_first_string() == 'Alice'
    
class Test_find_smaller_name:

    def test_spaces_in_input(self):
        my_input = ListOfStrings(['zé roberto', '   maria  Clara ', ' Alice  '])
        assert my_input.find_smaller_name() == 'Alice'