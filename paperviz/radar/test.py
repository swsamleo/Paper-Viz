from radar import Radar
fig=Radar()
fig.radar_plot(file='ronaldo.xlsx', index_col='player', category_col=['Pace','Shooting','Passing','Dribbling','Defending','Physical'], 
y_col_list='Ronaldo', y_lim=100,output_name='radar.pdf')