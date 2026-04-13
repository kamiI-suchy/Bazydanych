class Point:
    _counter = 0

    def __init__(self, x, y, color='yellow'):
        Point._counter += 1
        self.id = Point._counter
        self.x = x
        self.y = y
        self.color = color

    def __repr__(self):
        return f"id: {self.id}, ({self.x}, {self.y}), color: {self.color}"

    def move(self, shift_x, shift_y):
        self.x += shift_x
        self.y += shift_y

    def chColor(self, new_color):
        self.color = new_color


class PointsDict(dict):
    def __str__(self):
        return '\n'.join(f"'{k}': {v}" for k, v in self.items())


points = PointsDict()
points['p1'] = Point(2, 3, "blue")
points["p2"] = Point(4, 5)
points["p3"] = Point(10, 20, "green")
print(points)

print()

points.pop("p2")
points["p1"].move(1, 2)

points["p2"] = Point(7, 8)
points["p3"].move(4, 5)

points["p1"].chColor("orange")
print(points)
