import scipy.stats as stats
from matplotlib import pyplot as plt
import numpy as np

plt.figure(1, figsize=(12.5, 4))

a = np.linspace(0,4,100)
lambda_ = [0.5,1]
colors = ["#348ABD", "#A60628"]


for l,color in zip(lambda_,colors):
    plt.plot(a, stats.expon.pdf(a,scale = 1./l), color = color, label="$\lambda = %.1f$" % l)
    plt.fill_between(a,stats.expon.pdf(a,scale = 1./l),color = color, alpha = .33)

plt.legend()
plt.xlabel("$z$")
plt.ylabel("Probability of $z$")
plt.title("PDF of a exponential random variable")
plt.show()
