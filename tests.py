""" Tests for maths.py """
import pytest

from maths import hello
from maths import sumar

def test_hello():
    """ Test escribir hello world """
    assert "Hello World" == hello()

def test_sumar_numeros():
    """ Test sumando 2 numeros """
    assert 8 == sumar(3,5)


