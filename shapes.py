# shapes.py
import math
from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def area(self) -> float:
        """Вычисляет площадь фигуры"""
        pass

class Circle(Shape):
    def __init__(self, radius: float):
        super().__init__("Circle")
        if radius <= 0:
            raise ValueError("Радиус должен быть положительным")
        self.radius = radius

    def area(self) -> float:
        return math.pi * self.radius ** 2

class Triangle(Shape):
    def __init__(self, a: float, b: float, c: float):
        super().__init__("Triangle")
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("Стороны треугольника должны быть положительными")
        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError("Сумма любых двух сторон должна быть больше третьей")
        self.a = a
        self.b = b
        self.c = c

    def area(self) -> float:
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def is_right(self) -> bool:
        sides = sorted([self.a, self.b, self.c])
        return math.isclose(sides[0]**2 + sides[1]**2, sides[2]**2)


class Rectangle(Shape):
    
    def __init__(self, a, b: float):
        
        super().__init__("Rectangle")
        
        if a <=0 or b <= 0:
            raise ValueError("Стороны прямоугольника должны быть положительные")
        
        self.a = a
        self.b = b

    def area(self) -> float:
        return self.a * self.b
    
    

    

