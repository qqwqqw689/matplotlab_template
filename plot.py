import matplotlib.pyplot as plt
from matplotlib import axes

def get_standard_ax(fig, rect, xlabel="x", ylabel="y", xlim=None, ylim=None, xticks=None, yticks=None):

    ax = fig.add_subplot(rect, axes_class = axes.Axes)

    ax.set_xlabel(xlabel)
    ax.set_label(ylabel)

    if xlim is not None:
        ax.set_xlim(xlim)
    if ylim is not None:
        ax.set_ylim(ylim)

    if xticks is not None:
        ax.set_xticks(xticks)
    if yticks is not None:
        ax.set_yticks(yticks)

    return ax

import numpy as np

def f(x):
    return np.sinc(x)

def main():
    xlim = (-10, 10)
    xticks = np.arange(-10, 10, 1)

    fig = plt.figure()
    ax = get_standard_ax(fig, 111, xlabel="x", ylabel="y", xlim=xlim, xticks=xticks)

    ax.grid()

    x =  np.arange(-10, 10, 0.00001)
    ax.plot(x, f(x))

    plt.show()

if __name__ == "__main__":
    main()
