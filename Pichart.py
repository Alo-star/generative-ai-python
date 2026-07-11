import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
categories = ['Housing','Cultural','Transport','Entertainment','Sports']
expenses = [1200,400,300,200,250]

# create a pichart
plt.pie(expenses,labels=categories,autopct='%1.1f%%')

# add a title
plt.title('Monthly Expenses by Category')

# display the plot
plt.show()