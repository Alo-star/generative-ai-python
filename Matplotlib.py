from matplotlib.lines import lineStyles
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
Overs = ['1','2','3','4','5','6']
Runs =[15,10,25,20,30,40]
bowlers = ['alok','abir','agink','sumit','rahil','kumar']

plt.plot(Overs,Runs,color = 'r',linestyle='--',marker='o')
plt.plot(Overs,bowlers,color = 'b',linestyle='-',marker='o')
plt.xlabel('overs')
plt.ylabel('bowlers - Runs')
plt.title('Cricket data Analysis')
plt.grid(True)
plt.show()


