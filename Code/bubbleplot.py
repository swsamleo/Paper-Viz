# -*- coding: utf-8 -*-
"""BubblePlot.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nnJNf1Rz-aTBz3uARlJSprFcw5hp53QF
"""

import configparser
from google.colab import drive
# libraries
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import matplotlib.patches as mpatches
drive.mount('/content/gdrive')
pathconf = '/content/gdrive/My Drive/Visualization/parameter.conf'
path = '/content/gdrive/My Drive/Visualization/Data/'
path_img = '/content/gdrive/My Drive/Visualization/Images/'

# create data
x = np.random.rand(40)
y = np.random.rand(40)
z = np.random.rand(40) 
colors = np.random.rand(40)
categories = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1,  1, 1, 1, 1,  2, 2, 2, 2,  2, 2, 2, 2])

"""## Basic bubble plot"""

# plot size setting
fig, ax = plt.subplots(figsize = (8,6), dpi=80)

# drawing Plot
plt.scatter(x, y, s=z*1000, alpha=0.5)

# title and size
ax.set_title('Bubble plot',fontsize=22,pad = 18)

# x,y labels and size
plt.xlabel("X_label",fontsize=12)
plt.ylabel("values",fontsize=12)

# save image as pdf to path folder
# bbox in inches, only the given portion of the figure is saved, figure out the tight bbox of the figure
plt.savefig(path_img+'bubble.pdf', bbox_inches='tight')
# showing the image
plt.show()

"""## Bubble plot with Categorical Colors"""

# background setting
styles = ['darkgrid', 'whitegrid', 'dark', 'white', 'ticks']
sns.set_style(styles[0])

# # color labels setting
# must either be valid as mpl color(s) or as numbers to be mapped to colors
colormap = np.array(["lightcoral", "rosybrown", "brown"])

# plot size setting
fig, ax = plt.subplots(figsize = (8,6), dpi=100)

# drawing plot
plt.scatter(x, y, s=z*500, c=colormap[categories], alpha=0.7, linewidth=0.5)

# add the matching legend
pop_a = mpatches.Patch(color=colormap[0], alpha=0.7, label='Category A')
pop_b = mpatches.Patch(color=colormap[1],alpha=0.7, label='Category B')
pop_c = mpatches.Patch(color=colormap[2], alpha=0.7, label='Category C')

# title and size
ax.set_title('Bubble plot with Categorical Colors',fontsize=16,pad = 18)

# x,y labels and size
plt.xlabel("The X axis", fontsize=14)
plt.ylabel("The Y axis", fontsize=14)

# legend
plt.legend(handles=[pop_a,pop_b, pop_c])

# save image as pdf to path folder
# bbox in inches, only the given portion of the figure is saved, figure out the tight bbox of the figure
plt.savefig(path_img+'bubble_multi.pdf', bbox_inches='tight')
# showing the image
plt.show()

"""## Bubble with Colors Indicating a Continous Value"""

# a color palette guide for seaborn https://seaborn.pydata.org/tutorial/color_palettes.html

#background setting 
styles = ['darkgrid', 'whitegrid', 'dark', 'white', 'ticks']
sns.set_style(styles[0]) 

# plot size setting
fig, ax = plt.subplots(figsize = (8,6), dpi=100)

# map the color with X value, define palette with cmap
# define the edge colors with edgecolors
plt.scatter(x, y, s=400, c=z, cmap="Greens", alpha=0.4, edgecolors="grey")

# adding color map legend
plt.colorbar()

# title and size
ax.set_title('Bubble Plot with Color Map',fontsize=16,pad = 18)

# x,y labels and size
plt.xlabel("The X axis", fontsize=14)
plt.ylabel("The Y axis", fontsize=14)

# save image as pdf to path folder
# bbox in inches, only the given portion of the figure is saved, figure out the tight bbox of the figure
plt.savefig(path_img+'bubblePlotwithColorMap.pdf', bbox_inches='tight')
# display the plot
plt.show()

