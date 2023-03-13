import time
inicio = time.time()
for i in range(1, 1000000):
    var_name = "A" + str(i)
    exec(var_name + " = 1")
    print(var_name)
    fin = time.time()
print(fin-inicio)

