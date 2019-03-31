import time
import random

class SortingMethod:

    def __init__(self, method_name):
        self.name = method_name
    

    def sort(self, sequence):
        try:
            if self.name == 'selection':
                sequence = self.selection_sort(sequence)
            elif self.name == 'buble':
                sequence = self.buble_sort(sequence)
            elif self.name == 'improved buble':
                sequence = self.improved_buble_sort(sequence)
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

    def buble_sort(self, sequence):
        for i in range(len(sequence)-1, 0, -1):
            for j in range(i):
                if sequence[j] > sequence[j+1]:
                    sequence[j], sequence[j+1] = sequence[j+1], sequence[j]
        return sequence

    def improved_buble_sort(self, sequence):
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

if __name__ == "__main__":
    buble = SortingMethod('buble')
    selection = SortingMethod('selection')
    improved_buble = SortingMethod('improved buble')
    time_tracker = TimeTracker()
    aleatory_numbers = [random.randrange(1000) for i in range(4000)] 

    print('buble: ', time_tracker.track_time_sort(buble, aleatory_numbers))
    print('selection: ', time_tracker.track_time_sort(selection, aleatory_numbers))
    print('improved buble: ', time_tracker.track_time_sort(improved_buble, aleatory_numbers))
    print(is_sorted(improved_buble.sort(aleatory_numbers)))