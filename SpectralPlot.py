import numpy as np
import matplotlib.pyplot as plt
import math
'''
plt.subplot(2, 2, 1)
plt.plotfile('longestShift_1.asc', delimiter=' ', cols=(0, 1),
             names=('wavelength', 'counts'), marker='o')
plt.subplot(2, 2, 2)
plt.plotfile('longestShift_2.asc', delimiter=' ', cols=(0, 1),
             names=('wavelength', 'counts'), marker='o',newfig=False)
plt.plotfile('longestShift_3.asc', delimiter=' ', cols=(0, 1),
             names=('wavelength', 'counts'), marker='o')
plt.plotfile('longestShift_4.asc', delimiter=' ', cols=(0, 1),
             names=('wavelength', 'counts'), marker='o')
plt.plotfile('longestShift_5.asc', delimiter=' ', cols=(0, 1),
             names=('wavelength', 'counts'), marker='o')
plt.show()
'''

def plot_file(ax, fnme, cols=[], label=None):
    data = np.genfromtxt(
      fnme,
      skip_header=0,
      skip_footer=0,
      names=[str(col) for col in cols],
    )
    ax.plot(*[data[str(col)] for col in cols], label=label)

fig = plt.figure(figsize=(10, 3))
fig.text(
    0.5, 0.05,
    '"Raman Fiber Laser Spectrum at Different Coupling Efficiencies" ',
    ha='center')
PLOT_INDEXES = range(1,5)
nrows=2.0
for i in PLOT_INDEXES:
    ax = plt.subplot(nrows, math.ceil(len(PLOT_INDEXES)/nrows), i)
    file='longestShift_'+str(i+1)+'.asc'
    plot_file(ax, file, cols=[0, 1], label=str(i))
plt.show()