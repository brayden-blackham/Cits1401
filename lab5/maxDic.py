def maxdic(dic):
    max = 0
    for x in dic:
        print(dic[x])
        listy = dic[x]
        for value in listy:
            if max < value:
                max = value
    return max
x = maxdic({11:[12,12,321,4234],12:[11,323,4300],13:[15,1,9912,10101,-123],14:[2341],15:[-13,0,1686],36:[2301,123]}) 
print(x)
