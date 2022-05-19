from pyramid import pyramid
fig=pyramid()
fig.pyramid(file='email_campaign_funnel.csv',x_col_name=['Users'],y_col_name=['Stage'],group_col=['Gender'],paper_type='double')