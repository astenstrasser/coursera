class Triangle:

    def __init__(self, a, b, c):
        self.a = int(a)
        self.b = int(b)
        self.c = int(c)
    
    def perimeter(self):
        return self.a + self.b + self.c
    
    def triangle_type(self):
        if self.a == self.b and self.a == self.c:
            return 'equilateral'
        elif self.a == self.b or self.a == self.c or self.b == self.c:
            return 'isosceles'
        else:
            return 'scalene'