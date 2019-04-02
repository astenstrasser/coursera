import time
import random


class SortingMethod:

    def __init__(self, method_name):
        self.name = method_name

    def sort(self, sequence):
        try:
            if self.name == 'selection':
                sequence = self.selection_sort(sequence)
            elif self.name == 'bubble':
                sequence = self.bubble_sort(sequence)
            elif self.name == 'improved bubble':
                sequence = self.improved_bubble_sort(sequence)
            return sequence
        except:
            raise ValueError('Unknown Method name given: ', self.name)

    def selection_sort(self, sequence):
        for i in range(len(sequence)-1):
            smaller_position = i
            for j in range(i+1, len(sequence)):
                if sequence[j] < sequence[smaller_position]:
                    smaller_position = j
            sequence[i], sequence[smaller_position] = sequence[smaller_position], sequence[i]
        return sequence

    def bubble_sort(self, sequence):
        for i in range(len(sequence)-1, 0, -1):
            for j in range(i):
                if sequence[j] > sequence[j+1]:
                    sequence[j], sequence[j+1] = sequence[j+1], sequence[j]
        return sequence

    def improved_bubble_sort(self, sequence):
        for i in range(len(sequence)-1, 0, -1):
            any_changes = False
            for j in range(i):
                if sequence[j] > sequence[j+1]:
                    sequence[j], sequence[j+1] = sequence[j+1], sequence[j]
                    any_changes = True
            if not any_changes:
                return sequence
        return sequence


class TimeTracker:

    def track_time_sort(self, sorting_method, aleatory_numbers):
        time_begin = time.time()
        sorting_method.sort(aleatory_numbers)
        time_end = time.time()
        return time_end - time_begin


def is_sorted(sequence):
    for i in range(len(sequence)-1):
        if sequence[i] > sequence[i+1]:
            return False
    return True

def my_place():
    print(__name__)


if __name__ == "__main__":
    bubble = SortingMethod('bubble')
    selection = SortingMethod('selection')
    improved_bubble = SortingMethod('improved bubble')
    time_tracker = TimeTracker()
    aleatory_numbers = [random.randrange(1000) for i in range(4000)]
    
    print('improved bubble: ', time_tracker.track_time_sort(
        improved_bubble, aleatory_numbers[:]))
    print('bubble: ', time_tracker.track_time_sort(bubble, aleatory_numbers[:]))
    print('selection: ', time_tracker.track_time_sort(
        selection, aleatory_numbers[:]))
    print(is_sorted(improved_bubble.sort(aleatory_numbers)))
