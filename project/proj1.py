## Final Lists ##
mn = []
mx = []
avg = []
std = []
cor = []


def main(csvfile):

    csvLines = readFile(csvfile)
    #print("csvLines: ", csvLines)
    classes = getClasses(csvLines)
    #print("classes: ", classes)
    markDict = createDict(csvLines, classes)
    #print("\nmarkDict: ",markDict)
    rawMarks = createRawMarks(csvLines)
    #print("\nrawMarks: ",rawMarks)
    mn = minimum(rawMarks, markDict)
    print("\nmn: ", mn)
    mx = maximum(rawMarks, markDict)
    print("\nmx: ", mx)
    avg = average(rawMarks, markDict)
    print("\navg: ", avg)
    std = stdDev(rawMarks, markDict)
    print("\nstd: ", std)
    cor = spCor(rawMarks, markDict, classes)
    print("\ncor: ", cor)


def readFile(csvfile):
    f = open(csvfile)
    lines = []
    for line in f:
        s = line.strip().split(',')
        lines.append(s)
    f.close()
    return lines


def getClasses(csvLines):
    classes = csvLines[0]
    del classes[0]
    del classes[0]
    del csvLines[0]
    return classes


def createDict(csvLines, classes):
    lines = csvLines
    markDict = {}

    for line in lines:
        name = line[0]
        del line[0]
        del line[0]
        marks = {}
        total = 0
        for x in range(0, len(line)):
            total += float(line[x])
            marks[classes[x]] = line[x]
        markDict[name] = {
            "Marks": marks,
            "Total": total
        }
    return(markDict)


def createRawMarks(csvLines):
    rawMarks = csvLines
    return rawMarks

# A funtion to find the minimum mark


def minimum(rawMarks, markDict):
    minMarks = []
    for x in range(0, len(rawMarks[0])):
        minX = 100
        for y in range(0, len(rawMarks)):
            if (minX > float(rawMarks[y][x])):
                minX = float(rawMarks[y][x])
        minMarks.append(round(minX, 4))
    minTotal = 1000
    for name in markDict:
        if (minTotal > float(markDict[name]["Total"])):
            minTotal = float(markDict[name]["Total"])
    minMarks.append(round(minTotal, 4))
    return minMarks


def maximum(rawMarks, markDict):
    maxMarks = []
    for x in range(0, len(rawMarks[0])):
        maxX = 0
        for y in range(0, len(rawMarks)):
            if (maxX < float(rawMarks[y][x])):
                maxX = float(rawMarks[y][x])
        maxMarks.append(round(maxX, 4))
    maxTotal = 0
    for name in markDict:
        if (maxTotal < float(markDict[name]["Total"])):
            maxTotal = float(markDict[name]["Total"])
    maxMarks.append(round(maxTotal, 4))
    return maxMarks


def average(rawMarks, markDict):
    avgMarks = []
    for x in range(0, len(rawMarks[0])):
        totalX = 0
        for y in range(0, len(rawMarks)):
            totalX += float(rawMarks[y][x])
        avgX = totalX / float(len(rawMarks))
        avgMarks.append(round(avgX, 4))
    total = 0
    for name in markDict:
        total += float(markDict[name]["Total"])
    avgTotal = total / float(len(markDict))
    avgMarks.append(round(avgTotal, 4))
    return avgMarks


def stdDev(rawMarks, markDict):
    stdMarks = []
    for x in range(0, len(rawMarks[0])):
        column = []
        for y in range(0, len(rawMarks)):
            column.append(float(rawMarks[y][x]))
        stdMarks.append(round(helperStd(column), 4))
    marks = []
    for name in markDict:
        marks.append(float(markDict[name]["Total"]))
    stdMarks.append(round(helperStd(marks), 4))
    return stdMarks


def helperStd(col):
    variance = sum([((num - (sum(col) / len(col))) ** 2)
                    for num in col]) / len(col)
    return float(variance ** 0.5)


def spCor(rawMarks, markDict, classes):
    spCor = []
    calculateRank(markDict, classes)
    sumOfDifSq = calculateSumOfDifSq(markDict, classes)

    for each in range(0,len(classes)):
        p = 1 -((6*sumOfDifSq[each]))/(float(len(markDict))*(float(len(markDict))**2))
        p = round(p,4)
        spCor.append(p)
    spCor.append(1.0)
    return spCor


def calculateRank(markDict, classes):
    for clas in classes:
        X = []
        totals = []
        for name in markDict:
            X.append(float(markDict[name]["Marks"][clas]))
            X.sort(reverse=True)
            totals.append(float(markDict[name]["Total"]))
            totals.sort(reverse=True)
        for name in markDict:
            for each in range(0, len(X)):
                if (float(markDict[name]["Marks"][clas]) == X[each]):
                    clasRank = each + 1
                    markDict[name][clas + "Rank"] = clasRank
                    break
    for name in markDict:
        for each in range(0, len(X)):
            if (float(markDict[name]["Total"]) == totals[each]):
                totalRank = each + 1
                markDict[name]["TotalRank"] = totalRank
                break
                


def calculateSumOfDifSq(markDict, classes):
    sumOfDifSqTotal= []
    for clas in classes:
        sumOfDifSq = 0
        for name in markDict:
            dif = float(markDict[name]["TotalRank"]) - \
                float(markDict[name][clas + "Rank"])
            dif2 = float(dif)*float(dif)
            markDict[name][clas + "Dif2"] = dif2
            sumOfDifSq += dif2
        sumOfDifSqTotal.append(sumOfDifSq)
    return sumOfDifSqTotal


main('project/sample_student_marks.csv')
