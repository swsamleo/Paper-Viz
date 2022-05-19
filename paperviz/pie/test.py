from pie import Pie_plot
model=Pie_plot(path='Example_Data\\Pie\\',path_img='Images\\')
model.Pie(
    file='1.xlsx',
    value=['quants'],
    label=['country'],
    paper_type='double',
    plot_type='Stack',
    save_image=True,
    file_name='Pie chart'
)