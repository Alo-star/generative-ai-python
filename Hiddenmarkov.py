import pandas as pd
import numpy as np
from hmmlearn import hmm
import matplotlib.pyplot as plt


# Load dataset
df = pd.read_excel("New Superstore Data.xlsx")

# Convert order date to datetime
df["Order Date"] = pd.to_datetime(df["Order Date"])

# Aggregate daily profit
daily_profit = df.groupby("Order Date")["Profit"].sum().reset_index()
daily_profit = daily_profit.sort_values("Order Date")

# HMM requires 2D input → reshape
X = daily_profit["Profit"].values.reshape(-1, 1)

# We assume 2 hidden states:
# State 0 → Low-profit condition
# State 1 → High-profit condition
model = hmm.GaussianHMM(
    n_components=2,
    covariance_type="full",
    n_iter=200,
    random_state=42
)

# Train model
model.fit(X)

# Predict hidden states
hidden_states = model.predict(X)

daily_profit["HiddenState"] = hidden_states

# Model parameters
print("Mean profit per state:")
print(model.means_)

print("\nVariance per state:")
print(model.covars_)

# Visualization
plt.figure(figsize=(12,5))

plt.plot(
    daily_profit["Order Date"],
    daily_profit["Profit"],
    label="Daily Profit"
)

# Color by hidden state
colors = ['red' if s == 0 else 'green' for s in hidden_states]

plt.scatter(
    daily_profit["Order Date"],
    daily_profit["Profit"],
    c=colors
)

plt.title("Hidden Markov States on Daily Profit (Superstore)")
plt.xlabel("Date")
plt.ylabel("Profit")
plt.legend()
plt.show()