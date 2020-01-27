def gpf(n):
    factor = 2
    while (n>1):
        if not n % factor:
            n /= factor
            factor -= 1
        factor += 1
    return factor

def gcd(a, b):
    while a % b != 0:
        remainder = a % b
        a = b
        b = remainder
    return b