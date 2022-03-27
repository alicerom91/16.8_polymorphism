class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_area(self):
        return self.a * self.b


class Square:
    def __init__(self, a):
        self.a = a

    def get_area_square(self):
        return self.a ** 2
# vozvrashenije v stepen **2 v kvadrat
#Iskljuchenije
class NonPositiveDigitException(ValueError):
    pass

class Square:
    def __init__(self, a):
        if a < 0:
            raise NonPositiveDigitException('Неправильно указанна сторона квадрата')


class Circle:
    def __init__(self, r):
        self.r = r

    def get_area_circle(self):
        return (self.r ** 2) * 3.14

