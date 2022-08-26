
import seaborn as sns
import matplotlib
import matplotlib.font_manager
import mimetypes
import os
import matplotlib.pyplot as plt
import pandas as pd
import platform


class Area: 
  # read data
  def __init__(self, path=os.getcwd(),file='area.csv'):
      
      # get the current path of file .
      if platform.system().lower() == 'windows':
          path = path + '/'
          self.path_img=os.getcwd()+ '/'
      elif platform.system().lower() == 'linux':
          path = path.replace('/', '\\') + '/'
          self.path_img=os.getcwd().replace('/', '\\') + '/'
      self.data = self.read_file(file, path)
      

  def read_file(self, file, path):
      """Read different types of files and return pandas dataframe.

      This function can transform multiple file type such as csv/excel/text into
      a pandas dataframe. User need to input the filename such as: 'file.csv'.
      If the file type cannot be find or not support it, it will return the message.

      Args:
          file: filename of user data source

      Returns:
          data : A pandas dataframe

      """
      # Get the file URL
      # try:
      file_url = path + file

      ftype = mimetypes.guess_type(file_url, strict=True)[0]
      # except FileNotFoundError:
      #     print('e')

      # try catch
      # use mimetypes package to guess the file type
      # For example: 'file.csv' will return 'csv'
      # ftype = mimetypes.guess_type(file_url, strict=True)[0]
      ## read data file according to its format, default includes three types of files: csv/excel/text
      # read csv format data
      if 'csv' in ftype:
          data = pd.read_csv(file_url)
      elif 'excel' in ftype:
          data = pd.read_csv(file_url)
      # read excel format data
      elif 'sheet' in ftype:
          data = pd.read_excel(file_url)
      # read text format data from
      elif ftype == 'text/plain':
          data = pd.read_csv(file_url, sep="\t")


      else:
          raise FileNotFoundError("File type cannot find!")

      self.__dict__['data'] = data
      return data
  # Data sorting function 
  # x_col_name:'index' or actual columns name
  # y_col_name: actual y columns name
  # sort the databy using average value,

  def sort(self,file,x_col_name,y_col_name):
    # if the x_col_name is index return sorted y columns name and new index
    if x_col_name[0] == 'index':      
      for i in y_col_name: 
        self.data.loc['sort',i]=self.data.loc[:'sort',i].mean()
      newdata=self.data[y_col_name].sort_values(axis=1,ascending=False,by='sort')
      y_col_name=newdata.columns.tolist()
      y_col_name=[i for i in y_col_name if i not in x_col_name]
      self.data.drop(['sort'],inplace=True)
      self.data.index = pd.RangeIndex(start=0, stop=len(self.data.index), step=1)
      return y_col_name,self.data.index
    else:
      for i in y_col_name:
        self.data.loc['sort',i]=self.data.loc[:'sort',i].mean()
      newdata=pd.concat([self.data[x_col_name],self.data[y_col_name].sort_values(axis=1,ascending=False,by='sort')],axis=1)
      newdata=self.data[y_col_name].sort_values(axis=1,ascending=False,by='sort')
      y_col_name=newdata.columns.tolist()
      y_col_name=[i for i in y_col_name if i not in x_col_name]
      return y_col_name

  # check the available file name
  # if the input file name already existed then rename to file_1, file_2
  def get_available_name(self,filename):
    n=[1]
    def check_meta(file_name):
      file_name_new=file_name
      if file_name in [os.path.splitext(i)[0] for i in os.listdir(self.path_img)]:   
          file_name_new=file_name+'_'+str(n[0])
          n[0]+=1
      if file_name_new in [os.path.splitext(i)[0] for i in os.listdir(self.path_img)]:   
          file_name_new=check_meta(file_name)
      return file_name_new
    available_name=check_meta(filename)
    return available_name

  # file: file name of your data source
  # x_col_name: ['index'] or ['x_column_name_a','x_column_name_b'...]
  # y_col_name: ['y_column_name_a','y_column_name_b'...]
  # plot_type: type of plot: stack ,percentage or simple
  # paper_type : 'single' or 'double'
  def plot(self,  x_col_name=None, y_col_name=None, plot_type=None,paper_type=None,**kwargs):

    # Configuration of the line chart
    # plotwidth: width of the plot
    # plotheight: height of the plot
    # backgrid: backgrid of the plot
    # isframe: frame of the plot
    # my_font: the typeface of x, y labels
    # linewidth: linewidth of the lines in the plot
    # gridlinewidth: if backgrid is True, grid linewidth is the line width of background grid
    # labeltext_size: text size of x,y labels
    # x_label: the content of x label
    # y_label: the content of y label
    # labelpad: pad size of label
    # legend_size: size of legend
    # legend_loc: location of legend
    # legend_ncol: the legend columns number
    # title: True or False as options. If it is True, add title for the plot
    # title_pad: if the title is True, modify pad size of title
    # title_size: if the title is True, modify size of title
    # title_loc: if the title is True, modify location of title
    # Stack_colour_set: stack area chart color palette (the number of y columns <7)
    # Area_colour_set: simple area chart color palette (the number of y columns <7)
    # palette: if the number of y columns >7 in all kinds of area chart, use this color palette
    # ticks: True or False as options. If it is True, add ticks of x and y axis.
    # tick_size: size of tick 
    # tick_direction: 'out', 'inout' and 'in' options.
    # y_scale: the extra blank in y axis
    # alpha: transparency of each area
    # arealinewidth: in the simple area chart, the boundary width
    # y_col_num: the critical value of y columns in choosing color palette
    # sort: using sort function to handle data
    # save_image: True or False as options. If it is True, save chart
    # savefig_bbox_inches: Bounding box in inches
    # file_name: the file name in saving image
    header_list = self.data.columns.values.tolist()

    if x_col_name is None:
        x_col_name = ['index']
    if y_col_name is None:
        y_col_name = header_list
    if paper_type is None:
        paper_type = 'double'
    if plot_type is None:
        plot_type = 'Stack'


    single_column_conf={ 'plotwidth':8,#weight
                        'plotheight':6, #height
                        'my_font':'DejaVu Sans',
                        'backgrid':True,
                        'isframe':True,
                        'linewidth':2,
                        # 'gridlinewidth':0.5,
                        'labeltext_size':15,
                        'x_label':None,
                        'y_label':None,
                        'labelpad':10,
                        'legend_size':10,
                        'legend_loc':'upper right', 
                        'legend_ncol':2,
                        'title':False,
                        'title_pad':8,
                        'title_size':14,
                        'title_loc':'center',     
                        'Stack_colour_set':['006D77','8AA8A1','A1683A','E8998D','D1B490','EE7B30','FFCB77'],
                        'Area_colour_set':[(255/255, 173/255, 173/255),(255/255, 214/255, 165/255),(253/255, 255/255, 182/255),(202/255, 255/255, 191/255),
                                           (155/255, 246/255, 255/255),(160/255, 196/255, 255/255),(255/255, 198/255, 255/255)],
                        'palette':sns.color_palette('Set2'),
                        'ticks':True,
                        'tick_size':14,
                        'tick_direction':'out',
                        'save_image':False,
                        'y_scale':1.20,
                        'alpha':0.7,
                        'arealinewidth':1,
                        'y_col_num':7,
                        'sort':True,
                        'file_name':'area_chart',
                        'savefig_bbox_inches':'tight',

                        }  
    double_column_conf={ 'plotwidth':8,#weight
                        'plotheight':6, #height
                        'my_font':'DejaVu Sans',
                        'backgrid':True,
                        'isframe':True,
                        'linewidth':2,
                        'gridlinewidth':0.5,
                        'labeltext_size':25,
                        'x_label':None,
                        'y_label':None,
                        'labelpad':10,
                        'legend_size':10,
                        'legend_loc':'upper right', 
                        'legend_ncol':2,
                        'title':False,
                        'title_pad':10,
                        'title_size':20,
                        'title_loc':'center',     
                        'Stack_colour_set':['006D77','8AA8A1','A1683A','E8998D','D1B490','EE7B30','FFCB77'],
                        'Area_colour_set':[(255/255, 173/255, 173/255),(255/255, 214/255, 165/255),(253/255, 255/255, 182/255),(202/255, 255/255, 191/255),
                                           (155/255, 246/255, 255/255),(160/255, 196/255, 255/255),(255/255, 198/255, 255/255)],
                        'palette':sns.color_palette('Set2'),
                        'ticks':True,
                        'tick_size':20,
                        'tick_direction':'out',
                        'y_scale':1.20,
                        'alpha':0.7,
                        'arealinewidth':1,
                        'y_col_num':7,
                        'sort':True,
                        'save_image':False,
                        'savefig_bbox_inches':'tight',
                        'file_name':'area_chart',
                       
                        }
    conf = []
    if paper_type == 'single':
      conf = single_column_conf
    elif paper_type == 'double':
      conf = double_column_conf                    

    # when new configuraton is set, update the original one
    conf.update(kwargs) 

    # create figure and set figure size  
    fig, ax_left = plt.subplots(figsize = (conf['plotwidth'], conf['plotheight']))

    # background grid setting
    if conf['backgrid'] == True:
      ax_left.grid(linestyle="--", linewidth=conf['gridlinewidth'], color='gray', alpha=0.5)
            
    # # read file
    # try:
    #   data = self.read_file(file,path)
    # except Exception:
    #   print('Sorry, this file does not exist, please check the file name')
 
 
    #plot
    #area chart type setting
    # stack area plot 
    if plot_type == 'Stack':
    # x column is index
      if x_col_name[0] =='index':  
        ydata=[]

        for i in self.data[y_col_name]:
            ydata.append(self.data[i].tolist())
        # determine the number of y columns is more than critical value or not
        # if yes, using the setted color palette
        if len(y_col_name)<=conf['y_col_num']:        
          ax_left.stackplot(self.data.index,ydata,colors=conf['Stack_colour_set'],labels=y_col_name,alpha=conf['alpha']) ##
        # if not, using the seaborn color palette
        else:
          ax_left.stackplot(self.data.index,ydata,colors=conf['palette'],labels=y_col_name,alpha=conf['alpha'])
        # scale y axis to get more blank            
        ax_left_ylim = ax_left.get_ylim()
        ax_left.set_ylim(ax_left_ylim[0],ax_left_ylim[1]*conf['y_scale'])

      # if x colunm is not index
      else:
        ydata=[]
        for i in self.data[y_col_name]:
            ydata.append(self.data[i].tolist())
        # determine the number of y columns is more than critical value or not
        # if yes, using the setted color palette
        if len(y_col_name)<=conf['y_col_num']:         
          ax_left.stackplot(self.data[x_col_name[0]],ydata,colors=conf['Stack_colour_set'],labels=y_col_name,alpha=conf['alpha'])
        # if not, using the seaborn color palette  
        else:
          ax_left.stackplot(self.data[x_col_name[0]],ydata,colors=conf['palette'],labels=y_col_name,alpha=conf['alpha'])
        # scale y axis to get more blank    
        ax_left_ylim = ax_left.get_ylim()
        ax_left.set_ylim(ax_left_ylim[0],ax_left_ylim[1]*conf['y_scale']) 
    
    # percentage area plot
    if plot_type == 'percentage':
      # x column is index
      if x_col_name[0] =='index':
        ydata=[]
        # get the percentange of each part
        data = self.data[y_col_name].divide(self.data[y_col_name].sum(axis=1), axis=0)
        for i in data[y_col_name]:
            ydata.append(data[i].tolist()) 
        # determine the number of y columns is more than critical value or not
        # if yes, using the setted color palette
        if len(y_col_name)<=conf['y_col_num']:        
          ax_left.stackplot(data.index,ydata,colors=conf['Stack_colour_set'],labels=y_col_name,alpha=conf['alpha'])
        # if not, using the seaborn color palette  
        else:
          ax_left.stackplot(data.index,ydata,colors=conf['palette'],labels=y_col_name,alpha=conf['alpha'])   
        # scale y axis to get more blank           
        ax_left_ylim = ax_left.get_ylim()
        ax_left.set_ylim(ax_left_ylim[0],ax_left_ylim[1])
      
      # if x colunm is not index
      else:
        ydata=[]
        data = self.data[y_col_name].divide(self.data[y_col_name].sum(axis=1), axis=0)

        for i in data[y_col_name]:
          ydata.append(data[i].tolist()) 
        if len(y_col_name)<=conf['y_col_num']:         
          ax_left.stackplot(data[x_col_name[0]],ydata,colors=conf['Stack_colour_set'],labels=y_col_name,alpha=conf['alpha'])
            
        else:
          ax_left.stackplot(data[x_col_name[0]],ydata,colors=conf['palette'],labels=y_col_name,alpha=conf['alpha'])
        ax_left_ylim = ax_left.get_ylim()
        ax_left.set_ylim(ax_left_ylim[0],ax_left_ylim[1]) 
    
    #simple area chart
    if plot_type == 'Simple':
     
      # x column is index      
      if x_col_name[0] =='index':
        # data handling by using sort function
        if conf['sort'] == True:
          # if the input x coluns is index, the function return the sorted y columns and new index
          y_col_name=self.sort(self.data,x_col_name,y_col_name)[0]
          self.data.index=self.sort(self.data,x_col_name,y_col_name)[1]
        
        for i in range(0,len(y_col_name)):
          # determine the number of y columns is more than critical value or not
          # if yes, using the setted color palette
          if len(y_col_name)<=conf['y_col_num']:                     
            ax_left.fill_between(self.data.index, self.data[y_col_name[i]], color=conf['Area_colour_set'][i],
                 alpha=0.7, label=y_col_name[i])
          # if not, using the seaborn color palette    
          else:
            ax_left.fill_between(self.data.index, self.data[y_col_name[i]], color=conf['palette'][i],
                 alpha=0.7, label=y_col_name[i])
          # draw the bounday line   
          ax_left.plot(self.data.index, self.data[y_col_name[i]], color="Black", alpha=conf['alpha'], linewidth=conf['arealinewidth'])
        # scale y axis to get more blank 
        ax_left_ylim = ax_left.get_ylim()         
        ax_left.set_ylim(ax_left_ylim[0],ax_left_ylim[1]*conf['y_scale'])

      # x colunm is not index 
      else:
        #data handling by using sort function
        if conf['sort'] == True:
          # if the x column name is actual columns name, the function return sorted y columns name
          y_col_name=self.sort(self.data,x_col_name,y_col_name)
        
        for i in range(0,len(y_col_name)):
          if len(y_col_name)<=conf['y_col_num']: 
            ax_left.fill_between(self.data[x_col_name[0]], self.data[y_col_name[i]], color=conf['Area_colour_set'][i],
                  alpha=conf['alpha'], label=y_col_name[i])
          else:
            ax_left.fill_between(self.data[x_col_name[0]], self.data[y_col_name[i]], color=conf['palette'][i],
                  alpha=conf['alpha'], label=y_col_name[i])
          ax_left.plot(self.data[x_col_name[0]], self.data[y_col_name[i]], color="Black", alpha=conf['alpha'], linewidth=conf['arealinewidth'])
        ax_left_ylim = ax_left.get_ylim()          
        ax_left.set_ylim(ax_left_ylim[0],ax_left_ylim[1]*conf['y_scale'])
    
    #set ticks size
    for tick in ax_left.xaxis.get_major_ticks():
      tick.label.set_fontsize(conf['tick_size'])
    for tick in ax_left.yaxis.get_major_ticks():
      tick.label.set_fontsize(conf['tick_size'])

    # if False, top and right borders removing    
    if conf['isframe'] == False:
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        
    # x, y axis setting
    ax_left.set_xlabel(conf['x_label'], fontproperties=conf['my_font'], fontsize=conf['labeltext_size'], labelpad=conf['labelpad'])
    ax_left.set_ylabel(conf['y_label'], fontproperties=conf['my_font'], fontsize=conf['labeltext_size'], labelpad=conf['labelpad'])

    # set x, y tick's direction, default:out, can be set to in,out,inout
    if conf['tick_direction'] == 'in':
      matplotlib.rcParams['xtick.direction'] = 'in'
      matplotlib.rcParams['ytick.direction'] = 'in'
    elif conf['tick_direction'] == 'inout':
      matplotlib.rcParams['xtick.direction'] = 'inout'
      matplotlib.rcParams['ytick.direction'] = 'inout'
    elif conf['tick_direction'] == 'out':
      matplotlib.rcParams['xtick.direction'] = 'out'
      matplotlib.rcParams['ytick.direction'] = 'out'

    #legend setting
    # show in 2 line, location: upper right 
    ax_left.legend(ncol=conf['legend_ncol'],loc=conf['legend_loc'], fontsize=conf['legend_size']) #conf
    #title setting
    if conf['title'] == False:
      pass
    else:
      ax_left.set_title(conf['title'], fontsize=conf['title_size'], loc=conf['title_loc'], pad=conf['title_pad'])
    #save image
    if conf['save_image'] == True:
      file_name=conf['file_name']
      # use function to get available file name
      file_newname = self.get_available_name(file_name)
      # plt.savefig(self.path_img+file_newname, bbox_inches=conf['savefig_bbox_inches'],dpi=600,format='jpg')
      plt.savefig(self.path_img + file_name )
     
    # showing the image
    plt.show()