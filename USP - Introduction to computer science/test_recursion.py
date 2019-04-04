from recursion import sum_elements
from recursion import find_odds
from recursion import incomodam
from recursion import elefantes
import pytest


class TestSumElements:

    input_sum_elements = [([1, 2, 3, 4, 5, 6], 21),
                          ([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 12)]

    @pytest.mark.parametrize('list_of_elements, expected_result', input_sum_elements)
    def test_sum_elements(self, list_of_elements, expected_result):
        assert sum_elements(list_of_elements) == expected_result


class TestFindOdds:

    def test_find_odds(self):
        list_of_elements = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        odds = [1, 3, 5, 7, 9]
        assert find_odds(list_of_elements) == odds

    def test_find_odds_no_odd(self):
        list_of_elements = [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]
        odds = []
        assert find_odds(list_of_elements) == odds

    def test_find_odds_one_odd(self):
        list_of_elements = [4,4,4,4,4,5,4]
        odds = [5]
        assert find_odds(list_of_elements) == odds


class TestIncomodam:

    test_incomodam_inputs = [(1, 'incomodam '),
                             (0, ''),
                             (3, 'incomodam incomodam incomodam '),
                             (-1, '')]

    @pytest.mark.parametrize('times, expected_output', test_incomodam_inputs)
    def test_incomodam(self, times, expected_output):
        assert incomodam(times) == expected_output


class TestElefantes:

    def test_elefantes(self):
        times = 3
        expected_output = (
            '1 elefante incomoda muita gente\n'
            '2 elefantes incomodam incomodam muito mais\n'
            '2 elefantes incomodam muita gente\n'
            '3 elefantes incomodam incomodam incomodam muito mais'
        )   
        assert elefantes(times) == expected_output

    def test_elefantes_zero(self):
        times = 0
        expected_output = ''   
        assert elefantes(times) == expected_output

    def test_elefantes_one(self):
        times = 1
        expected_output = '1 elefante incomoda muita gente' 
        assert elefantes(times) == expected_output

    def test_elefantes_negative(self):
        times = -3
        expected_output = ''   
        assert elefantes(times) == expected_output
