import time

# Factorial de 100
n = 100
inicio = time.time()
factorial = 1
for i in range(1, n):
    factorial = factorial * i

# Factorial de 1000
n = 1000
factorial = 1
for i in range(1, n):
    factorial = factorial * i

# Factorial de 2000
n = 2000
factorial = 1
for i in range(1, n):
    factorial = factorial * i
fin = time.time()
print('%.6f' % float(fin-inicio))
   

