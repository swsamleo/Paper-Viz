from line import line
model=line()
model.plot(
    file="museum_visitors_line.csv",
    x_col_name=['index'],
    y_col_name=['Avila_Adobe','Firehouse_Museum','Chinese_American_Museum','America_Tropical_Interpretive_Center'],
    x_label='Index',
    y_label='vistors number',
    legend_label=['Avila_Adobe','Firehouse_Museum','Chinese_American_Museum','America_Tropical_Interpretive_Center'],
    paper_type='double',
    plot_type='Stack',
    title='Number of vistors in four museums',
    save_image=True,
    file_name='Line chart'
)