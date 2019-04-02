from recursion import sum_elements 
from recursion import find_odds
import pytest


class TestSumElements:

    input_sum_elements = [([1,2,3,4,5,6], 21),
                         ([1,1,1,1,1,1,1,1,1,1,1,1], 12)]

    @pytest.mark.parametrize('list_of_elements, expected_result', input_sum_elements)
    def test_sum_elements(self, list_of_elements, expected_result):
        assert sum_elements(list_of_elements) == expected_result

class TestFindOdds:

    input_find_odds = [([1,2,3,4,5,6,7,8,9], [1,3,5,7,9])]
                    #   ([5,5,5,5,5], [5,5,5,5,5])
                    #   ([2,2,2,2], []),
                    #   ([2,2,3,2], [3])]

    @pytest.mark.parametrize('list_of_elements, odds', input_find_odds)
    def test_find_odds(self, list_of_elements, odds):
        assert find_odds(list_of_elements) == odds
