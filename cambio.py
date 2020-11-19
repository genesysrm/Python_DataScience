

def temperatura(celcius):
    temperatura = (celcius * 9/5) + 32 
    return temperatura

faren = temperatura(18)
print(faren)

def celcius(temp):
    temperatura = (temp - 32) * 5.0/9.0
    return temperatura

celcius = celcius(64.4)
print(celcius)

