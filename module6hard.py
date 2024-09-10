class Figure():
    sides_count = 0
    def __init__(self, color, sides, filled = True):
        self.sides = sides
        self.color = color

    def get_color(self):
        return self.color

    def is_valid_color(self, r, g, b):

        if type(r) == int and type(g) == int and type(b) == int:
            if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
                return True
        return False

    def set_color(self, r, g, b):
        if self.is_valid_color(r, g, b):
            self.color = list((r, g, b))

    def is_valid_sides(self, *sides):
        return all(isinstance(side, int) and side > 0 for side in sides) and len(sides) == self.sides_count

    def get_sides(self):
        return self.sides_list

    def __len__(self):
        return sum(self.sides_list)

    def set_sides(self, *new_sides):
        if self.is_valid_sides(*new_sides):
            self.sides_count = len(new_sides)
            self.sides_list = list(new_sides)




class Circle(Figure):
    sides_count = 1
    def __init__(self, color, side, filled = True):
        super().__init__(color, side)
        self.set_color(color[0], color[1], color[2])
        self.set_sides(side)
        self.radius = side/ 2 * 3.14

    def get_square(self):
        return 3.14 * self.radius ** 2

class Triangle(Figure):
    sides_count = 3
    def __init__(self, color, sides, filled = True):
        super().__init__(color, sides)
        self.set_color(color[0], color[1], color[2])
        self.set_sides(sides)

    def get_square(self):
        p = len(self) / 2
        return (p * (p - self.sides[0])* (p - self.sides[1])* (p - self.sides[2])) ** 0.5


class Cube(Figure):
    sides_count = 12
    def __init__(self, color, sides, filled = True):
        super().__init__(color, sides)
        self.set_color(color[0], color[1], color[2])
        self.set_sides(*([sides]*self.sides_count))
    def get_volume(self):
        return self.sides_list[0] ** 3
