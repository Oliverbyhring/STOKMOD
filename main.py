import numpy as np

import funksjoner as func

a = func.expectedTransitionTime(0,1, 1000)
b = func.expectedTransitionTime(1,2, 1000)

print(a,b)


#percentages_01 = func.compareToAnalytic(0,1,1000)
#percentages_12 = func.compareToAnalytic(1,2,1000) 

#print(percentages_01, percentages_12)


# Checking for timesteps: 1000, 10 000, 100 000 
timeSteps = [100000] 
onePercentages_01 = [0,0,0] 
fivePercentages_01 = [0,0,0] 
onePercentages_12 = [0,0,0]
fivePercentages_12 = [0,0,0]

for ii in range(len(timeSteps)): 
    onePercentages_01[ii], fivePercentages_01[ii] = func.compareToAnalytic(0,1,timeSteps[ii])
    onePercentages_12[ii], fivePercentages_12[ii] = func.compareToAnalytic(1,2,timeSteps[ii])
    print('0-1: For timesteps = ', timeSteps[ii], ' we have ', onePercentages_01 , ' in the 1 perc interval')
    print('0-1: For timesteps = ', timeSteps[ii], ' we have ', fivePercentages_01 , ' in the 5 perc interval')
    print('1-2: For timesteps = ', timeSteps[ii], ' we have ', onePercentages_12 , ' in the 1 perc interval')
    print('1-2: For timesteps = ', timeSteps[ii], ' we have ', fivePercentages_12 , ' in the 5 perc interval')





