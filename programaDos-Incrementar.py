import time
inicio = time.time()
A = 0
for i in range(1000000000):
    A = A + 1
fin = time.time()
print('%.3f' % float(fin-inicio))
