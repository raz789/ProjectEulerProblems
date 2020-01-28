#Problem 1

sum = 0

for i in range(1000):
    if (i % 3 == 0) or (i % 5 == 0):
        sum += i

print(sum)

#Alternative shorthand
#print(sum([for i in range(0, 1000) if i % 3 == 0 or i % 5 == 0]))