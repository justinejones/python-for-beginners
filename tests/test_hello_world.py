""" Test file for Hello World Module"""
import pytest
from src.hello_world import main_method


def test_main_method(capfd):
    """Test to validate that the main method is called."""
    main_method()
    out, err = capfd.readouterr()
    assert out == "Hello World!\n"
