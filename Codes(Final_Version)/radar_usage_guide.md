# **[Paper-Viz (Radar Chart)](https://github.com/swsamleo/Paper-Viz)**  

### *Hi there, this is CRUISE Group👋*

## **🔭Introduction to Paper-Viz (Radar)**

Paper-Viz (Radar) is a library for making scientific radar graphics in Python. It is built based on matplotlib and pandas libraries and its plotting function operate on dataframes. 

Paper-Viz (Radar) helps you plot elegant and professional radar chart in an accurate and efficient manner to meet the publications requirements. Additionally,  it provides an easy way to add/delete elements and adjust chart, such as overlay. 

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

### **Basic Radar Chart**

<img src="https://github.com/swsamleo/Paper-Viz/blob/master/Images/radar/football.jpg" width="500"  alt="Basic radar Chart"/>

Once you have paperviz installed, you're ready to start an unforgettable plotting journey. You could load and plot your first basic line chart as instructed below:

~~~ python
# Import paperviz
from paperviz import radar

# Create a radar chart
radar.radar_plot(file='',
              index_col='',
              category_col=[],
              y_col_list=[],
              y_lim=(,),
              output_name=)
~~~


### **Advanced Radar Chart**

Paper-Viz (radar) provides a convenient way to show multiple groups by different color and labels. The category column allow to shows the different group of the radar plot.
The user only need to add the column in catgory_col list,y_col_list and it will work.
- *Radar chart with selected overlay*
<img src="https://github.com/swsamleo/Paper-Viz/blob/master/Images/radar/car.jpg" width="500" alt="Radar chart with selected overlay"/>

Paper-Viz (Radar) provides overlay of the radar plot: No overlay of the plot is the default style. If you are willing to use overlay, just  simply adjust the code:

~~~ python
 overlay= True
~~~

  

- *Spider chart with selected overlay*

<img src="https://github.com/swsamleo/Paper-Viz/blob/master/Images/radar/sick.jpg" width="560"  alt="Spider chart with selected overlay"/>

~~~ python
# Spider chart with selected overlay
radar.spider_plot(file='',
               index_col='',
               category_col=[],
               y_col_list=[],
               y_lim=(,),
               output_name='')
~~~


## **👯Parameters**

### **Basic Radar Chart**
>radar.radar_plot(file, index_col, category_col, y_col_list, y_lim,output_name,
                   **kwargs) [[source]](https://github.com/swsamleo/Paper-Viz)

### **Basic Parameters**

| Parameter         | Description                                                         |
|:------------------|:--------------------------------------------------------------------|
|file               |'file_name.file_type'. file type:txt/xlsx/csv, such as 'paperviz.txt'|
|index_col          |The index column. Normally it should be the name of the content      |
|category_col       |input list of attributes for the radar plot                          | 
|y_lim              |The Y lim value                                                      |
|output_name        |the output file name.                                                |


### **Basic Spider Chart**

>radar.spider_plot(file, index_col, category_col, y_col_list, y_lim,output_name,
                   **kwargs) [[source]](https://github.com/swsamleo/Paper-Viz)

| Parameter         | Description                                                         |
|:------------------|:--------------------------------------------------------------------|
|file               |'file_name.file_type'. file type:txt/xlsx/csv, such as 'paperviz.txt'|
|index_col          |The index column. Normally it should be the name of the content      |
|category_col       |input list of attributes for the radar plot                          | 
|y_lim              |The Y lim value                                                      |
|output_name        |the output file name.                                                |


### ****kwargs**

Patch properties for the chart drawn have been pre-set according to type of paper, and can be modified based on your requirements.

| Property          | Description                                                            | 
|:------------------|:-----------------------------------------------------------------------| 
|**Plot Setting**                                                                            |
|figsize            |tuple. The size of plot. The initial setting is (6,4)                   |  
|my_font            |the typeface of x, y labels,default:'DejaVu Sans'                       |
|**Title Setting**                                                                           |
|plot_title         |False or 'title_name', if not False, add title for the plot             |
|title_pad          |if the title is not False, modify pad size of title                     |
|title_size         |if the title is not False, modify size of title                         |
|title_loc          |if the title is not False, modify location of title                     |
|**XY Ticks setting**                                                                        |   
|xtrick_fontsize    |int. The fontsize of xtrick                                             |
|ytrick_fontsize    |int. The fontsize of xtrick                                             |
|ytick_color        |color. The y-tick color                                                 |
|xtick_color        |color. The x-tick color                                                 | 
|**Legend setting**                                                                          |
|legendbox_loc      |tuple. The location of legend. The default is (1.1,1.0)                 |



  


