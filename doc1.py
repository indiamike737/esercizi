import math
def radice():
    n1 = int(input())
    n2 = int(input())
    if n1 < 0 or n2 < 0:
        print("No")
        return
    else:
        p = n1*n2
    r = math.sqrt(p)
    print(r)



radice()
