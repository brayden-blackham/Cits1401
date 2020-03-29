## A function to convert a binary to a Decimal.
## Input: b, a string of arbitary length containing binary.
## Return: int, the deci of the binary b.


def binToDeci(b):
    print("")

    deci = 0
    for x in range(len(b)):
        deci += int(b[x]) * (2** (len(b)-x-1))

    print('Deci: ',deci)
    print("")

    

binToDeci('10011010')

