class Rectangle:
    def __init__(self):
        self.width, self.length = 0, 0  # set default dimensions to zero

    # set shape's width
    def setWidth(self, width):
        self.width = width

    # set shape's length
    def setLength(self, length):
        self.length = length

    # get shape's area
    def area(self):
        return self.length * self.width

    # get shapes perimeter
    def perimeter(self):
        return 2 * (self.length * self.width)


# create subclass Square and inherit from superclass Rectangle
class Square(Rectangle):

    # override the setWidth functionality for the Square object
    def setWidth(self, width):
        self.width, self.length = width, width

    # override the setLength functionality for the Square object
    def setLength(self, length):
        self.width, self.length = length, length


if __name__ == "__main__":
    rectangle = Rectangle()
    rectangle.setWidth(12)
    rectangle.setLength(15)
    print(f"Rectangle Area: {rectangle.area()}")  # Rectangle Area: 180
    print(f"Rectangle perimeter: {rectangle.perimeter()}")  # Rectangle perimeter: 360

    print()
    square = Square()
    square.setLength(15)
    square.setWidth(20)
    print(f"Square Area: {square.area()}")  # Square Area: 400
    print(f"Square perimeter: {square.perimeter()}")  # Square perimeter: 800
