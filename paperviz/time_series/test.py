from time_series import TimeSeries

file = 'Example_Data\Time_series/mortality.csv'
ts = TimeSeries(file)
ts.plot(
    x_col_name='date',
    y_col_name=['mdeaths', 'fdeaths'],
    xlabel='Date',
    ylabel=['Deaths'],
    legend=['Male', 'Female'],
    save_fig=True,
    fig_path='Images/Time_series.png')