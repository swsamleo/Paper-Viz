<img src="https://github.com/swsamleo/Paper-Viz/raw/master/Images/PaperViz.jpg" alt="PaperViz"/>

# Data Visualisation - CRUISE Group
Leader Dr Wei Shao

Team Member Nan Gao, Zhiqiu Chen, Ying Guo, Lanzhou Jiang, Junwei Ye, Haoran Ma, Zhengyuan Xu, Ziyan Peng
## Professional Python graphs for Scientific Papers
These visualisation codes show visualization modules by Seaborn and Matplotlib of Python. The codes were written by Cruise Group of RMIT University. Please refer to the following contents for details. If you're not into reading lenghty explanations at all, feel free to jump right into the commented code.
# Dependencies
If you want to run the codes, you need to install some other Python libraries in addition to Seaborn and Matplotlib, which have been marked in the codes section.
# Install
The latest stable release (and required dependencies) can be installed from PyPI:

    pip install paperviz

You may instead want to use the development version from Github:

    pip install git+https://github.com/swsamleo/Paper-Viz.git
Paper-Viz is also available from Anaconda and can be installed with conda:

    conda install paperviz
# Development
Paper-Viz development takes place on Github: https://github.com/swsamleo/Paper-Viz
# Documentation 
### [Area Chart](https://github.com/swsamleo/Paper-Viz/blob/master/paperviz/area/area.py)
By coloring the area between the axis and the line, the area map not only emphasizes the peaks and valleys, but also emphasizes the duration of the high and low points. The longer the high point lasts, the larger the area under the line. The stacked area plot can show the total value and item values, the percentage area chart can show the percentage of each item.
- Multi-item area chart
- Stacked area chart
- Percentange area chart
```    
from paperviz.area.area import Area
area_model = Area()
area_model.area(
    file="Example_Date\\Area\\numseunm_visitors.csv"
    x_col_name=['index'],
    y_col_name=['Acila_Adobe','Firehose_Museum','Chinese_American_Museum','America_Tropical_Interpretive_Center'],
    x_lable='Index',
    y_lable='vistors number',
    paper_type='double',
    plot_type='Stack',
    title='Number of vistors in four museums',
    save_image=True,
    file_name='Area chart'
)
```

<img src="https://github.com/swsamleo/Paper-Viz/raw/master/Images/Area_chart_2.jpg" width="200" height="160" alt="Multi-item area chart"/>        <img src="https://github.com/swsamleo/Paper-Viz/raw/master/Images/Area_chart_1.jpg" width="200" height="160" alt="Stacked area chart"/>      <img src="https://github.com/swsamleo/Paper-Viz/raw/master/Images/Area_chart.jpg" width="200" height="160" alt="Precentage area chart"/>

### [Bar Chart](https://github.com/swsamleo/Paper-Viz/blob/master/paperviz/bar/bar.py)
A bar chart is a classic way to visualise items based on counting or any given indicator.
- Single item bar chart
- Multi-item grouped bar chart
- Error bar chart with two groups
- Stacked bar chart with two groups

<img src="https://github.com/swsamleo/Paper-Viz/raw/master/Images/bar.jpg" width="210" height="160" alt="Single item bar chart"/>        <img src="https://github.com/swsamleo/Paper-Viz/raw/master/Images/bar_grouped.jpg" width="210" height="160" alt="Multi-item grouped bar chart"/>        <img src="https://github.com/swsamleo/Paper-Viz/raw/master/Images/bar_error.jpg" width="210" height="160" alt="Error bar chart with two groups"/>        <img src="https://github.com/swsamleo/Paper-Viz/raw/master/Images/bar_stacked.jpg" width="210" height="160" alt="Stacked bar chart with two groups"/>

### [Bubble Plot](https://github.com/swsamleo/Paper-Viz/blob/master/paperviz/bubble/bubble.py)
A bubble chart is a variation of a scatter chart in which the data points are replaced with bubbles, and an additional dimension of the data is represented in the size of the bubbles. Just like a scatter chart, a bubble chart does not use a category axis — both horizontal and vertical axes are value axes.
- Bubble chart with each bubble name and sizes
- Multi-item bubble plot with categorical colors
- Bubble plot with a color map

<img src="https://github.com/swsamleo/Paper-Viz/raw/master/Images/bubble/gdp.jpg" width="240" height="190" alt="Bubble chart with each bubble name and sizes"/>        <img src="https://github.com/swsamleo/Paper-Viz/raw/master/Images/bubble/gdp_continent.jpg" width="240" height="190" alt="Multi-item bubble plot with categorical colors"/>        <img src="https://github.com/swsamleo/Paper-Viz/raw/master/Images/bubble/gdp_colorbar.jpg" width="240" height="190" alt="Bubble plot with a color map"/>

### [Scatter Plot](https://github.com/swsamleo/Paper-Viz/blob/master/paperviz/scatter/scatter.py)
A scatter plot is a basic chart used to study the relationship between two variables. If you have multiple groups in your data, you might want to visualize each group in a different color.
- Single item scatter plot with trend line
- Multi-item scatter plot
- Scatter plot with multi-mark


<img src="https://github.com/swsamleo/Paper-Viz/raw/master/Images/scatter/ice_cream.jpg" width="240" height="190" alt="Single item scatter plot"/>        <img src="https://github.com/swsamleo/Paper-Viz/raw/master/Images/scatter/smoker.jpg" width="240" height="190" alt="Multi-item scatter plot"/>        <img src="https://github.com/swsamleo/Paper-Viz/raw/master/Images/scatter/marker.jpg" width="240" height="190" alt="Scatter plot with multi-mark"/>


### [Map](https://github.com/swsamleo/Paper-Viz/blob/master/paperviz/map/map.py)
Maps have been used for a long time to help people navigate on road journeys or comprehend the closeness of one site to another. The material on maps, as well as the maps themselves, have become digitized, interactive, and more attractive as they have been integrated into data analysis and reporting. Seeing location data mapped and integrated in visualizations has increased comprehension and provided a useful, fresh context for more people.

- Point Map
- KDE(Kernel density estimation) Map
- Point and KDE(Kernel density estimation) Map
- Sankey Map
- Choropleth Map
- Route Map

<img src="https://github.com/swsamleo/Paper-Viz/raw/master/Images/map/point.jpg" width="260" height="160" alt="Point Map"/>        <img src="https://github.com/swsamleo/Paper-Viz/raw/master/Images/map/kde.jpg" width="260" height="160" alt="KDE(Kernel density estimation) Map"/>        <img src="https://github.com/swsamleo/Paper-Viz/raw/master/Images/map/point+kde.jpg" width="260" height="160" alt="Point and KDE(Kernel density estimation) Map"/>        <img src="https://github.com/swsamleo/Paper-Viz/raw/master/Images/map/sankey.jpg" width="260" height="160" alt="Sankey Map"/>
        <img src="https://github.com/swsamleo/Paper-Viz/raw/master/Images/map/choropleth.jpg" width="260" height="160" alt="Choropleth Map"/>        <img src="https://github.com/swsamleo/Paper-Viz/raw/master/Images/map/multiple_path.jpg" width="260" height="160" alt="Route Map"/>

### [Histogram](https://github.com/swsamleo/Paper-Viz/blob/master/paperviz/histogram/histogram.py)
A histogram is a graphical display of data using bars of different heights. In a histogram, each bar groups numbers into ranges. Taller bars show that more data falls in that range. A histogram displays the shape and spread of continuous sample data. The height can mean density or actual value.
- Single item histogram with a density curve
- Multi-item histogram which height means actual value
- Stacked histogram

<img src="https://github.com/swsamleo/Paper-Viz/raw/master/Images/histogram.jpg" width="210" height="170" alt="Single item histogram with a density curve"/>        <img src="https://github.com/swsamleo/Paper-Viz/raw/master/Images/histogram_1.jpg" width="210" height="170" alt="Multi-item histogram"/>    <img src="https://github.com/swsamleo/Paper-Viz/raw/master/Images/histogram_2.jpg" width="210" height="170" alt="Stacked histogram"/>

### [Heatmap](https://github.com/swsamleo/Paper-Viz/blob/master/paperviz/heatmap/heatmap.py)
A heatmap is a graphical representation of data where the individual values contained in a matrix are represented as colors.
- Heatmap with values in blue to yellow colours

<img src="https://github.com/swsamleo/Paper-Viz/raw/master/Images/heatmap.jpg" width="210" height="170" alt="Heatmap with values in blue to yellow colours"/>        

### [Time Series Plot](https://github.com/swsamleo/Paper-Viz/blob/master/paperviz/time_series/time_series.py)
Time series plots are used to show how a given metric changes over time.
- Time series plot with maximum, minimum values
- Time series plot with peaks and troughs
- Time series plot with multivariables
- Time series plot with multiple plots
- Time series plot with regional zoom-in

<img src="https://github.com/swsamleo/Paper-Viz/raw/master/Images/Time_series/ts_max.png" width="200" height="160" alt="Time series plot with maximum, minimum values"/>        <img src="https://github.com/swsamleo/Paper-Viz/raw/master/Images/Time_series/ts_peaks" width="200" height="160" alt="Time series plot with peaks and troughs"/>        <img src="https://github.com/swsamleo/Paper-Viz/raw/master/Images/Time_series/ts_multivariable.png" width="200" height="160" alt="Time series plot with multivariables"/>        <img src="https://github.com/swsamleo/Paper-Viz/raw/master/Images/Time_series/ts_multiple_plot.png" width="160" height="200" alt="Time series with multiple plots"/> <img src="https://github.com/swsamleo/Paper-Viz/raw/master/Images/Time_series/ts_zoomin.png" width="300" height="200" alt="Time series plot with regional zoom-in"/>

### [Line Chart](https://github.com/swsamleo/Paper-Viz/blob/master/paperviz/line/line.py)
A line chart or line plot or line graph or curve chart is a type of chart which displays information as a series of data points called 'markers' connected by straight line segments. It is a basic type of chart common in many fields.

- Multi-line chart
- Multi-item line chart with categorical colours and marks
- Double axis line chart
- Insetplot line chart

<img src="https://github.com/swsamleo/Paper-Viz/raw/master/Images/multi-line.png" width="200" height="160" alt="Multi-line chart"/>        <img src="https://github.com/swsamleo/Paper-Viz/raw/master/Images/multiline-different-markers.png" width="200" height="160" alt="Multi-item line chart with categorical colours and marks"/>        <img src="https://github.com/swsamleo/Paper-Viz/raw/master/Images/double_axis_line.png" width="200" height="160" alt="Double axis line chart"/>        <img src="https://github.com/swsamleo/Paper-Viz/raw/master/Images/inset_line_plot.png" width="200" height="160" alt="Insetplot line chart"/>

### [Pie Chart](https://github.com/swsamleo/Paper-Viz/blob/master/paperviz/pie/pie.py)
A pie chart is the classic way of displaying composition. However, it is generally not recommended now because sometimes the area of the pie would be misleading. Therefore, if you want to use a pie chart, it is highly recommended to explicitly note the percentage or number of each part in the pie chart.
- Pie chart with outside annotation
- Pie chart with percentage marked on and changable radius and font size
- Pie chart with some labels exploration
- Multi-layer pie chart

<img src="https://github.com/swsamleo/Paper-Viz/raw/master/Images/pie_chart.jpg" width="320" height="290" alt="pie_chart_with_outside_annotation"/>        <img src="https://github.com/swsamleo/Paper-Viz/raw/master/Images/pie_chart_1.jpg" width="320" height="290" alt="pie_chart_with_changeable_radius_and_fontsize"/>         <img src="https://github.com/swsamleo/Paper-Viz/raw/master/Images/pie_chart_2.jpg" width="290" height="290" alt="pie_chart_with_label_exploration"/>     <img src="https://github.com/swsamleo/Paper-Viz/raw/master/Images/pie_chart_3.jpg" width="290" height="290" alt="multi layer pie chart"/>


### [Pyramid Chart](https://github.com/swsamleo/Paper-Viz/blob/master/paperviz/pyramid/pyramid.py)
The pyramid can be used to show the distribution of groups sorted by number, or it can be used to show the step-by-step filtering of the population.
- Pyramid with actual value annotation
- Pyramid with sort functions

<img src="https://github.com/swsamleo/Paper-Viz/raw/master/Images/pyramid.jpg" width="230" height="200" alt="Population pyramid with annotation"/>        <img src="https://github.com/swsamleo/Paper-Viz/raw/master/Images/pyramid_1.jpg" width="230" height="200" alt="Population pyramid with sort function"/>        

### [Box Plot](https://github.com/swsamleo/Paper-Viz/blob/master/paperviz/box/box.py)
A box plot or boxplot is a method for graphically depicting groups of numerical data through their quartiles. Displays the five-number summary of a set of data. The five-number summary is the minimum, first quartile, median, third quartile, and maximum.
- Multi-item box plot
- Multi-item box plot with annotation

<img src="https://github.com/swsamleo/Paper-Viz/raw/master/Images/box_plot.jpg" width="210" height="210" alt="Multi-item box plot"/>     <img src="https://github.com/swsamleo/Paper-Viz/raw/master/Images/box_plot_1.jpg" width="210" height="210" alt="Multi-item box plot with annotation"/>

### [Radar Chart](https://github.com/swsamleo/Paper-Viz/blob/master/paperviz/radar/radar.py)
A radar chart is a graphical method of displaying multivariate data in the form of a two-dimensional chart of three or more quantitative variables represented on axes starting from the same point. The relative position and angle of the axes is typically uninformative.
- Radar chart with single groups
- Radar chart with multiple groups
- Spider chart with multiple groups

<img src="https://github.com/swsamleo/Paper-Viz/raw/master/Images/radar/football.jpg" width="260" height="180" alt="Radar chart with single groups"/>  <img src="https://github.com/swsamleo/Paper-Viz/raw/master/Images/radar/car.jpg" width="260" height="180" alt="Radar chart with multiple groups"/>  <img src="https://github.com/swsamleo/Paper-Viz/raw/master/Images/radar/sick.jpg" width="260" height="180" alt="Spider chart with multiple groups"/>

### [Violin Plot](https://github.com/swsamleo/Paper-Viz/blob/master/paperviz/violin/violin.py)
A violin plot is a method of plotting numeric data. It is similar to a box plot, with the addition of a rotated kernel density plot on each side.
- Violin plot
- category violin plot

<img src="https://github.com/swsamleo/Paper-Viz/raw/master/Images/violin_plot.jpg" width="210" height="170" alt="Violin plot"/>        <img src="https://github.com/swsamleo/Paper-Viz/raw/master/Images/violin_plot_1.jpg" width="210" height="170" alt="category violin plot"/>
