import random 
import numpy as np 
import matplotlib.pyplot as plt



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


def markovChainSimulation(population, recoverProb, endTime): 
    susceptible = np.zeros(endTime+1)
    infested = np.zeros(endTime+1)
    recovered = np.zeros(endTime+1)
    susceptible[0] = population-50
    infested[0] = 50
    gamma = recoverProb
    timeList = np.arange(0,endTime+1)
    for i in range (1,endTime+1):
        beta = 0.5 * infested[i-1] / population
        newInfested = np.random.binomial(susceptible[i-1],beta)
        newRecovered = np.random.binomial(infested[i-1],gamma)
        susceptible[i] = susceptible[i-1]-newInfested
        infested[i] = infested[i-1]+newInfested-newRecovered
        recovered[i] = recovered[i-1]+newRecovered
    return timeList, susceptible, infested, recovered

def plotIllness(List1,List2,List3,List4):
    plt.figure()
    plt.plot(List1,List2,'y-', label = 'Susceptible')
    plt.plot(List1,List3,'r-', label = 'Infested')
    plt.plot(List1,List4,'g-', label = 'Recovered')
    plt.legend()
    plt.xlabel('Time, T')
    plt.ylabel('People, #')
    plt.show()
