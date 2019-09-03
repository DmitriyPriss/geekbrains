import math


class Triangle():
    def __init__(self, a_x, a_y, b_x, b_y, c_x, c_y):
        self.a_x = a_x
        self.a_y = a_y
        self.b_x = b_x
        self.b_y = b_y
        self.c_x = c_x
        self.c_y = c_y
        self.AB = round(math.sqrt(int(math.fabs(((b_y - a_y) ** 2) + ((b_x - a_x) ** 2)))), 2)
        self.BC = round(math.sqrt(int(math.fabs(((c_y - b_y) ** 2) + ((c_x - b_x) ** 2)))), 2)
        self.CA = round(math.sqrt(int(math.fabs(((a_y - c_y) ** 2) + ((a_x - c_x) ** 2)))), 2)

    def perimetr(self):
        self.perimetr = (self.AB + self.BC + self.CA)
        return (self.perimetr)

    def ploshad(self):
        self.perimetr /= 2
        self.ploshad = round(math.sqrt(
            self.perimetr * (self.perimetr - self.AB) * (self.perimetr - self.BC) * (self.perimetr - self.CA)), 2)
        return (self.ploshad)

    def vysota(self):
        self.ploshad *= 2
        self.vysota = round((self.ploshad / self.CA), 2)
        return (self.vysota)

my_tri = Triangle(2, 2, 5, 8, 7, 4)

print('Длинна строны АВ = {}, ВС = {}, СА = {}'.format(my_tri.AB, my_tri.BC, my_tri.CA))
print('Периметр треугольника АВС равен {}'.format(my_tri.perimetr()))
print('Площадь треугольника АВС равна {}'.format(my_tri.ploshad()))
print('Высота треугольника АВС, проведенная из угла В равна {}'.format(my_tri.vysota()))


class Trapeciya():
    def __init__(self, a_x, a_y, b_x, b_y, c_x, c_y, d_x, d_y):
        self.a_x = a_x
        self.a_y = a_y
        self.b_x = b_x
        self.b_y = b_y
        self.c_x = c_x
        self.c_y = c_y
        self.d_x = d_x
        self.d_y = d_y
        self.AB = round(math.sqrt(int(math.fabs(((b_y - a_y) ** 2) + ((b_x - a_x) ** 2)))), 2)
        self.BC = round(math.sqrt(int(math.fabs(((c_y - b_y) ** 2) + ((c_x - b_x) ** 2)))), 2)
        self.CD = round(math.sqrt(int(math.fabs(((c_y - d_y) ** 2) + ((c_x - d_x) ** 2)))), 2)
        self.DA = round(math.sqrt(int(math.fabs(((d_y - a_y) ** 2) + ((d_x - a_x) ** 2)))), 2)

    def perimetr(self):
        self.perimetr = (self.AB + self.BC + self.CD + self.DA)
        return (self.perimetr)

    def ploshad(self):
        self.ploshad = round(((self.AB + self.CD) / 2) * self.vysota(), 2)
        return (self.ploshad)

    def vysota(self):
        self.vysota = round(math.sqrt(((self.BC ** 2 - (self.DA - self.AB) ** 2 + self.BC ** 2 - self.CD ** 2) / (2 * (self.DA - self.AB))) ** 2), 2)
        return (self.vysota)

my_trap = Trapeciya(2, 2, 5, 8, 3, 2, 7, 4)

print('Длинна строны АВ = {}, ВС = {}, СD = {}, DA = {}'.format(my_trap.AB, my_trap.BC, my_trap.CD, my_trap.DA))
print('Периметр трапеции АВСD равен {}'.format(my_trap.perimetr()))
print('Площадь трапеции АВСD равна {}'.format(my_trap.ploshad()))
print('Высота трапеции АВСD, проведенная из угла В равна {}'.format(my_trap.vysota()))