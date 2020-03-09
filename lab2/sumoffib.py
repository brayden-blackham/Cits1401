import math


def main():
    n = 30
    
    last = 1
    seclast = 1
    now = 2
    sum = 4
    print("Fib\t sum\n")
    for y in range(1, n-3):
        seclast = last
        last = now
        now = seclast + last
        sum = sum + now
        print(now , "\t" , sum , "\n")

    return


main()
