# **[Paper-Viz (Area chart)](https://github.com/swsamleo/Paper-Viz)**  

### *Hi there, this is CRUISE Group👋*

## **🔭Introduction to Paper-Viz (area chart)**

Paper-Viz (Area_plot) is a library for making scientific area chart graphics in Python. It is built based on matplotlib and pandas libraries and its plotting function operate on dataframes. 

Paper-Viz (Area_plot) helps you plot elegant and professional area plot in an accurate and efficient manner to meet the publications requirements. Additionally,  it provides an easy way to add/delete elements and adjust chart.
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

### **Basic Violin Plot**

<img src="https://github.com/swsamleo/Paper-Viz/blob/master/Images/Area_chart_2.jpg" width="500"  alt="Basic violin plot"/>

Once you have paperviz installed, you're ready to start an unforgettable plotting journey. You could load and plot your first basic line chart as instructed below:

~~~ python
# Import paperviz
from paperviz import Area_plot

# Create a Box chart
Area_plot.area(
    file='',
    x_col_name='', 
    y_col_name='',
    plot_type='',
    paper_type='')
~~~

Paper-Viz (Area_plot) provides stacked area plot and percentage area plot.

~~~ python
 plot_type='Stack'
 plot_type='percentage'
~~~

### **Advanced box plot**

Paper-Viz (Violin_plot) provides a convenient way to show category violin plot. 

- *Multi-item box plot with annotation*

<img src="https://github.com/swsamleo/Paper-Viz/blob/master/Images/Area_chart_1.jpg" width="500" alt="Stack area plot"/>

~~~ python
# category violin plot
Area_plot.area(
    file='',
    x_col_name='',
    category='Stack'
    paper_type='',
)

~~~
<img src="https://github.com/swsamleo/Paper-Viz/blob/master/Images/Area_chart.jpg" width="500" alt="Stack area plot"/>

## **👯Parameters**

>Area_plot.area(self, file,  x_col_name,  y_col_name, plot_type,paper_type,**kwargs) [[source]](https://github.com/swsamleo/Paper-Viz)

### **Basic Parameters**

| Parameter         | Description                                                         |
|:------------------|:--------------------------------------------------------------------|
|file               |'file_name.file_type'. file type:txt/xlsx/csv, such as 'paperviz.txt'|
|x_col_name         |['x column name']                                                    |
|y_col_name         |['y column name']                                                    |
|plot_type          |type of plot: Stack ,percentage or simple                            |
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
|gridlinewidth      |grid line width                                                         |
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
|ticks             |True or False as options. If it is True, add ticks of x and y axis.      |
|tick_size         |size of tick                                                             |
|tick_direction    |'out', 'inout' and 'in' options.                                         |
|**Legend setting**                                                                          |
|legend_siz        |size of legend                                                           |
|legend_loc        |location of legend                                                       |
|legend_ncol       |the legend columns number                                                |
|**Area setting**                                                                            |
|Stack_colour_set  |stack area chart color palette (the number of y columns <7)              |
|Area_colour_set   |simple area chart color palette (the number of y columns <7)             |
|palette           |if the number of y columns >7, use this color palette                    |
|y_scale           |the extra blank in y axis                                                |
|alpha             |transparency of each area                                                |
|arealinewidth     |in the simple area chart, the boundary width                             |
|sort              |using sort function to handle data                                       |
|**Saving Setting**                                                                          |
|save_image         |bool. If it is True, save chart                                         |
|savefig_bbox_inches|Bounding box in inches                                                  |
|file_name          |the file name in saving image                                           |


  


