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

def lcm(a, b):
    return (a*b)/gcd(a,b)

#Return the lcm based on a list of numbers
def lcme(*args):
    if len(args) == 1:
        return args[0]
    else:
        n = lcm(args[0], args[1])
        return lcme(int(n), *args[2:])

