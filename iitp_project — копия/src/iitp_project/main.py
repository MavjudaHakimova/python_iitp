import numpy as np
import matplotlib.pyplot as plt

# Линейная интерполяция
def linear_interpolation(points, x):
    for i in range(len(points) - 1):
        x_i_1, y_i_1 = points[i]
        x_i, y_i = points[i + 1]
        if x_i_1 <= x <= x_i:
            return y_i_1 + (x - x_i_1) * (y_i - y_i_1) / (x_i - x_i_1)

# Пример использования линейной интерполяции
points = [(1, 2), (2, 4), (3, 3), (4, 5), (5, 2)]
x = 2.5
y = linear_interpolation(points, x)
print(f"Значение y в точке x={x}: {y}")

# Построение графика линейной интерполяции
x_values = [p[0] for p in points]
y_values = [p[1] for p in points]

plt.figure()
plt.plot(x_values, y_values, 'o-', label='Исходные точки')
plt.axvline(x=x, color='r', linestyle='--', label=f'x={x}')
plt.axhline(y=y, color='g', linestyle='--', label=f'y={y}')
plt.title('Линейная интерполяция')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid()
plt.savefig('linear_interpolation.pdf')
plt.close()

# Полиномиальная интерполяция
def interpolate_canonical(points):
    # Матрица Вандермонда
    n = len(points)
    matrix = np.zeros((n, n))
    for i in range(n):
        x_i = points[i][0]
        for j in range(n):
            matrix[i][j] = pow(x_i, j)
    a = np.linalg.solve(matrix, [point[1] for point in points])
    return a

# Алгоритм Горнера для вычисления полинома в данной точке
def evaluate_polynomial(a, x):
    result = 0
    for a_i in reversed(a):
        result = result * x + a_i
    return result

# Пример полиномиальной интерполяции
points_poly = [(0, 1), (1, 2), (4, 0), (5, 3)]
coefficients = interpolate_canonical(points_poly)

# Пример вычисления значения полинома в точке
x_poly = 3 
y_poly = evaluate_polynomial(coefficients, x_poly)
print(f"Значение полинома в точке x={x_poly}: {y_poly}")

# Построение графика полиномиальной интерполяции
x_range = np.linspace(0, 5, 100)
y_range = [evaluate_polynomial(coefficients, x_val) for x_val in x_range]

plt.figure()
plt.plot(x_range, y_range, label='Полиномиальная интерполяция')
plt.scatter(*zip(*points_poly), color='red', label='Исходные точки')
plt.axvline(x=x_poly, color='r', linestyle='--', label=f'x={x_poly}')
plt.axhline(y=y_poly, color='g', linestyle='--', label=f'y={y_poly}')
plt.title('Полиномиальная интерполяция')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid()
plt.savefig('polynomial_interpolation.pdf')
plt.close()
