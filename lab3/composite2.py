
## Function composite2(n)
## Input: n Integer
## Return: the Nth composite number which is NOT divisible by 2. 


def composite2(n):
    print("")

    # set store to first composite
    store = 4

    count = 0
    x = 0

    while(count != n):
        x += 1
        if (isComposite(x) and (x%2)):
            store = x
            count +=1
        
    print ('Return: ',store)


    print("")


def isComposite(n): 
  
    # Edge Case
    if (n <= 3): 
        return False
  
    # This is checked so that we can skip  
    # middle five numbers in below loop 
    if (n % 2 == 0 or n % 3 == 0): 
        return True
    i = 5
    while(i * i <= n): 
          
        if (n % i == 0 or n % (i + 2) == 0): 
            return True
        i = i + 6
          
    return False

composite2(333)