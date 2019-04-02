from more_about_searching_algorithms import Searcher
import pytest


class TestSearcher:

    @pytest.fixture
    def searcher(self):
        searcher = Searcher()
        return searcher

    #def test_simple_search(self):
    test_input = [([1,2,3,4,5,6,7,8,9,10], 1, 0),
                  ([1,2,3,4,5,6,7,8,9,10], 5, 4),
                  ([1,2,3,4,5,6,7,8,9,10], 0, -1)]
    
    @pytest.mark.parametrize('sequence, searched_item, expected_result', test_input)
    def test_simple_search(self, searcher, sequence, searched_item, expected_result):
        assert searcher.simple_search(searched_item, sequence) == expected_result

    @pytest.mark.parametrize('sequence, searched_item, expected_result', test_input)
    def test_binary_search(self, searcher, sequence, searched_item, expected_result):
        assert searcher.binary_search(searched_item, sequence) == expected_result