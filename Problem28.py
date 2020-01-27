#Problem 28
#We can see a pattern emerge. Each diagonal number for top right is (z+2)^2
sum = 0

for i in range(1, 501):
    corners = (((1+(i*2))*(1+(i*2))))
    cornerreducation = (i*2)
    sum += (corners*4) - (cornerreducation*6)

#+1 for the center number
print(sum+1)