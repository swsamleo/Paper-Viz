<img src="https://github.com/swsamleo/Paper-Viz/raw/master/Images/PaperViz2.jpg" alt="Multi-item area chart"/>

# 数据可视化 -- Cruise Group
这些可视化代码展示了Python的Seaborn和Matplotlib的可视化模块。这些代码是由RMIT大学Cruise Group编写。运行本文代码，除了安装 matplotlib 和 seaborn 可视化库外，还需要安装其他的一些辅助可视化库，已在代码部分作标注，具体内容请查看下面文章内容。如果您不想阅读冗长的说明，请随时跳到注释代码中。

## 面积图
##### [点击查看代码](Code/Area.ipynb)
通过对轴和线之间的区域进行着色，面积图不仅强调峰和谷，而且还强调高点和低点的持续时间。 高点持续时间越长，线下面积越大。
- 多面积图
- 分图多面积图

<img src="https://github.com/swsamleo/Paper-Viz/raw/master/Images/area.jpg" width="200" height="160" alt="Multi-item area chart"/>        <img src="https://github.com/swsamleo/Paper-Viz/raw/master/Images/area_grouped.jpg" width="200" height="160" alt="Separate multi-item area chart"/>

## 条形图/柱状图
##### [点击查看代码](Code/Bar.ipynb)
条形图是基于计数或任何给定指标可视化项目的经典方式。
- 单条形图
- 分组多条形图
- 误差条形图
- 堆叠式条形图

<img src="https://github.com/swsamleo/Paper-Viz/raw/master/Images/bar.jpg" width="200" height="160" alt="Single item bar chart"/>        <img src="https://github.com/swsamleo/Paper-Viz/raw/master/Images/bar_grouped.jpg" width="200" height="160" alt="Multi-item grouped bar chart"/>        <img src="https://github.com/swsamleo/Paper-Viz/raw/master/Images/bar_error.jpg" width="200" height="160" alt="Error bar chart with two groups"/>        <img src="https://github.com/swsamleo/Paper-Viz/raw/master/Images/bar_stacked.jpg" width="200" height="160" alt="Stacked bar chart with two groups"/>

## 气泡图
##### [点击查看代码](Code/BubblePlot.ipynb)
气泡图是散点图的一种变体，其中数据点被气泡替换，并且数据的附加维数由气泡的大小表示。就像散点图一样，气泡图也不使用类别轴-水平轴和垂直轴都是值轴。
- 单气泡图
- 带颜色目录的多气泡图
- 带颜色条的气泡图

<img src="https://github.com/swsamleo/Paper-Viz/raw/master/Images/bubble.jpg" width="200" height="160" alt="Single item bubble plot"/>        <img src="https://github.com/swsamleo/Paper-Viz/raw/master/Images/bubble_multi.jpg" width="200" height="160" alt="Multi-item bubble plot with categorical colors"/>        <img src="https://github.com/swsamleo/Paper-Viz/raw/master/Images/bubblePlotwithColorMap.jpg" width="200" height="160" alt="Bubble plot with a color map"/>

## 散点图
##### [点击查看代码](Code/Scatter_plot.ipynb)
散点图是用于研究两个变量之间关系的经典的和基本的图表。 如果数据中有多个组，则可能需要以不同颜色可视化每个组。
- 多颜色散点图
- 带目录颜色多分组散点图
- 带直方图的矩阵图
- 多颜色及标记的矩阵图

<img src="https://github.com/swsamleo/Paper-Viz/raw/master/Images/scatter.jpg" width="200" height="160" alt="Scatter plot with multiple colors"/>        <img src="https://github.com/swsamleo/Paper-Viz/raw/master/Images/scatter_multimarkers.jpg" width="200" height="160" alt="Scatter plot with categorical colours in multi groups"/>        <img src="https://github.com/swsamleo/Paper-Viz/raw/master/Images/scatterandhistogram.jpg" width="200" height="160" alt="Pairwise plot with histogram"/>        <img src="https://github.com/swsamleo/Paper-Viz/raw/master/Images/scatterandhistogram_multimarks.jpg" width="200" height="160" alt="Pairwise plot with categorical colours and marks"/>

## 地图
##### [点击查看代码](Code/MapVizSummary.ipynb)
- 带色条的地图
- 带色条的地图
- 带路径的地图
- 戴路径和指示点的地图
- 填色地图 (红色和黄色)
- 填色地图 (绿色和黄色)
- 带标注和色条的世界地图

<img src="https://github.com/swsamleo/Paper-Viz/raw/master/Images/map_heatmap.png" width="200" height="120" alt="Single item bar chart"/>        <img src="https://github.com/swsamleo/Paper-Viz/raw/master/Images/map_heatmap1.png" width="200" height="120" alt="Multi-item grouped bar chart"/>        <img src="https://github.com/swsamleo/Paper-Viz/raw/master/Images/map_pathmap.png" width="200" height="120" alt="Error bar chart with two groups"/>        <img src="https://github.com/swsamleo/Paper-Viz/raw/master/Images/map_pathandpointmap.png" width="200" height="120" alt="Stacked bar chart with two groups"/>

<img src="https://github.com/swsamleo/Paper-Viz/raw/master/Images/map_area%20filled%20colour%20(red%20and%20yellow).png" width="200" height="120" alt="Single item bar chart"/>        <img src="https://github.com/swsamleo/Paper-Viz/raw/master/Images/map_area%20filled%20colour%20(green%20and%20yellow).png" width="200" height="120" alt="Multi-item grouped bar chart"/>        <img src="https://github.com/swsamleo/Paper-Viz/raw/master/Images/worldmap.png" width="200" height="120" alt="Error bar chart with two groups"/>

## 直方图
##### [点击查看代码](Code/Histogram.ipynb)
直方图是使用不同高度的条形图的数据图形显示。在直方图中，每个条形将数字分组成为范围。高的条表示该范围内有更多数据。直方图表示连续样本数据的形状和分布。
- 带密度曲线的单直方图
- 带密度曲线的多直方图

<img src="https://github.com/swsamleo/Paper-Viz/raw/master/Images/hist1.jpg" width="210" height="170" alt="Single item histogram with a density curve"/>        <img src="https://github.com/swsamleo/Paper-Viz/raw/master/Images/hist2.jpg" width="210" height="170" alt="Multi-item histogram with density curves"/>

## 热力图/热图
##### [点击查看代码](Code/Confusion_matrix.ipynb)
热力图是数据的图形表示，其中矩阵中包含的各个值用颜色表示。
- 蓝色到黄色渐变带标值热力图
- 蓝色渐变带标值热力图

<img src="https://github.com/swsamleo/Paper-Viz/raw/master/Images/confusion_matrix1.jpg" width="210" height="170" alt="Heatmap with values in blue to yellow colours"/>        <img src="https://github.com/swsamleo/Paper-Viz/raw/master/Images/confusion_matrix2.jpg" width="210" height="170" alt="Heatmap with values in blue colours"/>

## 时序图/时间序列图
##### [点击查看代码](Code/Time_Series_Plot.ipynb)
时间序列图用于显示给定度量随时间变化的方式。
- 带最大值、最小值和记事线的时序图
- 带波峰波谷的时序图
- 随线标记图例的多线图
- 时间序列分解图

<img src="https://github.com/swsamleo/Paper-Viz/raw/master/Images/timeseries.jpg" width="200" height="160" alt="Time series plot with maximum, minimum values and event bar"/>        <img src="https://github.com/swsamleo/Paper-Viz/raw/master/Images/timeseries_peaks.jpg" width="200" height="160" alt="Time series plot with peaks and troughs"/>        <img src="https://github.com/swsamleo/Paper-Viz/raw/master/Images/timeseries_multiple.jpg" width="200" height="160" alt="Time series plot with legend marked on lines"/>        <img src="https://github.com/swsamleo/Paper-Viz/raw/master/Images/timeseries_decomposition.jpg" width="160" height="200" alt="Time series decomposition plot"/>

## 线图/折线图/曲线图
##### [点击查看代码](Code/Line.ipynb)
折线图或曲线图是一种将信息表示为一系列数据点（称为“标记”）的图表，这些数据点由直线段连接。它是许多领域中常见的基本图表类型之一。
- 带不同颜色及标记的多线图

<img src="https://github.com/swsamleo/Paper-Viz/raw/master/Images/line.jpg" width="230" height="160" alt="Multi-item line chart with categorical colours and marks"/>

## 饼图
##### [点击查看代码](Code/Pie.ipynb)
饼图是显示组成的经典方式。 然而，现在通常不建议使用它，因为馅饼部分的面积有时会变得误导。 因此，如果您要使用饼图，强烈建议明确记下饼图每个部分的百分比或数字。
- 带百分比值的饼图
- 带百分比值的环状饼图

<img src="https://github.com/swsamleo/Paper-Viz/raw/master/Images/pie1.jpg" width="275" height="160" alt="Pie chart with percentage marked on"/>        <img src="https://github.com/swsamleo/Paper-Viz/raw/master/Images/pie2.jpg" width="270" height="160" alt="Circle chart with percentage marked on"/>

## 金字塔图
##### [点击查看代码](Code/Pyramid.ipynb)
人口金字塔可用于显示由数量排序的组的分布，或者它也可以用于显示人口的逐级过滤。
- 分组人口金字塔图
- 带标值的人口分组金字塔图
- 带渐变色的人口金字塔图
- 带标值的金字塔图

<img src="https://github.com/swsamleo/Paper-Viz/raw/master/Images/pyramid_group.jpg" width="230" height="160" alt="Population pyramid with two groups"/>        <img src="https://github.com/swsamleo/Paper-Viz/raw/master/Images/pyramid_groupvalue.jpg" width="230" height="160" alt="Population pyramid with values marked on"/>        <img src="https://github.com/swsamleo/Paper-Viz/raw/master/Images/pyramid_group2.jpg" width="210" height="160" alt="Pyramid with values marked on"/>

## 箱形图/盒须图/盒式图/箱线图
##### [点击查看代码](Code/Boxplot.ipynb)
箱形图是一种通过四分位数以图形方式描绘数字数据组的方法。图中反应出一组数据的五位数概括。五位数概括指最小值，第一四分位数，中位数，第三四分位数和最大值。
- 多箱型图

<img src="https://github.com/swsamleo/Paper-Viz/raw/master/Images/boxplot.jpg" width="170" height="210" alt="Multi-item box plot"/>

## 雷达图
##### [点击查看代码](Code/Radar.ipynb)
雷达图是一种以二维图的形式显示多元数据的图形方法，该二维图包含三个或多个定量变量，这些变量在从同一点开始的轴上表示。轴的相对位置和角度通常是无用的。
- 分组雷达图

<img src="https://github.com/swsamleo/Paper-Viz/raw/master/Images/radar.jpg" width="195" height="165" alt="Radar chart with two groups"/>

## 小提琴图
##### [点击查看代码](Code/Violin.ipynb)
小提琴图是一种绘制数字数据的方法。它类似于箱形图，在每侧都增加了一个旋转的核密度图。
- 小提琴图
- 带分组的小提琴图

<img src="https://github.com/swsamleo/Paper-Viz/raw/master/Images/violin.jpg" width="210" height="170" alt="Violin plot"/>        <img src="https://github.com/swsamleo/Paper-Viz/raw/master/Images/violin_group.jpg" width="210" height="170" alt="Grouped violin plot"/>
