# test_shapes.py
import math
import pytest
from shapes import Circle, Triangle, Rectangle


def test_circle_area():
    c = Circle(1)
    assert math.isclose(c.area(), math.pi)

def test_triangle_area():
    t = Triangle(3, 4, 5)
    assert math.isclose(t.area(), 6)

def test_triangle_is_right():
    t = Triangle(3, 4, 5)
    assert t.is_right()
    t2 = Triangle(2, 3, 4)
    assert not t2.is_right()

def test_rectangle_area():
    r = Rectangle(3, 4)
    assert r.area() == 12

def test_names():
    assert Circle(1).name == "Circle"
    assert Triangle(3, 4, 5).name == "Triangle"
    assert Rectangle(2, 5).name == "Rectangle"

def test_invalid_triangle():
    with pytest.raises(ValueError):
        Triangle(1, 2, 3)  # не существует

def test_invalid_circle():
    with pytest.raises(ValueError):
        Circle(-1)

def test_invalid_rectangle():
    with pytest.raises(ValueError):
        Rectangle(-1, 2)
    with pytest.raises(ValueError):
        Rectangle(2, -1)
