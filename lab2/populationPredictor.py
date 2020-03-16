## the initial number of organisms, n
n = 170
## the rate of growth (a real number greater than 0), r
r = 0.8
## the number of hours it takes to achieve this rate, h
h = 5
## the number of hours during which the population grows, t
t = 20

def populationPredictor(number, rate, period, time):
    return number * (rate)**(time/period)
    

pop = populationPredictor(n,r,h,t)
print ('Number of Predicted organisms is :', pop)