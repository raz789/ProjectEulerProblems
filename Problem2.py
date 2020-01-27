#Problem 2

def fibonacci(first, second, limit):
    next = first + second
    if next >= limit:
        return [first, second]
    else:
        return [first, *fibonacci(first=second, second=next, limit=limit)]


print(sum([i for i in fibonacci(1, 2, 4000000) if i % 2 == 0]))