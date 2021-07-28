# **[Paper-Viz (pie chart)](https://github.com/swsamleo/Paper-Viz)**  

### *Hi there, this is CRUISE Group👋*

## **🔭Introduction to Paper-Viz (heatmap)**

Paper-Viz (Pie_plot) is a library for making scientific pie graphics in Python. It is built based on matplotlib and pandas libraries and its plotting function operate on dataframes. 

Paper-Viz (Pie_plot) helps you plot elegant and professional pie plot in an accurate and efficient manner to meet the publications requirements. Additionally,  it provides an easy way to add/delete elements and adjust chart.
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

### **Basic pie Plot**

<img src="https://github.com/swsamleo/Paper-Viz/blob/master/Images/pie_chart_4.jpg" width="500"  alt="Basic pie plot"/>

Once you have paperviz installed, you're ready to start an unforgettable plotting journey. You could load and plot your first basic line chart as instructed below:

~~~ python
# Import paperviz
from paperviz import Pie_plot

# Create a pie chart
Pie_plot.Pie(
    file='',
    value='', 
    label='',
    paper_type='')
~~~

### **Advanced box plot**

Paper-Viz (Violin_plot) provides a convenient way to show category violin plot. 

- *pie_chart_with_outside_annotation*

<img src="https://github.com/swsamleo/Paper-Viz/blob/master/Images/pie_chart.jpg" width="500" alt="pie_chart_with_outside_annotation"/>

~~~ python
# category violin plot
Pie_plot.Pie(
    file='',
    value='', 
    label='',
    info_style='Outside_box',
    donut=True
    paper_type='')

~~~
- *pie_chart_with_changeable_radius_and_fontsize*

<img src="https://github.com/swsamleo/Paper-Viz/blob/master/Images/pie_chart_1.jpg" width="500" alt="pie_chart_with_changeable_radius_and_fontsize"/>

~~~ python
# category violin plot
Pie_plot.Pie(
    file='',
    value='', 
    label='',
    info_style='Change_both',
    paper_type='')

~~~

- *pie_chart_with_label_exploration*

<img src="https://github.com/swsamleo/Paper-Viz/blob/master/Images/pie_chart_2.jpg" width="500" alt="pie_chart_with_label_exploration"/>

~~~ python
# category violin plot
Pie_plot.Pie(
    file='',
    value='', 
    label='',
    info_style='Change_both',
    paper_type='')

~~~

- *multi layer pie chart*

<img src="https://github.com/swsamleo/Paper-Viz/blob/master/Images/pie_chart_3.jpg" width="500" alt="multi layer pie chart"/>

~~~ python
# category violin plot
Pie_plot.Pie(
    file='',
    value=[], 
    label='',
    paper_type='')

~~~

## **👯Parameters**

>Pie_plot.Pie(self, file, value, label, paper_type, **kwargs) [[source]](https://github.com/swsamleo/Paper-Viz)

### **Basic Parameters**

| Parameter         | Description                                                         |
|:------------------|:--------------------------------------------------------------------|
|file               |'file_name.file_type'. file type:txt/xlsx/csv, such as 'paperviz.txt'|
|value              |['value name']                                                       |
|label              |['label name']                                                       |
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
|**Labels setting**                                                                          |   
|labeltext_size     |int. The fontsize of x y label                                          |
|**Legend setting**                                                                          |
|legend_size        |size of legend                                                          |
|legend_loc         |location of legend of labels                                            |
|layer_legend_loc   |location of legend of layers                                            |
|**pie setting**                                                                             |
|linewidth          |the width of each wedge outline                                         |
|edgecolor          |the color of wedge outline                                              |
|radius             |the radius of pie chart                                                 |
|explode            |True or false, if true, some wedge will explore outside, only the single layer can explode |
|explode_value      |when explode is True, the distance of stick out                         |
|explode_label      |when explode is True, the label of stick out                            |
|autopct|the format of value|
|actual_values|True or False, if true, show the actual value of each label|
|pctdistance|the distance of value|
|labeldistance|the distance of label|
|info_style|simple,change_font,change_radius,change_both|
|radius_scale|the scale of radius when info_style has some change in radius|
|fontsize_scale|the scale of font size when info_style has some change in font size|
|label_pos_scale|when the radius change, the label position scale|
|val_pos_scale|when the radius change, the value position scale|
|startangle|the pie chart start angle|
|font_size|the font size of value|
|palette|the color palette of pie chart|
|shadow| True or False, the shadow of pie chart|
|layer_scale| if there are multiple input value, the multi-layer radius scale|
|donut| True or False, if ture, draw donut plot|
|donut_circle |if donut is True, the position and radius of donut white blank|
|**Saving Setting**                                                                          |
|save_image         |bool. If it is True, save chart                                         |
|savefig_bbox_inches|Bounding box in inches                                                  |
|file_name          |the file name in saving image                                           |


  


