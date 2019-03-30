class Sequence:

    def __init__(self, sequence):    
        self.sequence = sequence

    def is_sorted(self):
        for i in range(len(self.sequence)-1):
            if self.sequence[i] < self.sequence[i+1]:
                pass
            else:
                return False
        return True

    def search(self, searched_item):
        for i in range(len(self.sequence)):
            if self.sequence[i] == searched_item:
                return i
        return False