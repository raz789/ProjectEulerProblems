#Problem 6
sumsq = 0
squaresum = 0

for i in range(1, 101):
    sumsq += i*i
    squaresum += i
    

squaresum *= squaresum


answer = squaresum - sumsq
print(answer)