from random import randint as rnd
n = 24
A = []

for t in range(n):
    A.append(rnd(-100, 100))
B = [1] * n

for i in range(1, n):
    if A[i] > A[i-1]:
        B[i] = B[i-1] + 1
    else:
        B[i] = 1

max_len = max(B)
max_index = B.index (max_len)
print('Изначальный массив\n', A)
print('Макс длина:', max_len)
print('Нужная подпоследовательность\n', A[max_index-max_len + 1:max_index + 1])