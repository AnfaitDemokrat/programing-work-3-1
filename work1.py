import numpy as np
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