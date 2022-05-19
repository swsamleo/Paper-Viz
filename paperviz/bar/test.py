from bar import bar_chart
fig=bar_chart(path='Example_Data\Bar\\')
fig.Bar(file='Stacked_Bar.csv',  x_col_name=['men_means','men_std','women_means','women_std'], 
 y_col_name=['G1','G2','G3','G4','G5'], x_label='Categories', y_label='Value',  direction='horizontal')