from searching_sorting_algorithms import Sequence
import pytest


class TestSort:

    test_input = [([1, 2, 3, 4, 5, 6, 7, 8], True),
                  ([7, 6, 5, 4, 3, 2, 1, 0], False),
                  ([6, 9, 9, 0, 5], False)]

    @pytest.mark.parametrize('sequence, expected_result', test_input)
    def test_sorting_algorithms(self, sequence, expected_result):
        input = Sequence(sequence)
        assert input.is_sorted() == expected_result

class TestSearch:

    test_input = [(['a', 'b', 'c', 'd'], 'x', False),
                  (['a', 'b', 'c', 'd'], 'b', 1),
                  (['ab', 'bc', 'cd', 'de'], 'cd' , 2)]

    @pytest.mark.parametrize('sequence, searched_item, expected_result', test_input)
    def test_searching_algorithms(self, sequence, searched_item, expected_result):
        input = Sequence(sequence)
        assert input.search(searched_item) == expected_result