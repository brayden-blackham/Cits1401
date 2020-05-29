'''
Written By: Brayden Blackham
Student Number: 22226136
Unit: Cits1401
Project 2: Create a Python 3 Program use Benford's law on a CSV full of numbers.
'''

# The main function is where other functions are called
# Input: filename, str , The name of the CSV File
# Input: no_places, int , The number of places for the analysis
# Input: regularise, boolean , Should the results be a fraction of the total?
# Return: counts, list, A list of counts of digits
def main(filename,no_places,regularise=False):
    csvLines = readFile(filename)
    numbers = createList(csvLines)
    counts = createCounts(numbers,no_places,regularise)

    return counts

# The readFile function opens, reads and closes the file
# Input: csvfile, str , The name of the CSV File
# Return: csvLines, list, A list of all the lines in the CSV
# ERROR: 'File does not exist', The program can't find the file so will gracefully exit.
def readFile(csvfile):
    try:
        f = open(csvfile)
        csvLines = []
        for line in f:
            s = line.strip().split(',')
            csvLines.append(s)
        f.close()
        return csvLines
    except FileNotFoundError:
        print('File does not exist') 
        exit()
    
# The createList function looks though the CSV and
# adds numbers too a list.
# Input: csvLines, list, A list of all the lines in the CSV
# Return: numbers, list, A list of all numbers in the CSV
def createList(csvLines):
    numbers = []
    # loop though lines of csv
    for line in csvLines:
        # Loop though terms in line.
        for number in line:
            # if cell in csv has something in it.
            if number: 
                # if the cell is a number
                if (number[0].isnumeric()):
                    # convert to float first, then to int,then string, then append.
                    # need to convert to float first becasue for deciaml that are strings you cant go straigt to int.
                    # eg. converting from "5.38" to int doesnt work. Need todo "5.38" > 5.38 > 5 (String, Float, Int).
                    # the final is type string is so we can referance there index's later.
                    numbers.append(str(int(float(number))))
    return numbers

# The createCounts function creates a Bedford's Law count.
# Input: numbers, list, A list of all numbers in the CSV
# Input: no_places, int , The number of places for the analysis
# Input: regularise, boolean , Should the results be a fraction of the total?
# Return: counts, list, A list of the counts of digits in either regularised form or not.
def createCounts(numbers,no_places,regularise):
    counts = []
    # Create the list(s) to where the digits will be counted
    for x in range(0,no_places):
        counts.append([0,0,0,0,0,0,0,0,0,0])
    
    totals = []
    # loop though number of places
    for x in range(0,no_places):
        total = 0
        # loop though all the numbers
        for number in numbers:
            # if number is long enough to have x digits
            if x < len(number):
                # Increment count for that digit and total by 1
                counts[x][int(number[x])] += 1
                total = total + 1
        totals.append(total)
    # loop though number of places
    for x in range(0,no_places):
        # moves the zero's too the last place in list.
        zeros = counts[x][0]
        del counts[x][0]
        counts[x].append(zeros)
    # convert to fractions if regularise
    if regularise:
        for x in range(0,no_places):
            for y in range(0,10):
                counts[x][y] = counts[x][y] / totals[x]

    return counts

# output = main("sample_accounts.csv",3)
# print(output)