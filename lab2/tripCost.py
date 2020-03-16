# The price of fuel per liter
ppl = 1.36
# The distance driven in KM
km = 173
# The economy of the car L/100km
econ = 12.85


def tripCost(price,distance,economy):
    cost = price * distance/100 * economy
    return cost

cost = tripCost(ppl,km,econ)
print('\nThe ',km,' trip cost $',cost,'\n')
