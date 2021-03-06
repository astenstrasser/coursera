class Matrix:

    def __init__(self, matrix_numbers):
        self.data = matrix_numbers

    def matrix_size(self):
        count_lines = 0
        count_colums = 0
        for _ in self.data:
            count_lines += 1
        for _ in self.data[0]:
            count_colums += 1
        return str(count_lines)+'X'+str(count_colums)

    def matrix_sum(self, m2):
        sum_m1_m2 = []
        if len(m2) == len(self.data):
            for i in range(len(self.data)):
                line = []
                if len(m2[i]) == len(self.data[i]):
                    for j in range(len(self.data[0])):
                        line.append(self.data[i][j] + m2[i][j])
                    sum_m1_m2.append(line)
                else:
                    return False
            return sum_m1_m2
        else:
            return False
        