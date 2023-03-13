import time

# Factorial de 10
n = 10
start_time = time.time()
factorial = 1
for i in range(1, n+1):
    factorial = factorial * i
end_time = time.time()
print("El factorial de", n, "es:", factorial)
print("Tiempo de ejecucion:", end_time - start_time, "segundos")


# Factorial de 100
n = 100
start_time = time.time()
factorial = 1
for i in range(1, n+1):
    factorial = factorial * i
end_time = time.time()
print("El factorial de", n, "es:", factorial)
print("Tiempo de ejecucion:", end_time - start_time, "segundos")

# Factorial de 200
n = 200
start_time = time.time()
factorial = 1
for i in range(1, n+1):
    factorial = factorial * i
end_time = time.time()
print("El factorial de", n, "es:", factorial)
print("Tiempo de ejecucion:", end_time - start_time, "segundos")
   

