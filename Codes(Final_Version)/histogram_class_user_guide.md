# **[Paper-Viz (hist plot)](https://github.com/swsamleo/Paper-Viz)**  

### *Hi there, this is CRUISE Group👋*

## **🔭Introduction to Paper-Viz (Histogram)**

Paper-Viz (hist_plot) is a library for making scientific histogram graphics in Python. It is built based on matplotlib and pandas libraries and its plotting function operate on dataframes. 

Paper-Viz (hist_plot) helps you plot elegant and professional histogram in an accurate and efficient manner to meet the publications requirements. Additionally,  it provides an easy way to add/delete elements and adjust chart.

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

### **Basic histogram Plot**

<img src="https://github.com/swsamleo/Paper-Viz/blob/master/Images/histogram.jpg" width="500"  alt="Basic box plot"/>

Once you have paperviz installed, you're ready to start an unforgettable plotting journey. You could load and plot your first basic chart as instructed below:

~~~ python
# Import paperviz
from paperviz import Box_plot

# Create a box chart
hist_plot.hist(
    file='',
    x_col_name='',    
    paper_type='')
~~~

Paper-Viz (hist_plot) provides Multi-item histogram plot and stacked histogram
~~~ python
 stacked=True
~~~

### **Advanced box plot**

Paper-Viz (hist_plot) provides a convenient way to show mean value and median value. 

- *Multi-item histogram*

<img src="https://github.com/swsamleo/Paper-Viz/blob/master/Images/histogram_1.jpg" width="500" alt="Multi-item histogram plot"/>

~~~ python
# Multi-item histogram
hist_plot.hist(
    file='',
    x_col_name=[],    
    paper_type='')
)

~~~
- *Stack histogram*

<img src="https://github.com/swsamleo/Paper-Viz/blob/master/Images/histogram_2.jpg" width="500" alt="Stack histogram plot"/>

~~~ python
# stack histogram
hist_plot.hist(
    file='',
    x_col_name=[],
    stacked=True
    paper_type='')
)

~~~


## **👯Parameters**

>hist_plot.hist(self, file, x_col_name, paper_type, **kwargs) [[source]](https://github.com/swsamleo/Paper-Viz)

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
|tick_size         |int. the size of x y ticks                                               |
|tick_direction    |set the direction of ticks                                               |
|**Legend setting**                                                                          |
|legend_size       |size of legend                                                           |
|legend_loc        |location of legend                                                       |
|**histogram setting**                                                                       |
|edgecolor         |the color of bins outlines                                               |
|alpha             |the alpha of bins                                                        |
|histtype          |the type of histogram                                                    |
|orientation       |vertical or horizontal                                                   |
|stacked           |True or False, if true, draw stack histogram                             |
|bins              |set the number of bins                                                   |
|density           |True or False, if true, the y axis means the density of each bins        |
|density_line      |True or False, if true, draw the density line of histogram               |
|**Saving Setting**                                                                          |
|save_image         |bool. If it is True, save chart                                         |
|savefig_bbox_inches|Bounding box in inches                                                  |
|file_name          |the file name in saving image                                           |


  


