
## returns s shifted by k, left if b is True, and right otherwise.
def bitshift(s,k,b):
    print("")
    store =""
    printing = ""
    if (b):
        for num in range(0,k):
            store += s[num]

        for num in range(k,len(s)):
            printing += s[num]
        
        print('true')

    if not (b):
        for num in range(0,len(s)-k):
            store += s[num]

        for num in range(len(s)-k,len(s)):
            printing += s[num]
        
    printing += store
        
    print("Initial string: ",s)
    print("Shifted string: ", printing)
    print("")

    


bitshift("100101",3,0) 