from util import lcme

#Gonna brute force this first
#long time

def commonmultiple():
    answer = 0
    for i in range(20, 100000000000):
        tally = 0
        for j in range(1, 21):
            if i % j == 0:
                tally += 1
        if tally == 20:
            print("20: " + str(i))

#Looks like the method to do so is LCM
#You can get it using the following:
# a * b / gcd(a, b)
#https://en.wikipedia.org/wiki/Least_common_multiple

print(lcme(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20))

