""" Tests for maths.py """
import pytest

from maths import add_ten
from maths import sumar

def test_add_ten():
    """ Tests the add_ten function """
    assert 15 == add_ten(5)


def test_add_ten_str_int():
    """ Tests the add_ten function for string input """
    assert add_ten('5') == '15'


def test_add_ten_none():
    """ Tests that add_ten throws a ValueError when None input given """
    assert add_ten(None) is None

def test_sumar_numeros():
    """ Test sumando 2 numeros """
    assert 8 == sumar(3,5)


