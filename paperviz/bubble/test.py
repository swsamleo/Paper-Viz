from bubble import Bubble
fig=Bubble(file="/Example_Data/Bubble/bubble_gdp.xlsx")
fig.bubble_plot(
    file='/Example_Data/Bubble/bubble_gdp.xlsx',
    x_col_name='Birth Rate',
    y_col_name='Life Expectancy',
    bubble_col='GDP',
    x_label='Life Expectancy',
    y_label='Birth Rate',
    bubble_name='Name',
    paper_type='double',
    plot_type='Stack',
    legend_title='Country name',
    save_image=True,
    output_name='Bubble chart'
)