import math

def expoApprox(x):
    approx = 1.00
    n = 1
    while(1):
        calc = float((x**n)/math.factorial(n))
        approx += calc
        if (calc < 0.01):
            break
        n += 1

    print(round(approx,3))
    

expoApprox(1)
expoApprox(2)
expoApprox(4)