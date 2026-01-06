def soma (a, b):

    c = a + b

    return c

def sub (a, b):

    c = a - b

    return c

def multi (a, b):

    c = a * b

    return c


def div (a, b):

    if b == 0:

        return None

    c = a / b

    return c

def fatorial(a):

    c = 1
    
    for i in range (1, a + 1):
        c *= i
    
    return c

def media(a):

    if len(a) == 0:
        return 0
    
    return sum(a) / len(a)



