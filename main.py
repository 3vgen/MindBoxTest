from shapes import Circle, Triangle, Rectangle


shapes = [Circle(2), Triangle(3, 4, 5), Rectangle(5, 5)]
for s in shapes:
    print(f"{s.name} — площадь: {s.area()}")
    if isinstance(s, Triangle):
        print(f"Прямоугольный: {s.is_right()}")
