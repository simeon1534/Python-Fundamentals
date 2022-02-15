class Circle:
    def __init__(self, diameter):
        self.diameter = diameter
        self.radius = diameter / 2

    __pi = 3.14

    def calculate_circumference(self):
        P = 2 * self.__pi * self.radius
        return P

    def calculate_area(self):
        S = self.__pi * (self.radius ** 2)
        return S

    def calculate_area_of_sector(self, angle):
        O = self.calculate_area() * (angle / 360)
        return O


circle = Circle(10)
angle=5

print(f'{circle.calculate_circumference():.2f}')
print(f"{circle.calculate_area():.2f}")
print(f"{circle.calculate_area_of_sector(angle):.2f}")
