# **[Paper-Viz (Violin plot)](https://github.com/swsamleo/Paper-Viz)**  

### *Hi there, this is CRUISE Group👋*

## **🔭Introduction to Paper-Viz (Violin plot)**

Paper-Viz (Violin_plot) is a library for making scientific scatter graphics in Python. It is built based on matplotlib and pandas libraries and its plotting function operate on dataframes. 

Paper-Viz (Violin_plot) helps you plot elegant and professional scatter chart in an accurate and efficient manner to meet the publications requirements. Additionally,  it provides an easy way to add/delete elements and adjust chart, such as trend lines. 

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
- seaborn


## **💪Usage Guide**

### **Basic Box Plot**

<img src="https://github.com/swsamleo/Paper-Viz/blob/master/Images/box_plot.jpg" width="500"  alt="Basic box plot"/>

Once you have paperviz installed, you're ready to start an unforgettable plotting journey. You could load and plot your first basic line chart as instructed below:

~~~ python
# Import paperviz
from paperviz import Box_plot

# Create a scatter chart
Box_plot.box(
    file='',
    x_col_name='',    
    paper_type='')
~~~

Paper-Viz (Box_plot) provides Multi-item box plot: No annotation or mean line of the plot is the default style. If you are willing to use annotation or mean line , just simply adjust the code:

~~~ python
 actual_value= True
 showmeans=True
~~~

### **Advanced box plot**

Paper-Viz (Box_plot) provides a convenient way to show mean value and median value. 

- *Multi-item box plot with annotation*

<img src="https://github.com/swsamleo/Paper-Viz/blob/master/Images/box_plot_1.jpg" width="500" alt="Multi-item scatter plot"/>

~~~ python
# Multi-item scatter plot
Box_plot.box(
    file='',
    x_col_name='',
    showmeans=True,
    actual_value=True,
    paper_type='',
)

~~~


## **👯Parameters**

>Box_plot.box(self, file, x_col_name, paper_type, **kwargs) [[source]](https://github.com/swsamleo/Paper-Viz)

### **Basic Parameters**

| Parameter         | Description                                                         |
|:------------------|:--------------------------------------------------------------------|
|file               |'file_name.file_type'. file type:txt/xlsx/csv, such as 'paperviz.txt'|
|x_col_name         |['x column name']                                                    |
|paper_type         |'single' or 'double'                                                 |


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
|gridlinewidth      |grid line width
|**Title Setting**                                                                           |
|title              |None or 'title_name', if not None, add title for the plot               |
|title_pad          |if the title is not None, modify pad size of title                      |
|title_size         |if the title is not None, modify size of title                          |
|title_loc          |if the title is not None, modify location of title                      |
|**XY Labels setting**                                                                       |   
|labeltext_size    |int. The fontsize of x y label                                           |
|x_label           |content of xlabel                                                        | 
|y_label           |content of ylabel                                                        | 
|tick_size         |int. the size of x y ticks
|**Boxes setting**                                                                           |
|width              |the width of each box                                                   |
|palette            |the color palette of box plot                                           |
|notch              |True or false, if true, add notch to each box                           |
|vert               |True or False, If True , makes the boxes vertical.                      |
|showfliers         |True or False, if true, show the outliers beyond the caps               |
|showcaps           |True or False, if true, show the caps on the ends of whiskers           |
|patch_artist       |True or False, if true, boxes and drawn with Patch artists              |
|box_linestyle      |The style of box outline                                                |
|box_linewidth      |The line width of box outlines                                          |
|medianline_color   |The color or median line color                                          |
|showmeans          |True or False, if true, show the median line                            |
|meanline_color     |The color or mean line color                                            |
|meanline_style     |The line style of mean line                                             |
|markers_shape      |The shape of outliers                                                   |
|actual_value       |True or False, if true show the actual value of mean or meadian         |
|**Saving Setting**                                                                          |
|save_image         |bool. If it is True, save chart                                         |
|savefig_bbox_inches|Bounding box in inches                                                  |
|file_name          |the file name in saving image                                           |


  


