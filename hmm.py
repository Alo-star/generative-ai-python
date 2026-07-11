# Hidden Markov Model (Hmm)

import matplotlib.pyplot as plt
from hmmlearn import hmm
import numpy as np

# Example from textbooks: Weather / activities
states = ['Rainy', 'Sunny']
observations = ['walk', 'shop', 'clean']

start_prob = np.array([0.6, 0.4])   # P(Rainy), P(Sunny)
trans_prob = np.array([[0.7, 0.3],  # from Rainy -> [Rainy, Sunny]
                       [0.4, 0.6]])  # from Sunny -> [Rainy, Sunny]

emit_prob = {  # emission: state -> {obs:prob}
    'Rainy': {'walk': 0.1, 'shop': 0.4, 'clean': 0.5},
    'Sunny': {'walk': 0.6, 'shop': 0.3, 'clean': 0.1}
}

state_index = {s: i for i, s in enumerate(states)}


def viterbi(obs_seq):
    T = len(obs_seq)
    N = len(states)
    # dp[t, s] = best log-prob of path ending in state s at time t
    dp = np.full((T, N), -np.inf)
    ptr = np.zeros((T, N), dtype=int)

    # init (use log-probs to avoid underflow)
    for s in range(N):
        dp[0, s] = np.log(start_prob[s]) + \
            np.log(emit_prob[states[s]][obs_seq[0]])

    # recursion
    for t in range(1, T):
        for s in range(N):
            emit_log = np.log(emit_prob[states[s]][obs_seq[t]])
            # choose previous state that maximizes dp[t-1, prev] + log(trans[prev, s])
            candidates = dp[t-1, :] + np.log(trans_prob[:, s]) + emit_log
            ptr[t, s] = np.argmax(candidates)
            dp[t, s] = np.max(candidates)

    # termination + backtrack
    best_last = np.argmax(dp[T-1, :])
    best_path = [best_last]
    for t in range(T-1, 0, -1):
        best_last = ptr[t, best_last]
        best_path.append(best_last)
    best_path.reverse()
    # return path and approx prob
    return [states[i] for i in best_path], np.exp(np.max(dp[T-1, :]))


# Test
obs_seq = ['walk', 'shop', 'clean']
path, prob = viterbi(obs_seq)
print("Observations:", obs_seq)
print("Viterbi best path:", path)
print("Path probability (approx):", prob)




# Simulate 2-state Gaussian HMM
np.random.seed(42)
n_components = 2  # hidden states
model = hmm.GaussianHMM(n_components=n_components,
                        covariance_type="full", n_iter=100)

# Manually set parameters and sample
model.startprob_ = np.array([0.6, 0.4])
model.transmat_ = np.array([[0.7, 0.3],
                            [0.4, 0.6]])
# Gaussian means for each hidden state
model.means_ = np.array([[0.0], [3.0]])
model.covars_ = np.array([[[0.5]], [[0.3]]])  # variances

# Sample a sequence
X, Z = model.sample(200)  # X: observations (200x1), Z: hidden states
plt.plot(X, label='observations')
plt.title("Gaussian HMM observations (simulated)")
plt.legend()
plt.show()

# Fit a new model to X (learning)
learn_model = hmm.GaussianHMM(
    n_components=2, covariance_type="full", n_iter=100, random_state=0)
learn_model.fit(X)

print("Learned startprob:", learn_model.startprob_)
print("Learned transmat:\n", learn_model.transmat_)
print("Learned means:", learn_model.means_.ravel())