from heatmap import heat_map
model=heat_map(path='Example_Data\\heat\\',path_img='Images\\')
model.heat(
    file='1.xlsx',
    col_labels=['Farmer Joe	Upland Bros.','Smith Gardening','Agrifun','Organiculture','BioGoods Ltd.','Cornylee Corp.'],
    row_labels=['cucumber','tomato','lettuce','asparagus','potato','wheat','barley'],
    paper_type='double'
)