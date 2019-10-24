# -*- coding: utf-8 -*-
"""Confusion_matrix.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1pkDJ2DCExMQlyC-iA0QshMzMvcB9S2eh
"""

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sn
import pandas as pd
import seaborn as sns
import math
from google.colab import drive
drive.mount('/content/gdrive')
path = '/content/gdrive/My Drive/Visualization/Data/'
path_img = '/content/gdrive/My Drive/Visualization/Images/'

# loading and preparing data
cm = np.array([[19,8,1,1,2],
     [12,19,6,4,1],
     [0,11,16,9,5],
     [0,3,15,18,12],
     [1,1,2,14,22]])
cm = cm.astype('int') / cm.sum(axis=1)[:, np.newaxis]
conf_matrix = pd.DataFrame(cm, index=[-2,-1,0,1,2], columns=[-2,-1,0,1,2])

# plot size setting
fig, ax = plt.subplots(figsize = (8,6))

# drawing plot, legend bar and colors
sns.heatmap(conf_matrix, annot=True,annot_kws={"size": 15},cmap="YlGnBu")

# title and size
ax.set_title('Title',fontsize=22,pad = 18)

# x,y label and size
plt.ylabel('True label',fontsize=18)
plt.xlabel('Predicted label',fontsize=18)

# ticks and size setting
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)

# save image as pdf to path folder
# bbox in inches, only the given portion of the figure is saved, figure out the tight bbox of the figure
plt.savefig(path_img+'confusion_matrix1.pdf', bbox_inches='tight')
# showing the image
plt.show()

# loading and preparing data
cm = np.array([[19,8,1,1,2],
     [12,19,6,4,1],
     [0,11,16,9,5],
     [0,3,15,18,12],
     [1,1,2,14,22]])    
conf_matrix = pd.DataFrame(cm, index=[-2,-1,0,1,2], columns=[-2,-1,0,1,2])

# plot size setting
fig, ax = plt.subplots(figsize = (8,6))

# drawing plot, legend bar and colors
sns.heatmap(conf_matrix, annot=True,annot_kws={"size": 15},cmap="Blues")

# title and size
ax.set_title('Title',fontsize=22,pad = 18)

# x,y label and size
plt.ylabel('True label',fontsize=18)
plt.xlabel('Predicted label',fontsize=18)

# ticks and size setting
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)

# save image as pdf to path folder
# bbox in inches, only the given portion of the figure is saved, figure out the tight bbox of the figure
plt.savefig(path_img+'confusion_matrix2.pdf', bbox_inches='tight')
# showing the image
plt.show()

