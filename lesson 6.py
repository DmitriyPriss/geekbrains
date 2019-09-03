import math


class Vector:
    """
    Класс для Вектора - направленного отрезка на плоскости
    """

    def __init__(self, coords):
        # Координаты храним в атрибуте __coord (ну захотелось нам так)
        # Два символа подчеркивания __ разрешают доступ к атрибуту только внутри класса
        self.__coords = coords

    @property  # с помощью этого декоратора можем обращаться к атрибуту x --> self.x Или obj.x
    def x(self):
        return self.__coords[0]

    @x.setter  # Позволяет в удобной форме устанавливать атрибут x --> self.x = 10 или obj.x = 10
    def x(self, x):
        self.__coords = x, self.__coords[1]

    @property
    def y(self):
        return self.__coords[1]

    @y.setter
    def y(self, y):
        self.__coords = self.__coords[0], y

    @property
    def len(self):
        return math.sqrt(self.x * self.x + self.y * self.y)

    @len.setter
    def len(self, value):
        self.x = 10
        self.y = 10

    def as_point(self):
        return self.__coords

    def rotate(self, angle):
        x = self.x * math.cos(angle) - self.y * math.sin(angle)
        y = self.x * math.sin(angle) + self.y * math.cos(angle)
        self.x, self.y = x, y


v1 = Vector((10, 5))
v2 = Vector((-10, 8))

print('v1.x = ', v1.x)
print('v2.y', v2.y)
v1.x = -21
print('v1.x = ', v1.x)