import time
inicio = time.time()
for i in range(1, 1000000000):
    A = 1
fin = time.time()
print('%.3f' % float(fin-inicio))

