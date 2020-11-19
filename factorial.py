def factorial(n): 
    valor = 1
    i = 1
    while i <= n:
        valor = valor * i
        i = i + 1
    return valor

valor = 5
factorial = factorial(5)
print(factorial)
