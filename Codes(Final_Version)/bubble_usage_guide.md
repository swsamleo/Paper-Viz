# **[Paper-Viz (Bubble Chart)](https://github.com/swsamleo/Paper-Viz)**  

### *Hi there, this is CRUISE Group👋*

## **🔭Introduction to Paper-Viz (Bubble)**

Paper-Viz (Bubble) is a library for making scientific bubble graphics in Python. It is built based on matplotlib and pandas libraries and its plotting function operate on dataframes. 

Paper-Viz (Bubble) helps you plot elegant and professional bubble chart in an accurate and efficient manner to meet the publications requirements. Additionally,  it provides an easy way to add/delete elements and adjust chart, such as bubble labels. 

## **📕Installation**

Paper-Viz official releases can be installed from `` PyPI ``

~~~ 
pip install paperviz
~~~

### **Dependencies** 

#### *Supported Python Versions*

- python 3.6+

#### *Required Dependencies*

- numpy
- matplotlib
- pandas


## **💪Usage Guide**

### **Basic Bubble Chart**

<img src="https://github.com/swsamleo/Paper-Viz/blob/master/Images/bubble/gdp.jpg" width="500"  alt="Basic bubble Chart"/>

Once you have paperviz installed, you're ready to start an unforgettable plotting journey. You could load and plot your first basic bubble chart as instructed below:

~~~ python
# Import paperviz
from paperviz import bubble

# Create a bubble chart
bubble.bubble_plot(
    file='',
    x_col_name='',
    y_col_name='',
    bubble_col='',
    x_label='',
    y_label='',
    bubble_name='',
    legend_title='',
    output_name='')
~~~


### **Advanced Bubble Chart**

Paper-Viz (Bubble) provides a convenient way to show multiple groups by different color and labels. The category column allow to shows the different group of the bubble plot.

- *Multi-category bubble plot*

<img src="https://github.com/swsamleo/Paper-Viz/blob/master/Images/bubble/gdp_continent.jpg" width="500" alt="Multi-item bubble plot"/>

~~~ python
# Multi-category bubble plot
bubble.bubble_category(
    file='',
    x_col_name='',
    y_col_name='',
    bubble_col='',
    category_col='',
    x_label='',
    y_label='',
    output_name='')

~~~

- *Bubble plot with colormap*

<img src="https://github.com/swsamleo/Paper-Viz/blob/master/Images/bubble/gdp_colormap.jpg" width="560"  alt="Bubble plot with colormap"/>

~~~ python
# Bubble plot with colormap
bubble.bubble_colormap(
    file='',
    x_col_name='',
    y_col_name='',
    bubble_col='',
    x_label='',
    y_label='',
    legend_label='',
    legend_title='',
    output_name='')
~~~


## **👯Parameters**

### **Basic Bubble Chart**
>bubble.bubble_plot(file, x_col_name, y_col_name, bubble_col, x_label,
                    y_label, bubble_name, legend_title,output_name, **kwargs) [[source]](https://github.com/swsamleo/Paper-Viz)

### **Basic Parameters**

| Parameter         | Description                                                         |
|:------------------|:--------------------------------------------------------------------|
|file               |'file_name.file_type'. file type:txt/xlsx/csv, such as 'paperviz.txt'|
|x_col_name         |['x column name']                                                    |
|y_col_name         |['y column name']                                                    |
|bubble_col         |The bubble values column                                             |
|x_label            |'x label name'                                                       |
|y_label            |'x label name'                                                       |
|bubble_name        |The column of each bubble name, show each bubble name in legend label|
|legend_title       |customize legend labels title                                        |
|output_name        |the output file name.                                                |


### **Multi-Category bubble plot**
>bubble.bubble_category(file, x_col_name, y_col_name, bubble_col,
                        x_label, y_label, category_col, output_name, **kwargs) [[source]](https://github.com/swsamleo/Paper-Viz)

| Parameter         | Description                                                         |
|:------------------|:--------------------------------------------------------------------|
|file               |'file_name.file_type'. file type:txt/xlsx/csv, such as 'paperviz.txt'|
|x_col_name         |['x column name']                                                    |
|y_col_name         |['y column name']                                                    |
|bubble_col         |The bubble values column                                             |
|x_label            |'x label name'                                                       |
|y_label            |'x label name'                                                       |
|category_col       |The category column of bubble                                        |
|legend_title       |customize legend labels title                                        |
|output_name        |the output file name.                                                |

### **Bubble plot with colormap**
>bubble.bubble_colormap(file, x_col_name, y_col_name, bubble_col,
                        x_label, y_label, output_name, **kwargs)[[source]](https://github.com/swsamleo/Paper-Viz)


| Parameter         | Description                                                         |
|:------------------|:--------------------------------------------------------------------|
|file               |'file_name.file_type'. file type:txt/xlsx/csv, such as 'paperviz.txt'|
|x_col_name         |['x column name']                                                    |
|y_col_name         |['y column name']                                                    |
|bubble_col         |The bubble values column                                             |
|x_label            |'x label name'                                                       |
|y_label            |'x label name'                                                       |
|output_name        |the output file name.                                                |


### ****kwargs**

Patch properties for the chart drawn have been pre-set according to type of paper, and can be modified based on your requirements.

| Property          | Description                                                            | 
|:------------------|:-----------------------------------------------------------------------| 
|**Plot Setting**                                                                            |
|plotwidth          |int                                                                     | 
|plotheight         |int                                                                     |
|backgrid           |bool. If True, show the backgrid of chart                               |
|isframe            |bool. If True, show the frame of chart                                  |   
|my_font            |the typeface of x, y labels,default:'DejaVu Sans'                       |
|linewidth          |int,the line width of the plot                                          |
|**Gridline Setting**                                                                        |
|gridlinewidth      |int.                                                                    |
|gridline_style     |The default style is '-'                                                |
|gridline_color     |The gridline color, default color is grey                               |
|gridline_alpha     |The default is 0.8                                                      |
|**Title Setting**                                                                           |
|plot_title         |False or 'title_name', if not False, add title for the plot             |
|title_pad          |if the title is not False, modify pad size of title                     |
|title_size         |if the title is not False, modify size of title                         |
|title_loc          |if the title is not False, modify location of title                     |
|**XY Ticks setting**                                                                        |   
|xtrick_fontsize    |int. The fontsize of xtrick                                             |
|ytrick_fontsize    |int. The fontsize of xtrick                                             | 
|**legend setting**                                                                          |
|legend_size        |int. The size of legend font                                            |
|legend_loc         |The legend location,default is 'upper right'                            |
|bubblesize_legend_loc|The second legend location                                            |
|bubbleszie_legend_title|The second legend label title                                       |
|**Bubble Setting**                                                                          |
|bubble_marker      |The marker of the bubble, The default is 'o'                            |
|bubble_scale       |int. The size of bubble, The initial bubble scale is 50                 |                                                    |
|alpha              |int. The initial bubble alpha is 0.8                                    |
|bubble_colors      |list. The list of bubble colors                                         |
|bubble_size        |int. The size of bubble of bubble colormap                              |                                
|bubble_cmap        |color. The colormap color                                               |
|colorbar_labelsize |int. The font size of colormap bar, default is 15                       |


  


