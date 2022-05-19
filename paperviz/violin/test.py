from violin import Violin_plot
avio=Violin_plot()
avio.Violin(
    file='4.xlsx',
    x_col_name=['line1','line2','line3'],
    category='gender',
    x_label='x',y_label='y',
    paper_type='single',
    save_image=True
)