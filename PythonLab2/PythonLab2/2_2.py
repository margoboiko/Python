import math
    
n = int(input('Enter n: '))

def sum(k):
    def a(k):
        if k == 1: 
           return 1
        else:
           return 3 * b(k - 1) + (2 * b(k - 1))

    def b(k):
        if k == 1: 
            return 1
        else:
            return a(k - 1)**2 + b(k - 1)

    if k == 1:
        return 1
    else:
        return sum(k - 1) + (2**k) / (1 + a(k) + b(k))

print(sum(n))
