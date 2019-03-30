from classes import Triangle
import pytest


class TestPerimeter:

    test_data = [(2, 2, 2, 6),
                 (1, 4, 2, 7),
                 (0, 0, 0, 0)]

    @pytest.mark.parametrize('a, b, c, expected', test_data)
    def test_perimeter(self, a, b, c, expected):
        t = Triangle(a, b, c)
        assert t.perimeter() == expected

class TestTriangleType:

    test_data = [(1, 1, 1, 'equilateral'),
                 (1, 2, 2, 'isosceles'),
                 (3, 1, 2, 'scalene'),
                 (3, 3, 4, 'isosceles')]
    
    @pytest.mark.parametrize('a, b, c, expected', test_data)
    def test_tipo_lado(self, a, b, c, expected):
        t = Triangle(a,b,c)
        assert t.triangle_type() == expected