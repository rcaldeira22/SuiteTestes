import pytest
from src.triangle import triangle_type

def test_invalid(): #TC1
        assert triangle_type(3,2,1) == "Not a triangle"

def test_equilatero(): #TC2
        assert triangle_type(3,3,3) == "Equilateral"

def test_isosceles(): #TC3
        assert triangle_type(3,3,4) == "Isosceles"

def test_escaleno(): #TC4
        assert triangle_type(3,4,5) == "Scalene"





