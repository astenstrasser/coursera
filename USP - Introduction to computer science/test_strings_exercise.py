import pytest
from strings_exercise import ListOfStrings


class TestFindSmallerName:

    def test_spaces_in_input(self):
        my_input = ListOfStrings(
            ['zé roberto', '   maria  Clara ', ' Alice  '])
        assert my_input.find_smaller_name() == 'Alice'


class TestOrderFirstString:

    def test_input_uppercase(self):
        my_input = ListOfStrings(['zé', 'maria', 'Alice'])
        assert my_input.order_first_string() == 'Alice'


class TestUpperLetters:

    def test_input(self):
        my_input = ListOfStrings(
            ['Are', 'we', 'developing', 'in', 'Python', '2', '?'])
        assert my_input.upper_letters() == 'AP'
