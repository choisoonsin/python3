class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def area(self):
        return self._width * self._height

if __name__ == '__main__':
    rect = Rectangle(5, 10)
    print(rect.area)  # Output: 50

    rect.width = 7
    rect.height = 12
    print(rect.area)  # Output: 84