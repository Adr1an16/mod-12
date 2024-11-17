# Adrian
# 11/15/2024
# This program defines a Flower class with attributes and methods, creates instances of the class, and calls the methods to demonstrate object-oriented programming in Python.

class Flower:
    def __init__(self, name):
        self.name = name  # Initialize the attribute 'name' of the class Flower.

    def grow(self):
        print("The " + self.name + " is growing.")  # Method to print that the flower is growing.

    def bloom(self):
        print("The " + self.name + " is blooming.")  # Method to print that the flower is blooming.

def main():
    flower1 = Flower("Rose")  # Create an instance of Flower with the name 'Rose'.
    flower1.grow()  # Call the grow method for the Rose instance.
    flower1.bloom()  # Call the bloom method for the Rose instance.
    
    flower2 = Flower("Daisy")  # Create an instance of Flower with the name 'Daisy'.
    flower2.grow()  # Call the grow method for the Daisy instance.
    flower2.bloom()  # Call the bloom method for the Daisy instance.
    
    flower3 = Flower("Tulip")  # Create an instance of Flower with the name 'Tulip'.
    flower3.grow()  # Call the grow method for the Tulip instance.
    flower3.bloom()  # Call the bloom method for the Tulip instance.

if __name__ == "__main__":
    main()  # Execute the main function to run the program.
