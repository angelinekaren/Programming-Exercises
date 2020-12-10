import math

class Shape:
    def __init__(self, color='green', filled=True):
        self.color = color
        self.filled = filled

    def getColor(self):
        return self.color

    def setColor(self, color):
        self.color = color

    def isFilled(self):
        if self.color=='' or self.filled==False:
            self.filled = False
            return 'not filled'
        else:
            self.filled = True
            return 'filled'

    def setFilled(self, filled):
        self.filled = filled

    def __str__(self):
        return f'A shape with color of {self.color} and {self.isFilled()}'


class Circle(Shape):
    def __init__(self, color='green', filled=True, radius=1.0):
        super().__init__(color, filled)
        self.radius = radius

    def getRadius(self):
        return self.radius

    def setRadius(self, radius):
        self.radius = radius

    def getArea(self):
        area = math.pi * (self.radius**2)
        return area

    def getPerimeter(self):
        perimeter = math.pi * (self.radius*2)
        return perimeter

    def __str__(self):
        return f'A circle with radius={self.radius}, which is a subclass of {super().__str__()}'

class Rectangle(Shape):
    def __init__(self, color='green', filled=True, width=1.0, length=1.0):
        super().__init__(color, filled)
        self.width = width
        self.length = length

    def getWidth(self):
        return self.width

    def setWidth(self, width):
        self.width  = width

    def getLength(self):
        return self.length

    def setLength(self, length):
        self.length = length

    def getArea(self):
        area = self.length*self.width
        return area

    def getPerimeter(self):
        perimeter = 2*(self.width + self.length)
        return perimeter

    def __str__(self):
        return f'A rectangle with width={self.width} and length={self.length}, which is a subclass of {super().__str__()}'

class Square(Rectangle):
    def __init__(self, side, color='green', filled=True, width=1.0, length=1.0):
        super().__init__(color, filled, width, length)
        self.side = side

    def getSide(self):
        return self.side

    def setSide(self, side):
        self.side = side

    def setWidth(self, side):
        Rectangle.width = self.side

    def setLength(self, side):
        Rectangle.length = self.side

    def __str__(self):
        return f'A square with side={self.side}, which is a subclass of {super().__str__()}'


if __name__ == "__main__":
    # testing 'Shape' class
    shape = Shape('red', False)
    print(shape)
    # testing 'Circle' class
    circle = Circle('blue', True, 2)
    print(circle)
    # testing 'Rectangle' class
    rectangle = Rectangle()
    print(rectangle)
    # testing 'Square' class
    square = Square(5, "red", False)
    print(square)


