from area import Area_plot
model=Area_plot(path=r'C:\Users\87139\Desktop\Paper-Viz-master\Example_Data',path_img='Images\\')
model.area(
    file="museum_visitors_line.csv",
    x_col_name=['index'],
    y_col_name=['Avila_Adobe','Firehouse_Museum','Chinese_American_Museum','America_Tropical_Interpretive_Center'],
    x_lable='Index',
    y_lable='vistors number',
    paper_type='double',
    plot_type='Stack',
    title='Number of vistors in four museums',
    save_image=True,
    file_name='Area chart'
)