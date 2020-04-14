def listSorting(Names, Ages):
    for i in range(1, len(Ages)):
        j = i-1
        nxt_age = Ages[i]
        nxt_name = Names[i]
        while (Ages[j] < nxt_age) and (j >= 0):
            Ages[j+1] = Ages[j]
            Names[j+1] = Names[j]
            j = j-1
            if (Ages[j-1] == Ages[j]):
                print(Names[j-1], Names[j])
                for i in range(len(Names[j]) - 1):
                    if (Names[j-1][i] < Names[j][i]):
                        break
                    elif (Names[j-1][i] > Names[j][i]):
                        temp = Names[j-1]
                        Names[j-1] = Names[j]
                        Names[j] = temp
                        break
        Ages[j+1] = nxt_age
        Names[j+1] = nxt_name

    print("(", Names, ",", Ages, ")")


# listSorting(['Chris','Amanda','Boris','Charlie'],[35,43,55,35])
# listSorting(['Tim','Mark','Ali','Cherry','Tina'],[45,65,33,37,45])
listSorting(['George', 'Mark', 'Asad', 'Candy', 'Harry', 'Cira', 'Lee'], [35, 41, 35, 65, 41, 23, 41])
