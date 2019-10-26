"""Hello World Class."""


class HelloWorld:
    """Class Hello World!"""

    def __init__(self, my_name="Hello World!"):
        """Initializer for the HelloWorld class"""
        self.my_name = my_name

    def print_name(self):
        """Prints the value of my_name"""
        print(str(self.my_name))
