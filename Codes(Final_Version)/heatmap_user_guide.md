# **[Paper-Viz (heatmap)](https://github.com/swsamleo/Paper-Viz)**  

### *Hi there, this is CRUISE Group👋*

## **🔭Introduction to Paper-Viz (heatmap)**

Paper-Viz (heatmap) is a library for making scientific heatmap graphics in Python. It is built based on matplotlib and pandas libraries and its plotting function operate on dataframes. 

Paper-Viz (heatmap) helps you plot elegant and professional heatmap plot in an accurate and efficient manner to meet the publications requirements. Additionally,  it provides an easy way to add/delete elements and adjust chart.
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

### **Basic heatmap Plot**

<img src="https://github.com/swsamleo/Paper-Viz/blob/master/Images/violin_plot_1.jpg" width="500"  alt="Basic violin plot"/>

Once you have paperviz installed, you're ready to start an unforgettable plotting journey. You could load and plot your first basic line chart as instructed below:

~~~ python
# Import paperviz
from paperviz import Violin_plot

# Create a Box chart
Violin_plot.Violin(
    file='',
    x_col_name='',    
    paper_type='')
~~~

Paper-Viz (Violin_plot) provides Multi-item violin plot: No annotation or mean line of the plot is the default style. If you are willing to use annotation or mean line , just simply adjust the code:

~~~ python
 category=''
~~~

### **Advanced box plot**

Paper-Viz (Violin_plot) provides a convenient way to show category violin plot. 

- *Multi-item box plot with annotation*

<img src="https://github.com/swsamleo/Paper-Viz/blob/master/Images/violin_plot.jpg" width="500" alt="category violin plot"/>

~~~ python
# category violin plot
Violin_plot.Violin(
    file='',
    x_col_name='',
    category=''
    paper_type='',
)

~~~


## **👯Parameters**

>Violin_plot.Violin(self, file, x_col_name, paper_type, **kwargs) [[source]](https://github.com/swsamleo/Paper-Viz)

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
|**Legend setting**                                                                          |
|legend_size       |size of legend                                                           |
|legend_loc        |location of legend                                                       |
|**Violin setting**                                                                          |
|width              |the width of each box                                                   |
|palette            |the color palette of box plot                                           |
|vert               |True or False, If True , makes the boxes vertical.                      |
|showextra          |True or False, if true, show the extra line                             |
|quantiles          |Show the quantiles line                                                 |
|medianline_color   |The color or median line color                                          |
|showmeans          |True or False, if true, show the median line                            |
|category           |Category columns of violin plot                                         |
|x_scale            |Extra blank in x axis                                                   |
|**Saving Setting**                                                                          |
|save_image         |bool. If it is True, save chart                                         |
|savefig_bbox_inches|Bounding box in inches                                                  |
|file_name          |the file name in saving image                                           |


  


