# Data analysis library numpy and pandas
import numpy as np
import matplotlib
import matplotlib.font_manager
import mimetypes
import os
import matplotlib.pyplot as plt
import pandas as pd
import platform

class heat_map:
    # read data
  def __init__(self, file):

    self.path = self.get_cwd()
    self.data = self.read_file(file, self.path)
    self.path_img = self.get_cwd()

  def get_cwd(self):
        # get the current path of file .
        if platform.system().lower() == 'windows':
            path = os.getcwd() + '/'

        elif platform.system().lower() == 'linux':
            path = os.getcwd().replace('/', '\\') + '/'
        return path

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
  # row_labels: the x axis labels
  # col_labels: the y axis labels/8-
  # paper_type : 'single' or 'double'lk
  def heat(self, file, row_labels = None, col_labels = None, paper_type = None, **kwargs):
    # Configuration of the heatmap
    # plotwidth: width of the plot
    # plotheight: height of the plot
    # my_font: the typeface of x, y labels
    # labeltext_size: text size of x,y labels
    # labelpad: pad size of label
    # title: True or False as options. If it is True, add title for the plot
    # title_pad: if the title is True, modify pad size of title
    # title_size: if the title is True, modify size of title
    # title_loc: if the title is True, modify location of title
    # cmap： the color of heatmap
    # annotate: True or False, if true, the value will show in the heatmap
    # colorbar: True or False, if true, the color bar of heatmap will show
    # barlabel: the label of color bar
    # xlabel_rotate: the rotation of x axis labels
    # ylabel_rotate: the rotation of y axis labels
    # barlabel_rotate: the rotation of colorbar labels
    # x_label: the content of x label
    # y_label: the content of y label
    # annotate_textsize: the font size of annotation
    # save_image: True or False as options. If it is True, save chart
    # savefig_bbox_inches: Bounding box in inches
    # file_name: the file name in saving image
    header_list = self.data.columns.values.tolist()

    df_li = self.data.values.tolist()
    # print(df_li)
    column_list = []
    for i in df_li:
        column_list.append(i[0])


    if col_labels is None:
        col_labels = header_list[0]
    if row_labels is None:
        row_labels = column_list
    if paper_type is None:
        paper_type = 'double'

    single_column_conf={ 'plotwidth':8,
                      'plotheight':6, 
                      'my_font':'DejaVu Sans',
                      'labeltext_size':20,
                      'labelpad':10,
                      'title':False,
                      'title_pad':10,
                      'title_size':20,
                      'title_loc':'center', 
                      'cmap':'GnBu',
                      'alpha':0.9,
                      'annotate':True,
                      'colorbar':True,
                      'barlabel':None,
                      'xlabel_rotate':45,
                      'ylabel_rotate':0,
                      'barlabel_rotate':-90,
                      'x_label':None,
                      'y_label':None,
                      'annotate_textsize':13,
                      'save_image':False,
                      'savefig_bbox_inches':'tight',
                      'file_name':'heatmap'
    }

    double_column_conf={ 'plotwidth':14,
                      'plotheight':14,
                      'my_font':'DejaVu Sans',
                      'backgrid':True,
                      'isframe':True,
                      'labeltext_size':22,
                      'labelpad':10,
                      'title':False,
                      'title_pad':10,
                      'title_size':22,
                      'title_loc':'center', 
                      'cmap':'GnBu',
                      'alpha':0.9,
                      'annotate':True,
                      'colorbar':True,
                      'barlabel':None,
                      'xlabel_rotate':45,
                      'ylabel_rotate':0,
                      'barlabel_rotate':-90,
                      'x_label':None,
                      'y_label':None,
                      'annotate_textsize':12,
                      'save_image':False,
                      'savefig_bbox_inches':'tight',
                      'file_name':'heatmap'
    }

    # choose a configuration
    if paper_type == 'single':
      conf = single_column_conf
    elif paper_type == 'double':
      conf = double_column_conf


    # when new configuraton is set, update the original one
    conf.update(kwargs)  
    # create figure and set figure size  
    fig, ax_left = plt.subplots(figsize = (conf['plotwidth'], conf['plotheight']))

    # x,y label setting                   
    ax_left.set_xlabel(conf['x_label'], fontproperties=conf['my_font'], fontsize=conf['labeltext_size'], labelpad=conf['labelpad'])
    ax_left.set_ylabel(conf['y_label'], fontproperties=conf['my_font'], fontsize=conf['labeltext_size'], labelpad=conf['labelpad'])

    # plot
    # find the row_label
    if row_labels not in list(self.data.columns):
      k=''
      for i in self.data.columns:
        if set(row_labels) <= set(self.data[i].values):
          k=i
        else:
          pass

      print(k)
      data=self.data.set_index(k)
      data.index.name=None
    # plot heatmap        
    im=ax_left.imshow(data,cmap=conf['cmap'],alpha=conf['alpha'])
    ax_left.set_xticks(np.arange(len(self.data.columns)))
    ax_left.set_yticks(np.arange(len(self.data.index)))
    # and label them with the respective list entries
    ax_left.set_xticklabels(self.data.columns,fontsize=conf['labeltext_size'])
    ax_left.set_yticklabels(self.data.index,fontsize=conf['labeltext_size'])
    # rotate x, y axis
    plt.setp(ax_left.get_xticklabels(), rotation=conf['xlabel_rotate'], ha="right",
          rotation_mode="anchor")
    plt.setp(ax_left.get_yticklabels(), rotation=conf['ylabel_rotate'], ha="right",
          rotation_mode="anchor")
    # if colorbar is true, draw color bar
    if conf['colorbar'] == True:
      cbar = ax_left.figure.colorbar(im, ax=ax_left)
      cbar.ax.tick_params(labelsize=conf['labeltext_size'])
      if conf['barlabel'] != None:
        cbar.ax.set_ylabel(conf['barlabel'], rotation=conf['barlabel_rotate'], va="bottom",fontsize=conf['labeltext_size'])
    # define an annotate function
    # the default format is .2f
    # if the background color is light the font color will be black, else, the font color will be white
    def annotate_heatmap(im, data=None, valfmt="{x:.2f}",
                     textcolors=("black", "white"),
                     threshold=None, **textkw):
      if not isinstance(data, (list, np.ndarray)):
          data = im.get_array()
      # get the boundary threshold （use 1/2 of max)
      if threshold is not None:
        threshold = im.norm(threshold)
      else:
        threshold = im.norm(data.max())/2.
      # set the position of annotation  
      kw = dict(horizontalalignment="center",
                  verticalalignment="center")
      kw.update(textkw)

      if isinstance(valfmt, str):
        valfmt = matplotlib.ticker.StrMethodFormatter(valfmt)
      texts = []
      # get the colored annotate font
      for i in range(data.shape[0]):
        for j in range(data.shape[1]):
          kw.update(color=textcolors[int(im.norm(data[i, j]) > threshold)])
          text = im.axes.text(j, i, valfmt(data[i, j]), fontsize=conf['annotate_textsize'],**kw)
          texts.append(text)
      return texts

    if conf['annotate'] == True:
      texts = annotate_heatmap(im, valfmt="{x:.1f}")
    # title setting
    if conf['title'] == False:
      pass
    else:
      ax_left.set_title(conf['title'], fontsize=conf['title_size'], loc=conf['title_loc'], pad=conf['title_pad'])
    # save image setting
    if conf['save_image'] == True:
      file_name=conf['file_name']
      file_newname = self.get_available_name(file_name)
      plt.savefig(self.path_img+file_newname, bbox_inches=conf['savefig_bbox_inches'],dpi=600,format='jpg') 

    plt.show()