import scipy.stats as stats
from matplotlib import pyplot as plt
import numpy as np

plt.figure(1, figsize=(12.5, 4))

a = np.arange(16)
lambda_ = [1.5, 4.2]
colors = ["#348ABD", "#A60628"]

plt.bar(a, stats.poisson.pmf(a, lambda_[0]), label="$\lambda = %.1f$" % lambda_[
        0],alpha = 0.6, edgecolor=colors[0], lw="3")
plt.bar(a, stats.poisson.pmf(a, lambda_[1]), label="$\lambda = %.1f$" % lambda_[
        1],alpha = 0.6, lw="3")

plt.xticks(a + 0.4, a)
plt.legend()
plt.xlabel("$k$")
plt.ylabel("Probability of $k$")
plt.title("PMF of a poisson random variable")
plt.show()
