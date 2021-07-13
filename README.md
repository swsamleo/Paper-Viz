<img src="https://github.com/swsamleo/Paper-Viz/blob/master/Images/PaperViz.jpg" alt="PaperViz"/>

# Data Visualisation - CRUISE Group
## Leader Dr Wei Shao
### Team Member Nan Gao, Zhiqiu Chen, Ying Guo, Lanzhou Jiang
## Professional Python graphs for Scientific Papers
These visualisation codes show visualization modules by Seaborn and Matplotlib of Python. The codes were written by Cruise Group of RMIT University. If you want to run the codes, you need to install some other Python libraries in addition to Seaborn and Matplotlib, which have been marked in the codes section. Please refer to the following contents for details. If you're not into reading lenghty explanations at all, feel free to jump right into the commented code.

## Area Chart
##### [Code](Code/Area_class.ipynb)
By coloring the area between the axis and the line, the area map not only emphasizes the peaks and valleys, but also emphasizes the duration of the high and low points. The longer the high point lasts, the larger the area under the line. The stacked area plot can show the total value and item values, the percentage area chart can show the percentage of each item.
- Multi-item area chart
- Stacked area chart
- Percentange area chart

<img src="https://github.com/swsamleo/Paper-Viz/blob/master/Images/Simple_area_chart.png" width="200" height="160" alt="Multi-item area chart"/>        <img src="https://github.com/swsamleo/Paper-Viz/blob/master/Images/Stack_area_plot.png" width="200" height="160" alt="Stacked area chart"/>      <img src="https://github.com/swsamleo/Paper-Viz/blob/master/Images/Percentage_Stacked_Area_Chart.png" width="200" height="160" alt="Precentage area chart"/>

## Bar Chart
##### [Code](Code/Bar.ipynb)
A bar chart is a classic way to visualise items based on counting or any given indicator.
- Single item bar chart
- Multi-item grouped bar chart
- Error bar chart with two groups
- Stacked bar chart with two groups

<img src="https://github.com/swsamleo/Paper-Viz/blob/master/Images/bar.jpg" width="210" height="160" alt="Single item bar chart"/>        <img src="https://github.com/swsamleo/Paper-Viz/blob/master/Images/bar_grouped.jpg" width="210" height="160" alt="Multi-item grouped bar chart"/>        <img src="https://github.com/swsamleo/Paper-Viz/blob/master/Images/bar_error.jpg" width="210" height="160" alt="Error bar chart with two groups"/>        <img src="https://github.com/swsamleo/Paper-Viz/blob/master/Images/bar_stacked.jpg" width="210" height="160" alt="Stacked bar chart with two groups"/>

## Bubble Plot
##### [Code](Code/bubble_class.ipynb)
A bubble chart is a variation of a scatter chart in which the data points are replaced with bubbles, and an additional dimension of the data is represented in the size of the bubbles. Just like a scatter chart, a bubble chart does not use a category axis — both horizontal and vertical axes are value axes.
- Bubble chart with each bubble name and sizes
- Multi-item bubble plot with categorical colors
- Bubble plot with a color map

<img src="https://github.com/swsamleo/Paper-Viz/blob/master/Images/bubble/gdp.jpg" width="230" height="190" alt="Bubble chart with each bubble name and sizes"/>        <img src="https://github.com/swsamleo/Paper-Viz/blob/master/Images/bubble/gdp_continent.jpg" width="230" height="190" alt="Multi-item bubble plot with categorical colors"/>        <img src="https://github.com/swsamleo/Paper-Viz/blob/master/Images/bubble/gdp_colorbar.jpg" width="230" height="190" alt="Bubble plot with a color map"/>

## Scatter Plot
##### [Code](Code/scatter_class.ipynb)
A scatter plot is a basic chart used to study the relationship between two variables. If you have multiple groups in your data, you might want to visualize each group in a different color.
- Single item scatter plot with trend line
- Multi-item scatter plot
- Scatter plot with multi-mark


<img src="https://github.com/swsamleo/Paper-Viz/blob/master/Images/scatter/ice_cream.jpg" width="230" height="190" alt="Single item scatter plot"/>        <img src="https://github.com/swsamleo/Paper-Viz/blob/master/Images/scatter/smoker.jpg" width="230" height="190" alt="Multi-item scatter plot"/>        <img src="https://github.com/swsamleo/Paper-Viz/blob/master/Images/scatter/marker.jpg" width="230" height="190" alt="Scatter plot with multi-mark"/>


## Map
##### [Code](Code/MapVizSummary.ipynb)
- Heatmap with colour bar
- Heatmap with colour bar
- Map with path
- Map with path and point marked
- Map with area filled colour (red and yellow)
- Map with area filled colour (green and yellow)
- World map with area marked and colour bar

<img src="https://github.com/swsamleo/Paper-Viz/blob/master/Images/map_heatmap.png" width="200" height="120" alt="Single item bar chart"/>        <img src="https://github.com/swsamleo/Paper-Viz/blob/master/Images/map_heatmap1.png" width="200" height="120" alt="Multi-item grouped bar chart"/>        <img src="https://github.com/swsamleo/Paper-Viz/blob/master/Images/map_pathmap.png" width="200" height="120" alt="Error bar chart with two groups"/>        <img src="https://github.com/swsamleo/Paper-Viz/blob/master/Images/map_pathandpointmap.png" width="200" height="120" alt="Stacked bar chart with two groups"/>

<img src="https://github.com/swsamleo/Paper-Viz/blob/master/Images/map_area%20filled%20colour%20(red%20and%20yellow).png" width="200" height="120" alt="Single item bar chart"/>        <img src="https://github.com/swsamleo/Paper-Viz/blob/master/Images/map_area%20filled%20colour%20(green%20and%20yellow).png" width="200" height="120" alt="Multi-item grouped bar chart"/>        <img src="https://github.com/swsamleo/Paper-Viz/blob/master/Images/worldmap.png" width="200" height="120" alt="Error bar chart with two groups"/>

## Histogram
##### [Code](Code/histogram_class.ipynb)
A histogram is a graphical display of data using bars of different heights. In a histogram, each bar groups numbers into ranges. Taller bars show that more data falls in that range. A histogram displays the shape and spread of continuous sample data. The height can mean density or actual value.
- Single item histogram with a density curve
- Multi-item histogram which height means actual value
- Stacked histogram

<img src="https://github.com/swsamleo/Paper-Viz/blob/master/Images/single_column_density_histogram.png" width="210" height="170" alt="Single item histogram with a density curve"/>        <img src="https://github.com/swsamleo/Paper-Viz/blob/master/Images/multiple_columns_simple_histogram.png" width="210" height="170" alt="Multi-item histogram"/>    <img src="https://github.com/swsamleo/Paper-Viz/blob/master/Images/stacked_histogram.png" width="210" height="170" alt="Stacked histogram"/>

## Heatmap
##### [Code](Code/heatmap_class.ipynb)
A heatmap is a graphical representation of data where the individual values contained in a matrix are represented as colors.
- Heatmap with values in blue to yellow colours

<img src="https://github.com/swsamleo/Paper-Viz/blob/master/Images/heatmap.png" width="210" height="170" alt="Heatmap with values in blue to yellow colours"/>        

## Time Series Plot
##### [Code](Code/Time_Series_Plot.ipynb)
Time series plots are used to show how a given metric changes over time.
- Time series plot with maximum, minimum values and event bar
- Time series plot with peaks and troughs
- Time series plot with legend marked on lines
- Time series decomposition plot

<img src="https://github.com/swsamleo/Paper-Viz/blob/master/Images/timeseries.jpg" width="200" height="160" alt="Time series plot with maximum, minimum values and event bar"/>        <img src="https://github.com/swsamleo/Paper-Viz/blob/master/Images/timeseries_peaks.jpg" width="200" height="160" alt="Time series plot with peaks and troughs"/>        <img src="https://github.com/swsamleo/Paper-Viz/blob/master/Images/timeseries_multiple.jpg" width="200" height="160" alt="Time series plot with legend marked on lines"/>        <img src="https://github.com/swsamleo/Paper-Viz/blob/master/Images/timeseries_decomposition.jpg" width="160" height="200" alt="Time series decomposition plot"/>

## Line Chart
##### [Code](Code/Line.ipynb)
A line chart or line plot or line graph or curve chart is a type of chart which displays information as a series of data points called 'markers' connected by straight line segments. It is a basic type of chart common in many fields.

- Multi-line chart
- Multi-item line chart with categorical colours and marks
- Double axis line chart
- Insetplot line chart

<img src="https://github.com/swsamleo/Paper-Viz/blob/master/Images/multi-line.png" width="200" height="160" alt="Multi-line chart"/>        <img src="https://github.com/swsamleo/Paper-Viz/blob/master/Images/multiline-different-markers.png" width="200" height="160" alt="Multi-item line chart with categorical colours and marks"/>        <img src="https://github.com/swsamleo/Paper-Viz/blob/master/Images/double_axis_line.png" width="200" height="160" alt="Double axis line chart"/>        <img src="https://github.com/swsamleo/Paper-Viz/blob/master/Images/inset_line_plot.png" width="200" height="160" alt="Insetplot line chart"/>

## Pie Chart
##### [Code](Code/pie_class.ipynb)
A pie chart is the classic way of displaying composition. However, it is generally not recommended now because sometimes the area of the pie would be misleading. Therefore, if you want to use a pie chart, it is highly recommended to explicitly note the percentage or number of each part in the pie chart.
- Pie chart with outside annotation
- Pie chart with percentage marked on and changable radius and font size
- Pie chart with some labels exploration

<img src="https://github.com/swsamleo/Paper-Viz/blob/master/Images/pie_chart_with_outside_annotation.png" width="275" height="250" alt="pie_chart_with_outside_annotation"/>        <img src="https://github.com/swsamleo/Paper-Viz/blob/master/Images/pie_chart_with_changeable_radius_and_fontsize.png" width="270" height="250" alt="pie_chart_with_changeable_radius_and_fontsize"/>     <img src="https://github.com/swsamleo/Paper-Viz/blob/master/Images/pie_chart_with_label_exploration.png" width="270" height="250" alt="pie_chart_with_label_exploration"/>

## Pyramid Chart
##### [Code](Code/pyramid_class.ipynb)
The pyramid can be used to show the distribution of groups sorted by number, or it can be used to show the step-by-step filtering of the population.
- Pyramid with actual value annotation
- Pyramid with sort functions

<img src="https://github.com/swsamleo/Paper-Viz/blob/master/Images/pyramid_with_annotation.png" width="230" height="200" alt="Population pyramid with annotation"/>        <img src="https://github.com/swsamleo/Paper-Viz/blob/master/Images/pyramid_with_sort.png" width="230" height="200" alt="Population pyramid with sort function"/>        

## Box Plot
##### [Code](Code/box_class.ipynb)
A box plot or boxplot is a method for graphically depicting groups of numerical data through their quartiles. Displays the five-number summary of a set of data. The five-number summary is the minimum, first quartile, median, third quartile, and maximum.
- Multi-item box plot
- Multi-item box plot with annotation

<img src="https://github.com/swsamleo/Paper-Viz/blob/master/Images/Multi-item_box_plot.png" width="210" height="210" alt="Multi-item box plot"/>     <img src="https://github.com/swsamleo/Paper-Viz/blob/master/Images/box_plot_with_annotation.png" width="210" height="210" alt="Multi-item box plot with annotation"/>

## Radar Chart
##### [Code](Code/Radar.ipynb)
A radar chart is a graphical method of displaying multivariate data in the form of a two-dimensional chart of three or more quantitative variables represented on axes starting from the same point. The relative position and angle of the axes is typically uninformative.
- Radar chart with two groups

<img src="https://github.com/swsamleo/Paper-Viz/blob/master/Images/radar.jpg" width="195" height="165" alt="Radar chart with two groups"/>

## Violin Plot
##### [Code](Code/violin_class.ipynb)
A violin plot is a method of plotting numeric data. It is similar to a box plot, with the addition of a rotated kernel density plot on each side.
- Violin plot
- category violin plot

<img src="https://github.com/swsamleo/Paper-Viz/blob/master/Images/simple_violin_plot.png" width="210" height="170" alt="Violin plot"/>        <img src="https://github.com/swsamleo/Paper-Viz/blob/master/Images/category_violin_plot.png" width="210" height="170" alt="category violin plot"/>
