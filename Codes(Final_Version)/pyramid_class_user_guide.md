# **[Paper-Viz (pyramid)](https://github.com/swsamleo/Paper-Viz)**  

### *Hi there, this is CRUISE Group👋*

## **🔭Introduction to Paper-Viz (pyramid)**

Paper-Viz (pyramid) is a library for making scientific pyramid graphics in Python. It is built based on matplotlib and pandas libraries and its plotting function operate on dataframes. 

Paper-Viz (pyramid) helps you plot elegant and professional pyramid in an accurate and efficient manner to meet the publications requirements. Additionally,  it provides an easy way to add/delete elements and adjust chart.

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

<img src="https://github.com/swsamleo/Paper-Viz/blob/master/Images/pyramid_1.jpg" width="500"  alt="Basic pyramid plot"/>

Once you have paperviz installed, you're ready to start an unforgettable plotting journey. You could load and plot your first basic chart as instructed below:

~~~ python
# Import paperviz
from paperviz import pyramid

# Create a pyramid chart
pyramid.pyramid(
    file='',
    x_col_name='',
    y_col_name='',
    group_col='',
    paper_type='')
~~~

Paper-Viz (pyramid) provides pyramid with annotation or sort function
~~~ python
 annotate=True
 sort=True
~~~

### **Advanced box plot**

Paper-Viz (hist_plot) provides a convenient way to show mean value and median value. 

- *annotation histogram*

<img src="https://github.com/swsamleo/Paper-Viz/blob/master/Images/pyramid.jpg" width="500" alt="annotation histogram plot"/>

~~~ python
# Multi-item histogram
pyramid.pyramid(
    file='',
    x_col_name='',
    y_col_name='',
    group_col='',
    annotate=True
    paper_type='')
)

~~~
- *sorted pyramid*

<img src="https://github.com/swsamleo/Paper-Viz/blob/master/Images/pyramid_1.jpg" width="500" alt="Stack histogram plot"/>

~~~ python
# stack histogram
pyramid.pyramid(
    file='',
    x_col_name='',
    y_col_name='',
    group_col='',
    sort=True
    paper_type='')
)

~~~


## **👯Parameters**

>pyramid.pyramid(self,file,x_col_name,y_col_name,group_col,paper_type ,**kwargs) [[source]](https://github.com/swsamleo/Paper-Viz)

### **Basic Parameters**

| Parameter         | Description                                                         |
|:------------------|:--------------------------------------------------------------------|
|file               |'file_name.file_type'. file type:txt/xlsx/csv, such as 'paperviz.txt'|
|x_col_name         |['x column name']                                                    |
|y_col_name         |['y column name']                                                    |
|group_col          |['group column name']                                                |
|paper_type         |'single' or 'double'                                                 |


### ****kwargs**

Patch properties for the chart drawn have been pre-set according to type of paper, and can be modified based on your requirements.

| Property          | Description                                                            | 
|:------------------|:-----------------------------------------------------------------------| 
|**Plot Setting**                                                                            |
|plotwidth          |int                                                                     | 
|plotheight         |int                                                                     |
|my_font            |the typeface of x, y labels,default:'DejaVu Sans'                       |
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
|xlabel_rotate     |the rotation of x axis labels                                            |
|ylabel_rotate     |the rotation of y axis labels                                            |
|**Legend setting**                                                                          |
|legend_textsize   |size of legend                                                           |
|legend_loc        |location of legend                                                       |
|**pyramid setting**                                                                         |
|color             |the colors of pyramid                                                    |
|axis_scale        |get more blank in x,y axis                                               |
|sort              |True or False, if true, sort the value in ascending order                |
|annotate_textsize |the font size of annotation                                              |
|x_pos_parameter   |get the relative x position of annotation                                |
|y_pos_parameter   |get the relative y position of annotation                                |
|**Saving Setting**                                                                          |
|save_image         |bool. If it is True, save chart                                         |
|savefig_bbox_inches|Bounding box in inches                                                  |
|file_name          |the file name in saving image                                           |


  


