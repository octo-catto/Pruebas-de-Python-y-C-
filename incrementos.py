import time
inicio = time.time()
for i in range(1, 10000):
    A = 0
for i in range(10000):
    A = A + 1
    print(A)
    fin = time.time()
print(fin-inicio)

