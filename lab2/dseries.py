def dseries():
    inString = input("Enter a value for N :")
    n = int(inString)
    count = 0
    for x in range(1,n+1):
        count += x**2
    print(count)
    return count
dseries()
