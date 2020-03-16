def oddfinder():
    inString = input("Enter 10 comma seperated values :")
    value = ''
    vals = []
    for elem in inString:
        if (elem == ','):
            vals.append(value)
            value = ''
        else:
            value = value + elem
    vals.append(value)
    print(vals)

    count = 0
    for num in vals:
        num = int(num)
        if (((num % 2) != 0) and (num > 0)):
            count += 1
    print ('Number of Odd Numbers is :', count)
    return count
        
oddfinder()
