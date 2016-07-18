import matplotlib.pyplot as plt
import numpy as np

with plt.xkcd():

    fig = plt.figure()
    ax = fig.add_axes((0.1, 0.2, 0.8, 0.7))
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    plt.xticks([])
    plt.yticks([])
    ax.set_ylim([-30, 10])

    data = np.ones(100)
    data[70:] -= np.arange(30)

    plt.annotate(
        'THE DAY I OF MY \nINTERVIEW',
        xy=(70, 1), arrowprops=dict(arrowstyle='->'), xytext=(15, -10))

    plt.plot(data)

    plt.xlabel('time')
    plt.ylabel('my overall confidence in my coding skills')
    fig.text(
        0.5, 0.05,
        '"Being a Python Coder by Atriya Ghosh" ',
        ha='center')

    fig = plt.figure()
    ax = fig.add_axes((0.1, 0.2, 0.8, 0.7))
    ax.bar([-0.125, 1.0 - 0.125], [0, 100], 0.25)
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.set_xticks([0, 1])
    ax.set_xlim([-0.5, 1.5])
    ax.set_ylim([0, 110])
    ax.set_xticklabels(['CONFIRMED BY\nMY SUPERVISOR', 'REFUTED BY\nMY SUPERVISOR'])
    plt.yticks([])

    plt.title("CLAIMS OF SUPER CODING POWERS")

fig.text(
    0.5, 0.05,
    '"Being a Python Coder by Atriya Ghosh"',
    ha='center')


plt.show()
