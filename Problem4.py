#Problem 4
#We iterate over each letter to the halfway point from the start and the end
#Works for even and odd digits e.g 5000 vs 50000
#Answer is the highest found palindrome

from itertools import product

period = range(100, 1000)
answer = 0

for i in product(period, period, repeat=1):
    resultint = i[0] * i[1]
    resultstr = str(resultint)
    length = len(resultstr)
    if all(resultstr[j] == resultstr[(-j-1)] for j in range((len(resultstr)//2) + 1)):
        if resultint > answer:
            answer = resultint

print(answer)