class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def scale(self, factor):
        self.width *= factor
        self.height *= factor

    def is_square(self):
        return self.width == self.height

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

# Create a rectangle
rect = Rectangle(5, 10)
print(rect)
print("Area:", rect.area())
print("Perimeter:", rect.perimeter())

# Scale the rectangle
rect.scale(2)
print("\nAfter scaling:")
print(rect)
print("Area:", rect.area())
print("Perimeter:", rect.perimeter())

# Check if it's a square
print("\nIs it a square?", rect.is_square())

# Create a square
square = Rectangle(4, 4)
print("\nCreated a square:")
print(square)
print("Area:", square.area())
print("Perimeter:", square.perimeter())
print("Is it a square?", square.is_square())
