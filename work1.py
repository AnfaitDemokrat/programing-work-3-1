import numpy as np
import matplotlib.pyplot as plt
#1
# 1.1. Масив 25х25 шз втпадковим значенням.
arr_25 = np.random.rand(25, 25)
print("min =", np.min(arr_25), ", max=", np.max(arr_25))
#1.2. Матриця 6х6 з елемнатами під діагональ від 1-5
mat_6x6 = np.zeros((6, 6), dtype=int)
for i in range(1, 6):
    for j in range(i):
        mat_6x6[i, j] = j + 1
print("Матриця з елементів під діагоналю:\n", mat_6x6) 
#1.3. Матриця доботку двух інчих матриць.
A = np.random.randint(0, 10 , (5, 3))
B = np.random.randint(0, 10 , (3, 2))       
C = A @ B
print("Матриця доботку", C)
#1.4. Масив з 20 елементів міняюший знаки 10-16 елементів.
arr = np.random.randint(-20, 20 , 20)
print("До зміни:",arr)
arr[9:16] *= -1
print("Після зміни",arr)
#2
#2.1.
x = np.random.rand(5)
y = np.random.rand(5)
couchy = 1 / np.subtract.outer(x, y)
det = np.linalg.det(couchy)
print("Матриця Коші:\n",couchy)
print("Визначник матриці Коші =",det)
#2.2.
x_vals = np.linspace(0 , 10 ,500)
y_vals = np.sin(x_vals) + np.cos(2 + x_vals)
max_inx = np.argmax(y_vals)
min_inx = np.argmin(y_vals)
print("Max x =", x_vals[max_inx], " y = " , y_vals[max_inx])
print("Min x =", x_vals[min_inx], " y =", y_vals[min_inx])
#3
# Диференціальне рівняння: y' = y(1 - 2x), y(0) = 1
def dydx(x, y):
    return y * (1 - 2 * x)

# Аналітичне рішення: y(x) = exp(x - x^2)
def y_analytic(x):
    return np.exp(x - x**2)

# Метод Ейлера
def euler_method(f, x0, y0, h, x_end):
    x_vals = np.arange(x0, x_end + h, h)
    y_vals = [y0]
    y = y0
    for x in x_vals[:-1]:
        y += h * f(x, y)
        y_vals.append(y)
    return x_vals, np.array(y_vals)

# Метод Рунге-Кутта 4-го порядку
def runge_kutta_4(f, x0, y0, h, x_end):
    x_vals = np.arange(x0, x_end + h, h)
    y_vals = [y0]
    y = y0
    for x in x_vals[:-1]:
        k1 = f(x, y)
        k2 = f(x + h / 2, y + h * k1 / 2)
        k3 = f(x + h / 2, y + h * k2 / 2)
        k4 = f(x + h, y + h * k3)
        y += (h / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
        y_vals.append(y)
    return x_vals, np.array(y_vals)

# Параметри
x0, y0 = 0, 1
h = 0.1
x_end = 2

# Обчислення
x_euler, y_euler = euler_method(dydx, x0, y0, h, x_end)
x_rk, y_rk = runge_kutta_4(dydx, x0, y0, h, x_end)
x_vals = np.linspace(x0, x_end, 200)
y_exact = y_analytic(x_vals)

# Графік
plt.figure(figsize=(10, 6))
plt.plot(x_vals, y_exact, label='Аналітичне рішення', color='black', linestyle='dashed')
plt.plot(x_euler, y_euler, label='Метод Ейлера', marker='o')
plt.plot(x_rk, y_rk, label='Метод Рунге-Кутта', marker='x')
plt.title("Порівняння чисельних методів з аналітичним рішенням")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.legend()
plt.show()