# Implementar la función mayor, que reciba tres números y devuelva el mayor de ellos.


def mayor(a, b, c):
    if a>=b:
        if a>=c:
            return a
        return c
    elif b>=c:
        return b
    return c

assert mayor(5,10,6) == 10
assert mayor(10,5,6) == 10
assert mayor(5,6,10) == 10
