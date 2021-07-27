# **[Paper-Viz (Scatter Chart)](https://github.com/swsamleo/Paper-Viz)**  

### *Hi there, this is CRUISE Group👋*

## **🔭Introduction to Paper-Viz (Box plot)**

Paper-Viz (Box_plot) is a library for making scientific scatter graphics in Python. It is built based on matplotlib and pandas libraries and its plotting function operate on dataframes. 

Paper-Viz (Scatter) helps you plot elegant and professional scatter chart in an accurate and efficient manner to meet the publications requirements. Additionally,  it provides an easy way to add/delete elements and adjust chart, such as trend lines. 

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
|**Title Setting**                                                                           |
|plot_title         |False or 'title_name', if not False, add title for the plot             |
|title_pad          |if the title is not False, modify pad size of title                     |
|title_size         |if the title is not False, modify size of title                         |
|title_loc          |if the title is not False, modify location of title                     |
|**XY Ticks setting**                                                                        |   
|xtrick_fontsize    |int. The fontsize of xtrick                                             |
|ytrick_fontsize    |int. The fontsize of xtrick                                             | 
|**Y-lim setting**                                                                           |
|ylim_setting       |bool. If True, can adjust the y-lim                                     |
|ylim_buttom        |if y-lim_setting is True, It can adjust the Ylim bottom value           |
|xin_end            |if the inset is True, the inset plot x axis ends from xin_end           |
|yin_start          |if the inset is True, the inset plot y axis starts from yin_start       |
|yin_end            |if the inset is True, the inset plot y axis starts from yin_end         |
|**Scatter Setting**                                                                         |
|ticks              |bool. If True, add ticks of x and y axis.                               |
|scatter_size       |int. The initial scatter size is 100                                                                     |
|alpha              |int. The initial scatter alpha is 0.8                                   |


  


