# **[Paper-Viz (Map Chart)](https://github.com/swsamleo/Paper-Viz)**  

### *Hi there, this is CRUISE Group👋*

## **🔭Introduction to Paper-Viz (Map)**

Paper-Viz (Map) is a library for making scientific map graphics in Python. It is built based on geoplot and geopandas libraries and its plotting function operate on geopanads dataframes. 

Paper-Viz (Map) helps you plot elegant and professional map chart in an accurate and efficient manner to meet the publications requirements. Additionally,  it provides an easy way to plot mutiple map plots. 

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

### **Basic map Chart**

<img src="https://github.com/swsamleo/Paper-Viz/blob/master/Images/map/point.jpg" width="500"  alt="Basic map Chart"/>

Once you have paperviz installed, you're ready to start an unforgettable plotting journey. You could load and plot your first basic map plot as instructed below:

~~~ python
# Import paperviz
from paperviz import map

# Create a scatter chart
scatterm4.map_plot(base_file='',
                   output_name='')
~~~

Paper-Viz (Map) provides overlay file of the map plot: point(scatter) style is the default style. If you are willing to use different overlay style like Kernel density estimation, just simply adjust the code:

~~~ python
 overlay_type= 'kde'
~~~
<img src="https://github.com/swsamleo/Paper-Viz/blob/master/Images/map/kde.jpg" width="500"  alt="kde map Chart"/>

### **Advanced Map Chart**

Paper-Viz (Map) provides a convenient way to show the combine of the kde and point plot:

- *Multi-item map plot*

<img src="https://github.com/swsamleo/Paper-Viz/blob/master/Images/map/point+kde.jpg" width="500" alt="combine of the kde and point plot"/>

~~~ python
# Combine of the kde and point plot
map.map_plot(base_file='',
         overlay_file='',
         overlay_type='both',
         output_name='')
)

~~~

- *choropleth map*

<img src="https://github.com/swsamleo/Paper-Viz/blob/master/Images/map/choropleth.jpg" width="560"  alt="choropleth map"/>

~~~ python
# map plot with multi-marker
map.map_plot(base_file='',
            overlay_file='',
            overlay_type='choropleth',
            choropleth_hue='', 
            output_name='')
~~~

- *sankey map*

<img src="https://github.com/swsamleo/Paper-Viz/blob/master/Images/map/sankey.jpg" width="560"  alt="sankey map"/>

~~~ python
# map plot with multi-marker
map.map_plot(base_file='', 
            sankey_plot=True,
            sankey_scale='', 
            output_name='')
~~~

- *multiple-path map*

<img src="https://github.com/swsamleo/Paper-Viz/blob/master/Images/map/multiple-path.png" width="560"  alt="multiple-path map"/>

~~~ python
# map plot with multi-marker
map.route_map(file='',
            latitude='',
            longtitude='')
~~~

## **👯Parameters**

>map.(base_file, overlay_file, overlay_type, output_name, **kwargs) [[source]](https://github.com/swsamleo/Paper-Viz)

### **Basic Parameters**

| Parameter         | Description                                                         |
|:------------------|:--------------------------------------------------------------------|
|base_file          |The file name of base file, it need to conatin ploygons              |
|overlay_file       |The file with overlay data                                           |
|overlay_type       |It can select the different map plot. The default is 'point'         |
|output_name        |the output file name.                                                |

### ****kwargs**

Patch properties for the chart drawn have been pre-set according to type of paper, and can be modified based on your requirements.

| Property          | Description                                                            | 
|:------------------|:-----------------------------------------------------------------------| 
|**Plot Setting**                                                                            |
|plotwidth          |int                                                                     | 
|plot_titile        |string. The default is empty                                            |
|title_fontsize     |int. The fontsize of the title                                          |
|**File Setting**                                                                            |
|file_longtitude    |string. The column name of the longtitude                               | 
|file_latitude      |string. The column name of the latitude                                 |
|**Polyplot(base plot) Setting**                                                             |
|polyplot_linewidth |int. The line width of the base map                                     |
|polyploy_facecolor |color. The color of the base map                                        |
|polyplot_figsize   |tuple. The size of the base map                                         |
|**KDE(Kernel density estimatio) map setting**                                               |   
|kde_cmap           |color. The color of the kde overlap                                     |
|kde_shade          |bool. The kde shadow                                                    | 
|kde_shade_lowest   |bool. The kde shadow to lowest                                          |
|kde_alpha          |int. The alpha of kde overlay                                           | 
|**Point plot setting**                                                                      |
|pointplot_edgecolor|color. The edge color of the point(scatter)                             |
|pointplot_linewidth|int. The line width of the point(scatter)                               |
|pointplot_alpha    |int. The alpha of the point(scatter                                     |
|pointplot_legend   |bool. The legend appear or not                                          |
|**Choropleth Setting**                                                                      |
|choropleth_figsize |tuple. The figsize of the choropleth                                    |
|choropleth_legend  |bool. The legend appear or not                                          |
|choropleth_hue     |string. The column name of category                                     |
|choropleth_cmap    |color. The choropleth map color bar color                               |
|**Sankey Setting**                                                                          |
|sankey_limits      |tuple. The limit of the sankey overlay                                  |
|sankey_color       |color. The color of the sankey(line)                                    |
|sankey_figsize     |tuple. The figsize of the sankey plot                                   |
|sankey_plot        |bool. If yes, the plot type will be transform to sankey plot            |
|sankey_scale       |string. The column name of the sankey scale(size of the column)         |
|**Cartogram Setting**                                                                       |
|cartogram_scale    |string. The column name of the cartogram scale(size of the column)      |
|cartogram_legend   |bool. The legend appear or not                                          |
|cartogram_cmap     |color. The color of cartogram                                           |
|cartogram_hue      |string. The column name of the cartogram scale(color of the column)     |
|cartogram_num_legend|int. The number of color category                                      |
|**Path Setting**                                                                            |
|path_scale    |string. The column name of the Path scale(size of the column)                |
|path_legend   |bool. The legend appear or not                                               |
|path_cmap     |color. The color of Path                                                     |
|path_hue      |string. The column name of the Path scale(color of the column)               |
|path_num_legend|int. The number of color category                                           |

### **Route map Parameters**
>map.route_map(file, longtitude,latitude, **kwargs)[[source]](https://github.com/swsamleo/Paper-Viz)

| Parameter         | Description                                                                |
|:------------------|:---------------------------------------------------------------------------|
|file               |The file name of route_map file, it need to conatain longtitude and latitude|
|longtitude         |The column name of longtitude                                               |
|latitude           |The column name of latitude                                               |


  
### ****kwargs**

Patch properties for the chart drawn have been pre-set according to type of paper, and can be modified based on your requirements.

| Property          | Description                                                            | 
|:------------------|:-----------------------------------------------------------------------|
|**File Setting**                                                                            |
|file_longtitude    |string. The column name of the longtitude                               | 
|file_latitude      |string. The column name of the latitude                                 |
|**Map Setting**                                                                             |
|map_location       |list. [latitude,longtitude]                                             |
|map_zoom           |int. The zoom setting of the map                                        |
|icon_color         |color. The icon color                                                   |
|icon_style         |The style of the icon. The default if 'plus'                            |
|line_color         |color. The color of the path line                                       |


