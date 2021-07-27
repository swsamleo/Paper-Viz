# **[Paper-Viz (Time-series)](https://github.com/swsamleo/Paper-Viz)**  

### *Hi there, this is CRUISE Group👋*

## **🔭Introduction to Paper-Viz (Time-series)**

The time-series data visualization class is created based on matplotlib. This class provides
single plot or multiple plots of dataset variables over a time interval. Currenly supports
marking and annotating minimum/maximum points, and annual peak/trough points, as well as
zooming-in a specified region of a plot.

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

### **Time-series with Max/Min annotation**

<img src="https://github.com/swsamleo/Paper-Viz/blob/master/Images/Time_series/ts_max.jpg" width="500"/>

Once you have paperviz installed, you're ready to start an unforgettable plotting journey. You could load and plot your first basic ts chart as instructed below:

~~~ python
# Import paperviz
from paperviz import time_series as ts
# create a TimeSeries instance for reading input data
ts = TimeSeries(file)
# Create a time-seies plot with annotation of min/max
ts.plot(x_col_name='Month',
        y_col_name=['Monthly beer production'], 
        start_time='1974',
        end_time='1988',
        xlabel='Date',
        ylabel=['Beer production'],
        date_fmt='%Y-%m',
        show_min=True,
        min_annotate=True,
        show_max=True,
        max_annotate=True)
~~~

### **Time-series with peaks/troughs annotation**

<img src="https://github.com/swsamleo/Paper-Viz/blob/master/Images/Time_series/ts_peaks.pdf" width="500"/>

~~~ python
# Create a time_series plot with annotation of annual peaks/troughs
ts.plot(x_col_name='Month',
        y_col_name=['#Passengers'],
        xlabel='Date',
        ylabel=['Air Passengers'],
        end_time='1960', 
        date_fmt='%Y-%m',
        figsize=(9, 6),
        show_peaks=True,
        show_troughs=True,
        peak_annotate=True,
        trough_annotate=True)
~~~

- *Time-series for more than one variable*

<img src="https://github.com/swsamleo/Paper-Viz/blob/master/Images/Time_series/ts_multivariable.pdf" width="560" />

~~~ python
# Create a time-series plot using two variables
ts.plot(x_col_name='date',
        y_col_name=['mdeaths', 'fdeaths'],
        xlabel='Date',
        ylabel=['Deaths'],
        legend=['Male', 'Female'])
~~~

- *Time-series for multiple plot*

<img src="https://github.com/swsamleo/Paper-Viz/blob/master/Images/Time_series/ts_multiple_plot.pdf" width="560" />

~~~ python
# Create a time-series plot using two variables
ts.plot(x_col_name='date',
        y_col_name=['mdeaths', 'fdeaths'],
        xlabel='Date',
        ylabel=['male', 'Female'],
        multiple_plot=True)
~~~

## **👯Parameters**

>TimeSeries.plot(x_col_name, y_col_name, start_time, end_time, **kwargs) [[source]](https://github.com/swsamleo/Paper-Viz)

### **Basic Parameters**

| Parameter         | Description                                                         |
|:------------------|:--------------------------------------------------------------------|
|file               |'file_name.file_type'. file type:txt/xlsx/csv, such as 'paperviz.txt'|
|x_col_name         |['x column name']                                                    |
|y_col_name         |['y column name']                                                    |
|start_time         |'start date of the timeline'                                         |
|end_time           |'end date of the timeline'                                           |

### ****kwargs**

Patch properties for the chart drawn have been pre-set according to type of paper, and can be modified based on your requirements.

| Property          | Description                                                            | 
|:------------------|:-----------------------------------------------------------------------| 
**Plot Setting**                                                                            
|figsize            |tuple                                                                   | 
|backgrid           |bool. If True, show the backgrid of plot                                |   
|my_font            |the typeface of x, y labels,default:'DejaVu Sans'                       |
|color              |list of color for each plot                                             |
|legend             |list of legend for each lot                                             |
|show_max           |bool. If True, mark the maximum point                                   |
|show_min           |bool. If True, mark the minimum point                                   |
|max_annotate       |bool. If Ture, annotate the maximum point                               |
|min_annotate       |bool. If True, annotate the minimum point                               |
|show_peaks         |bool. If True, mark annual peaks                                        |
|show_troughs       |bool. If True, mark annual troughs                                      |
|peak_annotate      |bool. If True, annotate the peaks                                       |
|trough_annotate    |bool. If True, annotate the troughs                                     |
|precision          |int. length of decimal digits for number annotation                     |
**Label setting**
|xlabel             |str                                                                     |
|xlabel_size        |default 15                                                              |
|ylabel             |list of str                                                             |
|ylabel_size        |default 15                                                              |
|peak_label         |default 'Annual Peaks'                                                  |
|peak_size          |default 10                                                              |
|trough_label       |default 'Annual Troughs'                                                |
|trough_size        |default 10                                                              |
**Grid Setting**
|grid_width         |default 0.5                                                             |
|grid_alpha         |default 0.5                                                             |                                   
**Title Setting**                                                                           
|title              |False or 'title_name', if not False, add title for the plot             |
|title_size         |if the title is not False, modify size of title                         |
**Ticks Setting**                                                                            |
|xtick_rotate       |angle of xtick rotation, default 0                                      |
|xtick_size         |size of xtick label                                                     |
|ytick_rotate       |angle fo xtick rotation, default 0                                      |
|ytick_size         |size of ytick label                                                     |
**Axes Setting**
|ylim_bot           |lower bound of y axis                                                   |
|ylim_top           |upper boud of x axis                                                    |
**Marker Setting**
|peak_marker        |default '^'                                                             |
|trough_marker      |default '^'                                                             |
|**Others**                                                                                  |
|zoom_in            |bool. If True, allow enlargin specified area of plot                    |
|zoom_scale         |int. Level of zoom-in scale                                             |
|zoom_loc           |str. Location of zoomed subplot                                         |
|x_start            |left x coordinate of zooming area for each plot                         |
|x_end              |right x coordinate of zooming area for each plot                        |
|y_start            |bottom y coordinate of zooming area for each plot                       |
|y_end              |top y coordinate of zooming area for each plot                          |
|save_fig           |bool. If True, enable local save of plot                                |
|fig_path           |the path for saving the figure                                          |