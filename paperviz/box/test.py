from box import Box_plot
model=Box_plot()
model.box(
    file='1.xlsx',
    x_col_name=['line1'],
    paper_type='double',
    plot_type='Stack',
    save_image=True,
    file_name='Box chart'
)