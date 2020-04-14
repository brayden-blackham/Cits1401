def nextRound(k,scores):
    temp = 100000
    cut = scores[k]
    for x in range(0,k):
        if (scores[x]<temp and not scores[x] == cut):
            temp = scores[x]
            
    print(temp)
    return temp
    



nextRound(5,[10,9,8,7,6,6,6,5,4])
nextRound(2, [0,0,0,0])