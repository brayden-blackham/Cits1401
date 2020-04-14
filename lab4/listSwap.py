def listSwap(lst):
    for each in range(0,len(lst),2):
        if(len(lst) == (each+1)):
            break
        temp = lst[each+1]
        lst[each+1] = lst[each]
        lst[each]=temp
    print(lst)

    

#listSwap([1,2,3,4,5])
#listSwap([12,15,"Ali","Chris",True,False])
listSwap([-1,7,[3,4],"Joe",90,[33],"True"])