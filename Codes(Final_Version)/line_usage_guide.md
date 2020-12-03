# **[Paper-Viz (Line Chart)](https://github.com/swsamleo/Paper-Viz)**  

### *Hi there, this is CRUISE Group👋*

## **🔭Introduction to Paper-Viz (Line)**
------------------------------------------

Paper-Viz (Line) is a library for making scientific line graphics in Python. It is built based on matplotlib and pandas libraries and its plotting function operate on dataframes. 

Paper-Viz (Line) helps you plot elegant and professional line chart in an accurate and efficient manner to meet the publications requirements. Additionally,  it provides an easy way to add/delete elements and adjust chart, such as extra lines, double axis, inset plot, markers and legend. 

## **📕Installation**
---------------------

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
---------------------

### **Basic Line Chart**

<img src="https://github.com/swsamleo/Paper-Viz/blob/master/Images/bar.jpg" width="210" height="160" alt="Basic Line Chart"/>

Once you have paperviz installed, you're ready to start an unforgettable plotting journey. You could load and plot your first basic line chart as instructed below:

~~~ python
# Import paperviz
from paperviz import line

# Create a line chart
line.plot(file='', x_col_name=[''], y_col_name=[''], x_label=[''], y_label=[''], legend_label=[''], paper_type='single')
~~~

if you want to draw multiple lines, there is no need to write another line of code, just  simply adjust the code:

~~~ python
 x_col_name=['x1','x2','xn'], y_col_name=['y1','y2','yn'], legend_label=['l1','l2','ln']
~~~

Paper-Viz (Line) provides two types of style: `` 'single' `` and `` 'double' ``, which refer to 'single-column format paper' and 'double-column format paper' respectively. `` 'single' `` is the default style. If you are willing to use `` 'double' `` style, just  simply adjust the code:

~~~ python
 paper_type='double'
~~~

### **Advanced Line Chart**

Paper-Viz (Line) provides a convenient way to add markers, double axis, and inset plot.

- *Line Chart with Markers*

<img src="https://github.com/swsamleo/Paper-Viz/blob/master/Images/bar.jpg" width="210" height="160" alt="Line Chart with Markers"/>

~~~ python
# Create a line chart with markers
line.plot(file='', x_col_name=[''], y_col_name=[''], x_label=[''], y_label=[''], legend_label=[''], paper_type='single', markers=True)
~~~

- *Line Chart with Double Axis*

<img src="https://github.com/swsamleo/Paper-Viz/blob/master/Images/bar.jpg" width="210" height="160" alt="Line Chart with Double Axis"/>

~~~ python
# Create a line chart with double axis
line.plot(file='', x_col_name=[['xl1','xl2'],['xr1','xr2']], y_col_name=[['yl1','yl2'],['yr1','yr2']], x_label=[''], y_label=[''], legend_label=[['l1','l2'],['r1','r2']], paper_type='single', markers=True)
~~~

- *Line Chart with Inset Plot*

<img src="https://github.com/swsamleo/Paper-Viz/blob/master/Images/bar.jpg" width="210" height="160" alt="Line Chart with Inset Plot"/>

~~~ python
# Create a line chart with inset plot
line.plot(file='', x_col_name=[''], y_col_name=[''], x_label=[''], y_label=[''], legend_label=[''], paper_type='single', inset = True, xin_start = , xin_end = , yin_start = , yin_end = )
~~~

## **👯Parameters**
-------------------

>line.plot(file, x_col_name, y_col_name, x_label, y_label, legend_label, paper_type,**kwargs) [[source]](https://github.com/swsamleo/Paper-Viz)

### **Basic Parameters**

| Parameter         | Description                                                         |
|:------------------|:--------------------------------------------------------------------|
|file               |'file_name.file_type'. file type:txt/xlsx/csv, such as 'paperviz.txt'|
|x_col_name         |['x column name']                                                    |
|y_col_name         |['y column name']                                                    |
|x_label            |'x label name'                                                       |
|y_label            |'x label name'                                                       |
|legend_label       |['legend label name']                                                |
|paper_type         |types of paper format, 'single' or 'double'                          |

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
|**Line Setting**                                                                            |
|linewidth          |int                                                                     |  
|gridlinewidth      |if backgrid is True, grid linewidth is the line width of background grid|  
|sa_linecolor       |if paper type is 'single', lines use this palette                       |  
|da_linecolor       |if paper type is 'double', lines use this palette                       |
|linestyle          |{'-',':','-.','--'}                                                     |
|**Label Setting**                                                                           |
|labeltext_size     |int                                                                     |
|labelpad           |pad size of label,int                                                   |
|**Legend Setting**                                                                          |
|legend_size        |int                                                                     |
|legend_loc         |'upper right','lower left','center'                                     |
|ncol               |number of columns of legend,int                                         |
|**Title Setting**                                                                           |
|title              |False or 'title_name', if not False, add title for the plot             |
|title_pad          |if the title is not False, modify pad size of title                     |
|title_size         |if the title is not False, modify size of title                         |
|title_loc          |if the title is not False, modify location of title                     |
|**Markers Setting**                                                                         |   
|markers            |bool. If True, add markers                                              |
|markersize         |if the title is not False, modify size of marker                        |
|markers_shape      |{'o','v','D','X','P','2','p','x','d','4','<','*'}                       |
|**x,y Axis Range**                                                                          |
|xy_lim             |bool. If True, add x and y axis' value range                            |
|x_range            |if the xy_lim is True, set x axis range                                 |
|y_range            |if the xy_lim is True, set y axis range                                 |
|**Inset Plot Setting**                                                                      |
|inset              |bool. If True, add inset plot                                           |
|xin_start          |if the inset is True, the inset plot x axis starts from xin_start       |
|xin_end            |if the inset is True, the inset plot x axis ends from xin_end           |
|yin_start          |if the inset is True, the inset plot y axis starts from yin_start       |
|yin_end            |if the inset is True, the inset plot y axis starts from yin_end         |
|**Ticks Setting**                                                                           |
|ticks              |bool. If True, add ticks of x and y axis.                               |
|tick_size          |int                                                                     |
|tick_direction     |'out', 'inout' and 'in' as options.                                     |
|x_minor_locator    |number of minor ticks in x axis,int                                     |
|y_minor_locator    |number of minor ticks in y axis,int                                     |
|**Others**                                                                                  |
|present_linevalue  |bool. If True, present point value in the line                          |
|double_axis        |bool. If True, add second axis on the right of figure                   |
|save_image         |bool. If True, save chart                                               |
|savefig_bbox_inches|Bounding box in inches,2-tuple, or 4-tuple of floats                    |  
  


