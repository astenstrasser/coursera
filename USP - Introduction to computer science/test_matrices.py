from matrices import Matrix


class TestMatrixSize:

    def test_matrix_input(self):
        m = Matrix([[1, 2, 3], [4, 5, 6]])
        assert m.matrix_size() == '2X3'


class TestMatrixSum:

    def test_matrix_sum(self):
        m1 = Matrix([[1, 2, 3], [4, 5, 6]])
        m2 = Matrix([[2, 3, 4], [5, 6, 7]])
        assert m1.matrix_sum(m2.data) == [[3, 5, 7], [9, 11, 13]]

    def test_diff_sizes(self):
            m1 = Matrix([[1], [2], [3]])
            m2 = Matrix([[2, 3, 4], [5, 6, 7]])
            assert m1.matrix_sum(m2.data) == False
