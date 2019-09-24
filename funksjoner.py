import random 
import numpy as np 



def expectedTransitionTime(initState, endState, timeSteps): 
    if initState==0: 
        prob = 0.05 
    else: prob = 0.2 
    n = np.zeros(timeSteps)
    for i in range(len(n)): 
        xState = initState
        counter = 0
        while(xState==initState): 
            counter += 1                            
            randNum = random.randint(0,100) 
            if randNum < 100*prob:                  
                xState = endState
        n[i] = counter 
    nAve = sum(n)/len(n)
    return nAve
    


def compareToAnalytic(initState, endState, timeSteps):  
    # Returns the percentage of transition times that falls within 1% and 5% error of the   
    # analytic solution when running "expectedTransitionTime" 1000 times 
    if initState==0: 
        analyticResult = 20
    else: analyticResult = 5
    fivePercentCount = 0
    onePercentCount = 0
    nSample = np.zeros(1000)        # Array of average timesteps for this timeSteps
    for j in range(1000):            # Will run the function 1000 times 
        nSample[j] = expectedTransitionTime(initState, endState, timeSteps)
        
        if nSample[j]<= analyticResult*1.05 and nSample[j]>= analyticResult*0.95: 
            fivePercentCount+=1
        if nSample[j]<= analyticResult*1.01 and nSample[j]>= analyticResult*0.99: 
            onePercentCount+=1
            #print('We are in the extremely good area!! ')
    #print('1%: Testing for less then ', analyticResult*1.01, ' and more than ', analyticResult*0.99, '.')
    #print('5%: Testing for less then ', analyticResult*1.05, ' and more than ', analyticResult*0.95, '.')
    return onePercentCount/1000, fivePercentCount/1000






                







