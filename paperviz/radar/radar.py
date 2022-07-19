# Data analysis library numpy and pandas
import pandas as pd
import numpy as np

# Data visualization library matplotlib and seaborn
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.font_manager
# Get the file path and file type
import mimetypes
import urllib
import os
## import data visualization library matplotlib and seaborn
## import module to read files
import mimetypes
import os
import urllib
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import pandas as pd
import platform
import requests
import collections
#
# path_current = os.getcwd()
# # the path is where the dataset saved
# path = path_current + '/Example_Data/Radar/'
# # the "path_img" is the position where final image will be saved
# path_img = path_current + '/Images/'
class Radar:
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
    # read data
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


    def radar_plot(self, file, index_col=None, category_col=None, y_col_list=None, y_lim=None,output_name=None,
                   **kwargs):
        """Radar chart with selected overlay

        This function will convert the user's incoming data set into DataFrame and then draw
        the radar Chart using Matplotlib. The radar chart can show category, y, overlay.

        To use this function, User need a dataset with three variable columns. The three variables are
        index_col, category_col and y_col_list. The index column usually the name of that row such as 'player,
        The category_col is list of category and the y_col_list is the list of y value need to present.

        In our example, The index_col is player, The category_col is 
        ['Pace','Shooting','Passing','Dribbling','Defending','Physical'],
        and the y_col_list is ['Cristiano Ronaldo'].

        Args:
            file: file name of your data source, it support csv/excel,text.for example:'new_file.csv'
            index_col: The index column. Normally it should be the name of the content
            category_col: input list of attributes for the radar plot
            y_col_name: input list of items
            y_lim: The Y lim value

        """
        header_list = self.data.columns.values.tolist()
        df_li = self.data.values.tolist()
        df = df_li[0]


        if index_col is None:
            index_col = header_list[0]
        if category_col is None:
            header_list.pop(0)
            category_col = header_list
        if y_col_list is None:
            y_col_list = str(df[0])
        if y_lim is None:
            y_lim = 100
        if output_name is None:
            output_name = 'radar.pdf'


        conf = {
            'figsize': 
            (6, 4),
            'overlay':
            True,
            'linewidth':
            2,
            'gridlinewidth':
            0.8,
            'labeltext_size':
            20,
            'labelpad':
            10,
            'legend_size':
            10,
            'legend_loc':
            'upper right',
            'title':
            False,
            'title_pad':
            10,
            'title_size':
            15,
            'title_loc':
            'center',
            'title_height':
            1.1,
            'xtick_fontsize':
            15,
            'ytick_fontsize':
            15,
            'ytick_color':
            'blue',
            'xtick_color':
            'black',
            'alpha':
            0.3,
            'legendbox_loc': (1.1, 1.0),
            'plot_title':
            ''
        }

        # when new configuraton is set, update the original one
        conf.update(kwargs)

        # Input the valid filename and return the pandas dataframe for drawing
        # data = self.read_file(sfile)

        # set the index column
        
        data = self.data.set_index(index_col)
        # set the selected category from user input
        data = data[category_col]

        # set the y column
        data = data.loc[y_col_list]

        # create the close shape list
        close_shape = []

        # plot height and width
        fig = plt.figure(figsize=conf['figsize'])
        # polar plot
        ax = fig.add_subplot(111, polar=True)
        # radar plot
        for i in [data.values]:
            # link the line become a close shape radar plot
            
            close_shape = np.concatenate((i, [i[0]]))
            # calculate the angel of label placement
            label_placement = np.linspace(start=0,
                                          stop=2 * np.pi,
                                          num=len(close_shape))
            
            ax.plot(label_placement, close_shape)
            

            # The overlay background
            if conf['overlay'] == True:
                ax.fill(label_placement, close_shape, alpha=conf['alpha'])

        # apply the labels and line into the right place
        lines, labels = plt.thetagrids(np.degrees(label_placement),
                                       labels=np.concatenate((category_col, [category_col[0]])))

        # add the legend, legend will show the y values
        ax.legend(labels=[y_col_list],
                  bbox_to_anchor=conf['legendbox_loc'],
                  fontsize=conf['legend_size'])
        
        
        # x tricks and y ticks color and fontsize
        plt.yticks(color=conf['ytick_color'], fontsize=conf['ytick_fontsize'])
        plt.xticks(color=conf['xtick_color'], fontsize=conf['xtick_fontsize'])

        # Y lim value from user input for accurcy
        

        # plot title
        plt.title(conf['plot_title'],
                  fontsize=conf['title_size'],
                  y=conf['title_height'])
        

        # xtrick alignment, It can automatict adjust x tricks location, let the x tricks lables outside of the plot
        for theta, label in zip(ax.get_xticks(), ax.get_xticklabels()):
            theta = theta * ax.get_theta_direction() + ax.get_theta_offset()
            theta = np.pi / 2 - theta
            y, x = np.cos(theta), np.sin(theta)
            if x >= 0.1:
                label.set_horizontalalignment('left')
            if x <= -0.1:
                label.set_horizontalalignment('right')
            if y >= 0.5:
                label.set_verticalalignment('bottom')
            if y <= -0.5:
                label.set_verticalalignment('top')
        # save the plot
        plt.show()
        plt.tight_layout()
        plt.savefig(self.path_img + output_name)

    def spider_plot(self, file, index_col, category_col, y_col_list, y_lim,output_name,
                    **kwargs):
        """Spider chart with selected overlay

        This function will convert the user's incoming data set into DataFrame and then draw
        the spider Chart using Matplotlib. The radar chart can show category, y, overlay.

        To use this function, User need a dataset with three variable columns. The three variables are
        index_col, category_col and y_col_list. The index column usually the name of that row such as 'player,
        The category_col is list of category and the y_col_list is the list of y value need to present.

        In our example, The index_col is status, The category_col is 
        ['blood sugar','blood pressure','blood oxygen','blood fat',' heart rate'],
        and the y_col_list is ['Before','After'].

        Args:
            file: file name of your data source, it support csv/excel,text.for example:'new_file.csv'
            index_col: The index column. Normally it should be the name of the content
            category_col: input list of attributes for the radar plot
            y_col_name: input list of items
            y_lim: The Y lim value

        """

        conf = {
            'figsize':
            (6, 4),
            'overlay':
            False,
            'linewidth':
            2,
            'gridline_width':
            0.8,
            'gridline_color':
            'grey',
            'gridline_style':
            '-',
            'labeltext_size':
            20,
            'labelpad':
            10,
            'legend_size':
            10,
            'legend_loc':
            'upper right',
            'title':
            False,
            'title_pad':
            10,
            'title_size':
            15,
            'title_loc':
            'center',
            'title_height':
            1.1,
            'xtick_fontsize':
            15,
            'ytick_fontsize':
            15,
            'ytick_color':
            'blue',
            'xtick_color':
            'black',
            'alpha':
            0.3,
            'legendbox_loc': (1.3, 1.0),
            'plot_title':
            ''
        }

        # when new configuraton is set, update the original one
        conf.update(kwargs)

        # read file
        # data = self.read_file(file)

        # set the index column
        data = self.data.set_index(index_col)
        # set the selected category from user input
       
        data = self.data[category_col]
        # set the y column
        data = self.data.loc[y_col_list]
        # create the close shape list
        close_shape = []
        # plot height and width
        fig = plt.figure(figsize=conf['figsize'])
        # polar plot
        ax = fig.add_subplot(111, polar=True)

        # spider plot
        for i in data.values:
            # link the line become a close shape radar plot
            close_shape = np.concatenate((i, [i[0]]))
            # calculate the angel of label placement
            label_placement = np.linspace(start=0,
                                          stop=2 * np.pi,
                                          num=len(close_shape))
            ax.plot(label_placement, close_shape)

            # The overlay background
            if conf['overlay'] == True:
                ax.fill(label_placement, close_shape, alpha=conf['alpha'])

            # change the gridline become spider plot
            pl = ax.yaxis.get_gridlines()
            for line in pl:
                line.get_path()._interpolation_steps = len(close_shape)

        # adjust the gridline color,linewidth and linestyle
        ax.grid(color=conf['gridline_color'],
                linestyle=conf['gridline_style'],
                linewidth=conf['gridline_width'])

        # apply the labels and line into the right place
        lines, labels = plt.thetagrids(np.degrees(label_placement),
                                       labels=category_col)

        # add the legend, legend will show the y values
        ax.legend(labels=y_col_list,
                  bbox_to_anchor=conf['legendbox_loc'],
                  fontsize=conf['legend_size'])

        # x tricks and y ticks color and fontsize
        plt.yticks(color=conf['ytick_color'], fontsize=conf['ytick_fontsize'])
        plt.xticks(color=conf['xtick_color'], fontsize=conf['xtick_fontsize'])

        # Y lim value from user input for accurcy
        plt.ylim(y_lim)

        # save the plot
        plt.savefig(self.path_img + output_name)

        # plot title
        plt.title(conf['plot_title'],
                  fontsize=conf['title_size'],
                  y=conf['title_height'])

        # xtrick alignment, It can automatict adjust x tricks location, let the x tricks lables outside of the plot
        for theta, label in zip(ax.get_xticks(), ax.get_xticklabels()):
            theta = theta * ax.get_theta_direction() + ax.get_theta_offset()
            theta = np.pi / 2 - theta
            y, x = np.cos(theta), np.sin(theta)
            if x >= 0.1:
                label.set_horizontalalignment('left')
            if x <= -0.1:
                label.set_horizontalalignment('right')
            if y >= 0.5:
                label.set_verticalalignment('bottom')
            if y <= -0.5:
                label.set_verticalalignment('top')

        # save the plot
        plt.tight_layout()
        plt.show()
        plt.savefig(self.path_img + output_name)
