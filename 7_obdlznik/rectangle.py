class Rectangle:
    def __init__(self, a: float, b: float, x: float, y: float):
        """
        Constructor.
        a, b = the lengths of the sides of the rectangle (width, height).
        (x, y) = coordinates of the upper-left corner.
        """
        self.__a = a  # Width
        self.__b = b  # Height
        self.__x = x  # X-coordinate of the upper-left corner
        self.__y = y  # Y-coordinate of the upper-left corner

    def setDimensions(self, a: float, b: float) -> None:
        """Set new dimensions a x b for the rectangle."""
        self.__a = a
        self.__b = b

    def getDimensions(self) -> tuple:
        """Return a tuple (a, b) with the current dimensions."""
        return (self.__a, self.__b)

    def isSquare(self) -> bool:
        """
        Return True if the rectangle is a square (a == b), otherwise False.
        """
        return self.__a == self.__b

    def getArea(self) -> float:
        """
        Return the area of the rectangle (a * b).
        """
        return self.__a * self.__b

    def getCircumference(self) -> float:
        """
        Return the perimeter (circumference) of the rectangle: 2 * (a + b).
        """
        return 2 * (self.__a + self.__b)

    def getPosition(self) -> tuple:
        """
        Return a tuple (x, y) representing the upper-left corner of the rectangle.
        """
        return (self.__x, self.__y)

    def move(self, deltaX: float, deltaY: float) -> None:
        """
        Move the rectangle by deltaX (in the horizontal direction) and deltaY (in the vertical direction).
        """
        self.__x += deltaX
        self.__y += deltaY

    def moveTo(self, x: float, y: float) -> None:
        """
        Move the rectangle so its upper-left corner is now at (x, y).
        """
        self.__x = x
        self.__y = y

    def contains(self, px: float, py: float) -> bool:
        """
        Return True if the point (px, py) is inside or on the boundary of the rectangle.
        Here, we assume the rectangle extends from x to x+a horizontally,
        and from y to y+b vertically.
        """
        # Rectangle boundaries:
        left = self.__x
        right = self.__x + self.__a
        top = self.__y
        bottom = self.__y + self.__b

        # Check if px, py is within or on these boundaries
        return (left <= px <= right) and (top <= py <= bottom)

    def makeSquare(self) -> None:
        """
        Modify the rectangle into a square by setting the longer side to the length of the shorter side.
        """
        if self.__a < self.__b:
            self.__b = self.__a
        else:
            self.__a = self.__b


if __name__ == "__main__":
    # Example usage
    rect = Rectangle(10, 5, 2, 3)
    print("Initial position:", rect.getPosition())        # (2, 3)
    print("Initial dimensions:", rect.getDimensions())    # (10, 5)
    print("Is square?", rect.isSquare())                  # False
    print("Area:", rect.getArea())                        # 50
    print("Circumference:", rect.getCircumference())      # 30

    # Move the rectangle
    rect.move(3, 2)
    print("New position after move:", rect.getPosition()) # (5, 5)

    # Check contains
    print("Contains point (5,5)?", rect.contains(5, 5))    # True
    print("Contains point (20,20)?", rect.contains(20, 20))# False

    # Make it a square
    rect.makeSquare()
    print("Dimensions after makeSquare():", rect.getDimensions())  # (5, 5)
    print("Is now a square?", rect.isSquare())                     # True
