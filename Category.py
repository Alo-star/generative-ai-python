import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
categories= ['Housing','Cultural','Transport','Entertainment','Sports']
alice_expenses = [1200, 300, 300, 200, 150]
bob_expenses = [1100, 120, 350, 180, 140]
carol_expenses = [1300, 280, 420, 220, 150]

x = np.arange(len(categories))
bar_width = 0.2

plt.bar(x - bar_width, alice_expenses, width=bar_width, label='Alice')
plt.bar(x, bob_expenses, width=bar_width, label='Bob')
plt.bar(x + bar_width, carol_expenses, width=bar_width, label='Carol')

plt.xlabel('Expense Categories')
plt.ylabel('Monthly Expenses')
plt.title('Monthly expenses for Alice, Bob, and Carol')
plt.xticks(x, categories)
plt.legend()
plt.show()