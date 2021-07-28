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

<img src="https://github.com/swsamleo/Paper-Viz/blob/master/Images/heatmap.jpg" width="500"  alt="Basic heatmap plot"/>

Once you have paperviz installed, you're ready to start an unforgettable plotting journey. You could load and plot your first basic line chart as instructed below:

~~~ python
# Import paperviz
from paperviz import Violin_plot

# Create a Box chart
heatmap.heat(
    file='',
    row_labels='',
    col_labels='',    
    paper_type='')
~~~


## **👯Parameters**

>heatmap.heat(self, file, row_labels, col_labels, paper_type, **kwargs) [[source]](https://github.com/swsamleo/Paper-Viz)

### **Basic Parameters**

| Parameter         | Description                                                         |
|:------------------|:--------------------------------------------------------------------|
|file               |'file_name.file_type'. file type:txt/xlsx/csv, such as 'paperviz.txt'|
|row_labels         |['row column name']                                                  |
|col_labels         |['col column name']                                                  |
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
|xlabel_rotate     |the rotation of x axis labels                                            |
|ylabel_rotate     |the rotation of y axis labels                                            |
|barlabel          |the label of color bar                                                   |
|barlabel_rotate   |the rotation of colorbar labels                                          |
|**heatmap setting**                                                                         |
|cmap              |the color of heatmap                                                     |
|annotate          |True or False, if true, the value will show in the heatmap               |
|colorbar          |True or False, if true, the color bar of heatmap will show               |
|annotate_textsize |the font size of annotation                                              |
|**Saving Setting**                                                                          |
|save_image         |bool. If it is True, save chart                                         |
|savefig_bbox_inches|Bounding box in inches                                                  |
|file_name          |the file name in saving image                                           |


  


