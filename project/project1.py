'''
Written By: Brayden Blackham
Student Number: 22226136
Unit: Cits1401
Project 1: Create a Python 3 Program to calculate differant Metrics for a Class.
'''

# The main function is where other functions are called
# Input: csvfile, str , The name of the CSV File
# Return: minimum, list, The minimum mark for each subject
# Return: maximum, list, The maximum mark for each subject
# Return: average, list, The average mark for each subject
# Return: stdDev, list, The stdDev of marks for each subject
# Return: spCor, list, The Spearman's Correlation of the marks for each subject
def main(csvfile):
    ## Helper Varibles.
    csvLines = readFile(csvfile)
    classes = getClasses(csvLines)
    checkValidity(csvLines,classes)
    sortAlphabetical(csvLines)
    markDict = createDict(csvLines, classes)

    ## Call Functions to Return Lists
    return minimum(csvLines, markDict),maximum(csvLines, markDict),average(csvLines, markDict),stdDev(csvLines, markDict),spCor(markDict, classes)


### START: HELPER FUNCTIONS ###

# The readFile function opens, reads and closes the file
# Input: csvfile, str , The name of the CSV File
# Return: csvLines, list, A list of all the lines in the CSV
def readFile(csvfile):
    f = open(csvfile)
    csvLines = []
    for line in f:
        s = line.strip().split(',')
        csvLines.append(s)
    f.close()
    return csvLines

# The getClasses function creates a list of class names as well as removing that row from csvLines
# Input: csvLines, list, A list of all the lines in the CSV
# Return: classes, list, A list of class names
def getClasses(csvLines):
    classes = csvLines[0]
    del classes[0]
    del classes[0]
    del csvLines[0]
    return classes

# The checkValidity function handles the 'Same Name & Same Score' Error
# Input: csvLines, list, A list of all the lines in the CSV
# Input: classes, list, A list of class names
# ERROR: SAME NAME AND SAME SUBJECT SCORE, exit(), Will exit if the 'Same Name & Same Score' is found.
def checkValidity(csvLines,classes):
    names = []
    for line in csvLines:
        names.append(line[0])
    ##Check for duplicate Names
    for i in range(0,len(names)):
        for j in range(0,len(names)):
            ## If there are duplicate names, Check for same scores and Print ERROR and exit()
            if (i != j and names[i] == names[j]):
                for k in range(2,len(csvLines[0])):
                    if (csvLines[i][k] == csvLines[j][k]):
                        print("ERROR: SAME NAME AND SAME SUBJECT SCORE; Name: ", names[i],",Subject ",classes[k-2],", Score: ", csvLines[i][k])
                        exit()

# The sortAlphabetical function sorts csvLines into alphabetical order, to help with rank calculation later.
# Input: csvLines, list, A list of all the lines in the CSV
def sortAlphabetical(csvLines):
    for i in range(len(csvLines)): 
        for j in range(0, len(csvLines)-i-1): 
            if csvLines[j][0] > csvLines[j+1][0] : 
                csvLines[j], csvLines[j+1] = csvLines[j+1], csvLines[j]

# The createDict function creates a dictionary so all the infomation for a student is referanceable
#       via there ID which is unique(because name is not).
# Input: csvLines, list, A list of all the lines in the CSV
# Input: classes, list, A list of class names
# Return: markDict, dict, A dictionary including the Name, Marks, and Total Score for each student.
def createDict(csvLines, classes):
    lines = csvLines
    markDict = {}
    id = 0
    for line in lines:
        name = line[0]
        del line[0]
        del line[0]
        marks = {}
        total = 0
        for x in range(0, len(line)):
            total += float(line[x])
            marks[classes[x]] = line[x]
        markDict[id] = {
            "Name": name,
            "Marks": marks,
            "Total": total
        }
        id = id+1
    return(markDict)

# The helperStd function calculates the standard deviation of a column (subject).
# Input: col, list, A list of all the marks in a subject.
# Return: float, The standard deviation for the input column (subject).
def helperStd(col):
    variance = sum([((num - (sum(col) / len(col))) ** 2)
                    for num in col]) / len(col)
    return float(variance ** 0.5)

# The calculateRank function calculates the rank for every student in every subject and adds the rank to the markDict.
# Input: markDict, dict, A dictionary including the Name, Marks, and Total Score for each student.
# Input: classes, list, A list of class names
def calculateRank(markDict, classes):
    # Loop through classes
    for clas in classes:
        orderedScores = []
        # Order the scores.
        for id in markDict:
            orderedScores.append(float(markDict[id]["Marks"][clas]))
            orderedScores.sort(reverse=True)
        # Loop though ordered score and match them with there ordered mark, giving them a rank in the process.
        for x in range(0,len(orderedScores)):
            for id in markDict:
                if (float(markDict[id]["Marks"][clas]) == orderedScores[x]):
                    # If the person already has a rank for that subject, skip onwards
                    if str(clas) + "Rank" in markDict[id]:
                        break
                    # else, give them a rank
                    else:
                        markDict[id][clas + "Rank"] = x+1
        #Logic to Handle the same score.
        for x in markDict:
            for y in markDict:
                # If The rank is the same, give the second a higher rank
                if x!=y and (markDict[x][clas + "Rank"] == markDict[y][clas + "Rank"]):
                    markDict[y][clas + "Rank"] += 1
    # Rank Total Scores
    orderedTotalScores = []
    # Order the scores.
    for id in markDict:
        orderedTotalScores.append(float(markDict[id]["Total"]))
        orderedTotalScores.sort(reverse=True)
    # Loop though ordered score and match them with there ordered mark, giving them a rank in the process.
    for x in range(0,len(orderedTotalScores)):
        for id in markDict:
            if (float(markDict[id]["Total"]) == orderedTotalScores[x]):
                if "TotalRank" in markDict[id]:
                    break
                else:
                    markDict[id]["TotalRank"] = x+1
    #Logic to Handle the same score.
    for x in markDict:
        for y in markDict:
            # If The rank is the same, give the second a higher rank
            if x!=y and (markDict[x]["TotalRank"] == markDict[y]["TotalRank"]):
                markDict[y]["TotalRank"] += 1

# The calculateSumOfDifSq function calculates 
# Input: markDict, dict, A dictionary including the Name, Marks, and Total Score for each student.
# Input: classes, list, A list of class names  
# Return: sumOfDifSqTotal, list, A list of the Total Sum of Differance Squared for each subject.
def calculateSumOfDifSq(markDict, classes):
    sumOfDifSqTotal= []
    # Loop though the classes and add the calcutation to the list.
    for clas in classes:
        sumOfDifSq = 0
        for id in markDict:
            dif2 = (markDict[id]["TotalRank"] - markDict[id][clas + "Rank"])**2
            markDict[id][clas + "Dif2"] = dif2
            sumOfDifSq += dif2
        sumOfDifSqTotal.append(sumOfDifSq)
    return sumOfDifSqTotal



### END: HELPER FUNCTIONS ###

### START: RETURN FUNCTIONS ###

# The minimum function finds the minimum mark for each subject
# Input: csvLines, list, A list of all the lines in the CSV
# Input: markDict, dict, A dictionary including the Name, Marks, and Total Score for each student
# Return: minMarks, list, The minimum mark for each subject
def minimum(csvLines, markDict):
    minMarks = []
    # Find the min mark for each Subject
    for x in range(0, len(csvLines[0])):
        minX = 1000000
        for y in range(0, len(csvLines)):
            if (minX > float(csvLines[y][x])):
                minX = float(csvLines[y][x])
        minMarks.append(round(minX, 4))
    # Find the min mark for "Total"
    minTotal = 1000000
    for id in markDict:
        if (minTotal > float(markDict[id]["Total"])):
            minTotal = float(markDict[id]["Total"])
    minMarks.append(round(minTotal, 4))
    return minMarks

# The maximum function finds the maximum mark for each subject
# Input: csvLines, list, A list of all the lines in the CSV
# Input: markDict, dict, A dictionary including the Name, Marks, and Total Score for each student
# Return: maxMarks, list, The maximum mark for each subject
def maximum(csvLines, markDict):
    maxMarks = []
    # Find the max mark for each Subject
    for x in range(0, len(csvLines[0])):
        maxX = 0
        for y in range(0, len(csvLines)):
            if (maxX < float(csvLines[y][x])):
                maxX = float(csvLines[y][x])
        maxMarks.append(round(maxX, 4))
    # Find the max mark for "Total"    
    maxTotal = 0
    for id in markDict:
        if (maxTotal < float(markDict[id]["Total"])):
            maxTotal = float(markDict[id]["Total"])
    maxMarks.append(round(maxTotal, 4))
    return maxMarks

# The average function finds the maximum mark for each subject
# Input: csvLines, list, A list of all the lines in the CSV
# Input: markDict, dict, A dictionary including the Name, Marks, and Total Score for each student
# Return: avgMarks, list, The average of the marks for each subject
def average(csvLines, markDict):
    avgMarks = []
    # Calulate the Average for the classes
    for x in range(0, len(csvLines[0])):
        totalX = 0
        for y in range(0, len(csvLines)):
            totalX += float(csvLines[y][x])
        avgX = totalX / float(len(csvLines))
        avgMarks.append(round(avgX, 4))
    total = 0
    # Calculate the avg Total
    for id in markDict:
        total += float(markDict[id]["Total"])
    avgTotal = total / float(len(markDict))
    avgMarks.append(round(avgTotal, 4))
    return avgMarks

# The stdDev function finds the standard deviation of the marks for each subject
# Input: csvLines, list, A list of all the lines in the CSV
# Input: markDict, dict, A dictionary including the Name, Marks, and Total Score for each student
# Return: stdMarks, list, The standard deviation of the marks for each subject
def stdDev(csvLines, markDict):
    stdMarks = []
    # Loop though all the Columns
    for x in range(0, len(csvLines[0])):
        column = []
        # Loop through all the Rows
        for y in range(0, len(csvLines)):
            # Add the score to the list for the Column
            column.append(float(csvLines[y][x]))
        # Call the helperStd function to calculate the Std of the column, and append to the stdMarks list.
        stdMarks.append(round(helperStd(column), 4))
    marks = []
    # Calculate the Std for the total column
    for id in markDict:
        marks.append(float(markDict[id]["Total"]))
    # Call the helperStd function to calculate the Std of the column, and append to the stdMarks list.
    stdMarks.append(round(helperStd(marks), 4))
    return stdMarks


# The spCor function finds the Spearman's Correlation of the marks for each subject
# Input: csvLines, list, A list of all the lines in the CSV
# Input: markDict, dict, A dictionary including the Name, Marks, and Total Score for each student
# Return: spCorrelations, list, The Spearman's Correlation of the marks for each subject
def spCor(markDict, classes):
    spCorrelations = []
    # Calls Helper function to calculate the rank of each student in each class
    calculateRank(markDict, classes)
    # Calls Helper function to calculate the Sum of Differance Squared for each class
    sumOfDifSq = calculateSumOfDifSq(markDict, classes)

    # Calulate the Spearman's Correlation for each subject
    for clas in range(0,len(classes)):
        p = 1 -((6*sumOfDifSq[clas]))/(float(len(markDict))*((float(len(markDict))**2)-1))
        p = round(p,4)
        spCorrelations.append(p)
    spCorrelations.append(1.0)
    return spCorrelations


### END: RETURN FUNCTIONS ###


### START: TESTING SECTION ###

# mn,mx,avg,std,cor = main('sample_student_marks.csv')
# print("mn: ",mn)
# print("mx: ",mx)
# print("avg: ", avg)
# print("std: ",std)
# print("cor: ",cor)