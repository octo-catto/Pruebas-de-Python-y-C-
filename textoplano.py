import time
inicio = time.time()
for i in range(1000):
    with open('archivo.txt', 'a') as f:
        f.write(str(i) + '\n')
fin = time.time()
print('%.3f' % float(fin-inicio))
