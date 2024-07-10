def projection(v1: tuple[float, float], v2: tuple[float, float]) -> tuple[float, float]:
    # Координаты точки B
    B_X, B_Y = v1
    # Координаты точки C
    C_X, C_Y = v2
    # Вектор AB (так как A = (0,0), AB = B - A = (B_X - 0, B_Y - 0))
    AB_X = B_X
    AB_Y = B_Y
    # Скалярное произведение вектора AC (C - A) и вектора AB
    dot_product_AC_AB = C_X * AB_X + C_Y * AB_Y
    # Длина вектора AB в квадрате
    length_AB_squared = AB_X * AB_X + AB_Y * AB_Y
    
    # Параметр t, определяющий проекцию
    t = dot_product_AC_AB / length_AB_squared
    
    # Координаты точки D, которая является проекцией C на прямую AB
    D_X = AB_X * t
    D_Y = AB_Y * t
    return D_X, D_Y