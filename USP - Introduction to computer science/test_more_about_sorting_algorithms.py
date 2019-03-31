from more_about_sorting_algorithms import SortingMethod
import random
import pytest
from more_about_sorting_algorithms import TimeTracker

class TestSortingMethods:

    @pytest.fixture
    def aleatory_numbers(self):
        aleatory_numbers = [random.randrange(1000) for i in range(800)]
        return aleatory_numbers

    @pytest.fixture
    def nearly_sorted_numbers(self):
        nearly_sorted_numbers = [i for i in range(800)]
        nearly_sorted_numbers[len(nearly_sorted_numbers)//5] = -10
        return nearly_sorted_numbers

    @pytest.fixture
    def buble_sorting_method(self):
        buble_sorting_method = SortingMethod('buble')
        return buble_sorting_method

    @pytest.fixture
    def improved_buble_sorting_method(self):
        improved_buble_sorting_method = SortingMethod('improved buble')
        return improved_buble_sorting_method

    @pytest.fixture
    def selection_sorting_method(self):
        selection_sorting_method = SortingMethod('selection')
        return selection_sorting_method

    def is_sorted(self, sequence):
        for i in range(len(sequence)-1):
            if sequence[i] > sequence[i+1]:
                return False
        return True

    is_sorted_input = [([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], True),
                       ([1, 2, 3, 4, 5, 6, 2, 8, 2, 10], False),
                       ([1, 2, 3, 4, -4, 6, 2, 8, -1, 10], False),
                       ([1, 2, 2, 4, 5, 5, 7, 8, 9, 9], True)]

    @pytest.mark.parametrize('sequence, expected', is_sorted_input)
    def test_is_sorted(self, sequence, expected):
        assert self.is_sorted(sequence) == expected

    def test_selection_sort(self, selection_sorting_method):
        non_sorted = [6, 5, 4, 3, 9, 1]
        print(selection_sorting_method.sort(non_sorted))
        assert selection_sorting_method.sort(non_sorted) == [1, 3, 4, 5, 6, 9]

    def test_selection_sort_aleatory(self, aleatory_numbers, selection_sorting_method):
        sorted_list = selection_sorting_method.sort(aleatory_numbers)
        assert self.is_sorted(sorted_list)

    def test_selection_sort_nearly_sorted(self, nearly_sorted_numbers, selection_sorting_method):
        sorted_list = selection_sorting_method.sort(nearly_sorted_numbers)
        assert self.is_sorted(sorted_list)

    def test_buble_sort(self, buble_sorting_method):
        non_sorted = [6, 5, 4, 3, 9, 1]
        assert buble_sorting_method.sort(non_sorted) == [1, 3, 4, 5, 6, 9]

    def test_buble_sort_aleatory(self, buble_sorting_method, aleatory_numbers):
        sorted_list = buble_sorting_method.sort(aleatory_numbers)
        assert self.is_sorted(sorted_list)

    def test_buble_sort_nearly_sorted(self, buble_sorting_method, nearly_sorted_numbers):
        sorted_list = buble_sorting_method.sort(nearly_sorted_numbers)
        assert self.is_sorted(sorted_list)

    def test_improved_buble_sort(self, improved_buble_sorting_method):
        non_sorted = [6, 5, 4, 3, 9, 1]
        assert improved_buble_sorting_method.sort(non_sorted) == [
            1, 3, 4, 5, 6, 9]

    def test_improved_buble_sort_aleatory(self, improved_buble_sorting_method, aleatory_numbers):
        sorted_list = improved_buble_sorting_method.sort(aleatory_numbers)
        assert self.is_sorted(sorted_list)

    def test_improved_buble_sort_nearly_sorted(self, improved_buble_sorting_method, nearly_sorted_numbers):
        sorted_list = improved_buble_sorting_method.sort(nearly_sorted_numbers)
        assert self.is_sorted(sorted_list)


class TestTimeTracker:

    @pytest.fixture
    def aleatory_numbers(self):
        aleatory_numbers = [random.randrange(1000) for i in range(800)]
        return aleatory_numbers

    @pytest.fixture
    def buble_sorting_method(self):
        buble_sorting_method = SortingMethod('buble')
        return buble_sorting_method

    @pytest.fixture
    def time_tracker(self):
        time_tracker = TimeTracker()
        return time_tracker

    def test_track_buble_sort(self, time_tracker, buble_sorting_method, aleatory_numbers):
        time_passed = time_tracker.track_time_sort(buble_sorting_method, aleatory_numbers)
        assert type(time_passed) == float and time_passed > 0
        
