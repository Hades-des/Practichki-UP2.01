
N = int(input("Введите положительное число N: "))
result = 1
for i in range(1, N + 1):
      result *= i

if N < 0:
    print("Факториал определен только для неотрицательных чисел.")
else:
    fact = result
    print(f"Факториал числа {N} равен {fact}")
