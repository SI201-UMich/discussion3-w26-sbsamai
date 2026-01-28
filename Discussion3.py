import math

class Rectangle():
    # Create the constructor "__init__" method
    def __init__(self, length, width):
        self.length = length
        self.width = width
    # YOUR CODE HERE



    # Create the "__str__" method

    # YOUR CODE HERE
    def __str__(self): 
        return str("A rectangle with " + self.width + "and" + self.length)


    # Create the "area_calculator" method

    # YOUR CODE HERE
    def area_calculator(self):
        return self.length * self.width



    # Create the "__eq__" method
    # 
    def __eq__(self, other):
    # Returns a boolean value
        if self.width == other.width and self.length == other.length:
            return True
        else:
            return False
    # YOUR CODE HERE


    


def main():
    r1 = Rectangle(10, 10)
    # call the __str__ method
    print(r1)
    # call the area_calculator method
    print("Area:", r1.area_calculator())


    r2 = Rectangle(10, 15)
    print(r2)
    print("Area:", r2.area_calculator())
    # call the __eq__ method
    print(r1 == r2)
    print()

    # you can create additional rectangle objects to 
    # test your code or learn more about how the class behaves
    pass

if __name__ == "__main__":
    main()