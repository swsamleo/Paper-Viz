from scatter import Scatter
s1=Scatter(path='Example_Data\Scatter\\',path_img='Images\\')
s1.scatter_plot(
    file='ice_cream.xlsx',
    x_col_name='Ice Cream Sales',
    y_col_name='Temperature',
    x_label='Ice Cream Sales',
    y_label='Temperature °C',
    trend_line=True,
    scatter_size=100,
    output_name='ice_cream.jpg')