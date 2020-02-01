from itertools import islice

class Prime:

    def __init__(self, limit):
        self.limit = limit
        self.plist = [True] * limit
        self.plist[0] = self.plist[1] = False

    def __iter__(self):
        for i, isprime in enumerate(self.plist):
            if isprime:
                yield i
                for n in range(i*i, self.limit, i):
                    self.plist[n] = False

    def __getitem__(self, n):
        return next(islice(self.__iter__(), n, None))

    #Problem 3
    #Needs 64-bit python installed

    #We need a prime generator probably
    #Sieve of Eratosthenes
    #https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

    #My initial attempt brute force, naive
    #Not a sieve, since it doesn't mark things as true/false
    #Slow, doesn't work with large numbers

    def myprimegen(self, n):
        p = 2
        primelist = list(range(2, n))
        print("hello")
        for k in range(len(primelist)):
            factorlist = range(p+p, n, p)
            for factor in factorlist:
                for i in primelist.copy():
                    if i == factor:
                        primelist.remove(factor)
            print(p)
            p = primelist[(primelist.index(p)+1) % len(primelist)]

        print(primelist)

    #prime(10000)

    #Found a faster version!
    #https://stackoverflow.com/questions/3939660/sieve-of-eratosthenes-finding-primes-python
    #Looks like I was going the wrong way about it with the algorithm
    #Better to mark the value at an index(representing a prime) as false
    #OverflowError with large numbers! This is due to how generators work
    #Could fix with using smaller array types, like bytearrays?


    def primegen(self, limit):
        a = [True] * limit
        a[0] = a[1] = False
        for i, isprime in enumerate(a):
            if isprime:
                yield i
                for n in range(i*i, limit, i):
                    a[n] = False
