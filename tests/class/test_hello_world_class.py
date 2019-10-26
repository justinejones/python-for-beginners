""" Test file for Hello World Class Module"""
import pytest
from src.my_class.hello_world_class import HelloWorld


def test_class_default_constructor(capfd):
    """Test to validate that the main method is called."""
    result = "Hello World!"
    hello_world = HelloWorld()
    print(type(hello_world))
    assert type(hello_world) is not None
    hello_world.print_name()
    out, err = capfd.readouterr()
    assert result in out


def test_class_init(capfd):
    """
    Test to validate that the class is created
    witn non default constructor.
    """
    result1 = "Hello World Again!"
    result2 = "Hello World 2.0!"
    hello_world = HelloWorld(result1)
    hello_world2 = HelloWorld(result2)

    print(type(hello_world))
    assert type(hello_world) is not None
    hello_world.print_name()
    out, err = capfd.readouterr()
    assert result1 in out

    print(type(hello_world2))
    assert type(hello_world2) is not None
    hello_world2.print_name()
    out, err = capfd.readouterr()
    assert result2 in out
