import random

n = int(input("Masukkan nilai N: "))

for i in range(1, n+1):
    a = random.uniform(0, 0.5)
    print(f"Data ke: {i} => {a}")
