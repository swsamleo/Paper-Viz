from time_series import TimeSeries

file_name = "mortality.csv'"

ts = TimeSeries(file_name)
ts.plot(
    x_col_name='date',
    y_col_name=['mdeaths', 'fdeaths'],
    xlabel='Date',
    ylabel=['Deaths'],
    legend=['Male', 'Female'],
    save_fig=True,
    fig_path='Images/Time_series.png')