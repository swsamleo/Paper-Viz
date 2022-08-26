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

class Defaultdict(collections.UserDict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.confint = {
            'plotwidth':
                [6,10],
            'plotheight':
                [4,8],
            'linewidth':
                [1,4],
            'gridlinewidth':
                [0.1,1],
            'gridline_alpha':
                [0.1,1],
            'labeltext_size':
                [10, 30],
            'labelpad':
                [5,20],
            'legend_size':
                [5,20],
            'title_pad':
                [5,20],
            'title_size':
                [5,30],
            'bubble_scale':
                [10, 100],
            'xtrick_fontsize':
                [5,20],
            'ytrick_fontsize':
                [5,20],
            'alpha':
                [0.1,1],
            'colorbar_labelsize':
                [5,30],
            'bubble_size':
                [100,1000]
        }
        self.conflist = ['bubble_colors']
        self.confbool = ['isframe', 'backgrid']
        self.confstr = [
            'my_font',
            'gridline_style',
            'gridline_color',
            'legend_loc',
            'title_loc',
            'bubble_marker',
            'plot_title',
            'bubble_cmap',
            'bubble_colors',
            'bubblesize_legend_loc',
            'bubbleszie_legend_title'
        ]

    def __setitem__(self, key, item):
        try:
            if key in self.confint:
                if type(item) == int or type(item) == float:
                    if self.confint[key][0]<=item and item<=self.confint[key][1]:
                        self.data[key] = item
                    else:
                        raise TypeError(f'the value of the {key} out of range !')
                else:
                    raise TypeError(f'the value of the {key} must be int !')
            elif key in self.confbool:
                if str(item) in ['True', 'False']:
                    self.data[key] = item
                else:
                    raise TypeError(f'the value of the {key} must be True or False !')
            elif key in self.confstr:
                if type(item)==str:
                    self.data[key] = item
                else:
                    raise TypeError(f'the value of the {key} must be str !')
            elif key in self.conflist:
                if type(item)==list:
                    self.data[key] = item
                else:
                    raise TypeError(f'the value of the {key} must be list !')
        except AttributeError:
            self.data[key] = item

class Bubble:
    def __init__(self, file):
        self.conf = Defaultdict(
            plotwidth=8,
            plotheight=6,
            my_font='DejaVu Sans',
            backgrid=True,
            isframe=True,
            linewidth=2,
            gridlinewidth=0.5,
            gridline_style='--',
            gridline_color='gray',
            gridline_alpha=0.8,
            labeltext_size=20,
            labelpad=10,
            legend_size=12,
            legend_loc='upper right',
            title_pad=10,
            title_size=15,
            bubble_scale=50,
            title_loc='center',
            xtrick_fontsize=15,
            ytrick_fontsize=15,
            bubble_marker='o',
            alpha=0.8,
            colorbar_labelsize=16,
            plot_title='',
            bubble_size=400,
            bubble_cmap='Blues',
            bubble_colors=[
                "#e07a5f", "#f4f1de", "#81b29a", "#f2cc8f",
                "#264653", "#2a9d8f", "#e9c46a", "#f4a261", "#e76f51",
                '#ECE133', '#56B4E9', "#3d405b", "#e07a5f", "#f4f1de",
                "#81b29a", "#f2cc8f", "#264653", "#2a9d8f", "#e9c46a",
                "#f4a261", "#e76f51", '#ECE133', '#56B4E9'
            ],
            bubblesize_legend_loc='lower left',
            bubbleszie_legend_title='Sizes'
        )
        self.path = self.get_cwd()
        self.data=self.read_file(file, self.path)
        


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
        print(path,file)
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
        elif 'excel'in ftype:
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

    def draw_setting(self, conf, ax, x_label, y_label):
        # part of picture setting

        if conf['backgrid'] == True:
            ax.grid(linestyle=conf['gridline_style'],
                    linewidth=conf['gridlinewidth'],
                    color=conf['gridline_color'],
                    alpha=conf['gridline_alpha'])

        ## x, y axis setting
        # fontsize: x, y title size
        ax.set_xlabel(x_label,
                      fontproperties=conf['my_font'],
                      fontsize=conf['labeltext_size'],
                      labelpad=conf['labelpad'])
        ax.set_ylabel(y_label,
                      fontproperties=conf['my_font'],
                      fontsize=conf['labeltext_size'],
                      labelpad=conf['labelpad'])

    def pic_save(self, conf, path_img, output_name, file_type):
        # save the picture in specific file type

        # xtricks and yticks font size
        plt.xticks(fontsize=self.conf['xtrick_fontsize'])
        plt.yticks(fontsize=self.conf['ytrick_fontsize'])

        # title
        plt.title(conf['plot_title'], fontsize=self.conf['title_size'])

        # save the plot

        plt.savefig(path_img + output_name + file_type)
        plt.show()

    # def conf_setting(self, key, value):
    #     self.conf_set.update(key / value)

    def bubble_plot(self, file, path=None, file_type='.pdf', path_img=None, x_col_name=None, y_col_name=None,
                    bubble_col=None, x_label='x label',
                    y_label='y label', bubble_name=None, legend_title='title', output_name='output', **kwargs):
        """Bubble chart with each bubble name and sizes 

        This function will convert the user's incoming data set into DataFrame and then draw
        the Bubble Chart using Matplotlib. The bubble chart can show x, y, the size of bubbles and the names of bubbles.
        
        To use this function, you need a dataset with four variables columns. The four variables are x_col_name,
        y_col_name, bubble_col and bubble_name. The bubble_col is the column decide bubble sizes and bubble_name 
        is will show each bubble name in the legend lables.
        
        In our example, The x_col_name is life_Expectancy, The y_col_name is Birth Rate, The bubble_col is GDP and
        bubble_name is country Name. 

        Args:
            file: file name of your data source, it support csv/excel,text. for example: 'new_file.csv'
            x_col_name: The X column name
            y_col_name: The Y column name
            bubble_col : The bubble values column
            x_label: x axis label
            y_label: y axis label
            bubble_name: The column of each bubble name, it will show each bubble name in legend lables
            legend title: customize legend lables title
            plot_title: The title of the plot
            output_name : output file name


        """
        header_list = self.data.columns.values.tolist()

        # default parameter setting

        if x_col_name is None:
            x_col_name = header_list[1]
        if y_col_name is None:
            y_col_name = header_list[2]
        if bubble_col is None:
            bubble_col = header_list[3]
        if bubble_name is None:
            bubble_name = header_list[0]
        if path is None:
            path = self.path
        if path_img is None:
            path_img = path

        conf = {
            # 'bubble_colors': [
            #     "#3d405b", "#e07a5f", "#f4f1de", "#81b29a", "#f2cc8f",
            #     "#264653", "#2a9d8f", "#e9c46a", "#f4a261", "#e76f51",
            #     '#ECE133', '#56B4E9'
            # ],
            # 'bubblesize_legend_loc': 'lower left',
            # 'bubbleszie_legend_title': 'Sizes'

        }
        conf.update(self.conf)

        # when new configuraton is set, update the original one
        conf.update(kwargs)
        ## create figure and set figure size
        fig, ax = plt.subplots(figsize=(self.conf['plotwidth'], self.conf['plotheight']))
        ## background grid setting

        self.draw_setting(conf, ax, x_label, y_label)

        # start plot

        # origin bubble data

        bubble_list = list(self.data[bubble_col])

        # scale the bubble size become smaller/bigger depend on user input, the inital setting is 50
        bubble_scale = []
        for i in range(len(bubble_list)):
            bubble_scale.append(bubble_list[i] / conf['bubble_scale'])

        # bubble colors
        # count the number of x column values and match with our bubble color list
        num_index = len(self.data[x_col_name])
        colors = conf['bubble_colors'][:num_index]
       
        # plot bubble chart
        scatter = ax.scatter(x=list(self.data[x_col_name]),
                             y=list(self.data[y_col_name]),
                             c=colors,
                             s=bubble_scale,
                             marker=conf['bubble_marker'],
                             alpha=conf['alpha'],
                             data=self.data,
                             label=colors)

        # add bubble_name into the legend 
        legend_list = list(self.data[bubble_name])

        # match the color of the label
        l = []
        for i in range(0, num_index):
            l.append(
                mpatches.Patch(color=colors[i],
                               alpha=conf['alpha'],
                               label=legend_list[i]))
        # legend
        legend1 = ax.legend(handles=l, title=legend_title, fontsize=conf['legend_size'])

        # add the second legend(bubble_sizes)
        ax.add_artist(legend1)

        # create the handles and labels for the bubble sizes legend
        handles, labels = scatter.legend_elements(prop="sizes",
                                                  alpha=conf['alpha'])

        # scale back the origin data into the legend labels
        kw = dict(prop="sizes", func=lambda s: s * conf['bubble_scale'])

        # bubble sizes legend add into the plot
        legend2 = ax.legend(*scatter.legend_elements(**kw),
                            loc=conf['bubblesize_legend_loc'],
                            title=conf['bubbleszie_legend_title'],
                            fontsize=conf['legend_size'])

        self.pic_save(conf, path_img, output_name, file_type)

    def bubble_category(self, file, path=None, file_type='.pdf', path_img=None, x_col_name=None, y_col_name=None,
                        bubble_col=None,
                        x_label='x label', y_label='y label', category_col=None, output_name='output', **kwargs):

        """Bubble chart with different category

         This function will convert the user's incoming data set into DataFrame and then draw
         the Bubble Chart using Matplotlib. The bubble chart can show x, y, the size of bubbles and the bubble category.
         Bubble category is used for when the dataset have a column with multiple type. For example, in our example
         continent is a good category. It have Asia, Europe, Africa, Oceania and Americas. Each category will have differnt
         bubble colors and also legend for different category.

         In the example, x_col_name is life_Exp, y_col_name is population, bubble_col is gdp and the category column is
         continent.

         Args:
              file: file name of your data source, it support csv/excel,text. for example: 'new_file.csv'
              x_col_name: The X column name
              y_col_name: The Y column name
              bubble_col : The bubble values column
              category_col: The category column of bubble
              x_label: x axis label
              y_label: y axis label
              legend title: customize legend lables title
              plot_title: The title of the plot
              output_name : output file name

        """

        header_list = self.data.columns.values.tolist()

        # default parameter setting

        if x_col_name is None:
            x_col_name = header_list[1]
        if y_col_name is None:
            y_col_name = header_list[2]
        if bubble_col is None:
            bubble_col = header_list[3]
        if category_col is None:
            category_col = header_list[0]
        if path is None:
            path = self.path
        if path_img is None:
            path_img = path

        conf = {
            # 'bubble_colors': [
            #     "#3d405b", "#e07a5f", "#f4f1de", "#81b29a", "#f2cc8f",
            #     "#264653", "#2a9d8f", "#e9c46a", "#f4a261", "#e76f51",
            #     '#ECE133', '#56B4E9', "#3d405b", "#e07a5f", "#f4f1de",
            #     "#81b29a", "#f2cc8f", "#264653", "#2a9d8f", "#e9c46a",
            #     "#f4a261", "#e76f51", '#ECE133', '#56B4E9'
            # ],

        }
        conf.update(self.conf)

        # when new configuraton is set, update the original one
        conf.update(kwargs)
        # ## create figure and set figure size
        fig, ax = plt.subplots(figsize=(conf['plotwidth'], conf['plotheight']))
        # ## background grid setting
        self.draw_setting(conf, ax, x_label, y_label)
        # self.draw_setting(conf,ax,x_label,y_label)

        # Input the valid filename and return the pandas dataframe for drawing

        # origin bubble data
        bubble_list = list(self.data[bubble_col])

        # scale the bubble size become smaller
        bubble_scale = []
        for i in range(len(bubble_list)):
            bubble_scale.append(bubble_list[i] / conf['bubble_scale'])

        map_color = []
        # create the list to get the category unique value
        # Example: ['Asia' 'Europe' 'Africa' 'Americas' 'Oceania']
        category_list = self.data[category_col].unique()

        # map each category item to one color
        # {'Asia': 'r', 'Europe': 'b', 'Africa': 'y','Americas':'g','Oceania':'c'}
        map_color = dict(
            zip(category_list, conf['bubble_colors'][:len(category_list)]))

        # color for each item
        colors = self.data[category_col].map(map_color)

        # plot the bubble chart
        scatter = ax.scatter(self.data[x_col_name],
                             self.data[y_col_name],
                             s=bubble_scale,
                             color=colors,
                             label=colors,
                             alpha=self.conf['alpha'],
                             edgecolors='grey')

        # create the mptaches list to for legend
        match_color = []
        for key, value in map_color.items():
            match_color.append(mpatches.Patch(color=value, label=key))
        # crate the legend
        ax.legend(handles=match_color, fontsize=self.conf['legend_size'])

        self.pic_save(conf, path_img, output_name, file_type)

    def bubble_colormap(self, file, path=None, file_type='.pdf', path_img=None, x_col_name=None, y_col_name=None,
                        bubble_col=None,
                        x_label='x label', y_label='y label', output_name='output', **kwargs):
        """Bubble chart with colormap

        This function will convert the user's incoming data set into DataFrame and then draw
        the Bubble Chart using Matplotlib. The bubble chart can show x, y and bubbles colormap.

        In this bubble chart, the bubble size are fixed. The bubble_col values will decide the The depth
        of color of the bubbles. The colormap legend will place at the right hand side of the plot.

        Args:
            file: file name of your data source, it support csv/excel,text. for example: 'new_file.csv'
            x_col_name: The X column name
            y_col_name: The Y column name
            bubble_col : The bubble values column
            x_label: x axis label
            y_label: y axis label
            plot_title: The title of the plot
            output_name : output file name

        """

        header_list = self.data.columns.values.tolist()

        # default parameter setting

        if x_col_name is None:
            x_col_name = header_list[1]
        if y_col_name is None:
            y_col_name = header_list[2]
        if bubble_col is None:
            bubble_col = header_list[3]
        if path is None:
            path = self.path
        if path_img is None:
            path_img = path

        conf = {
            # 'bubble_size':
            #     400,
            # 'bubble_cmap':
            #     'Blues',
            # 'plot_title': '',
            # 'colorbar_labelsize': 16

        }

        conf.update(self.conf)

        # when new configuraton is set, update the original one
        conf.update(kwargs)
        ## create figure and set figure size
        fig, ax = plt.subplots(figsize=(conf['plotwidth'], conf['plotheight']))
        ## background grid setting
        self.draw_setting(conf, ax, x_label, y_label)

        # Input the valid filename and return the pandas dataframe for drawing

        # bubble chart
        plt.scatter(x=x_col_name,
                    y=y_col_name,
                    c=bubble_col,
                    s=conf['bubble_size'],
                    cmap=conf['bubble_cmap'],
                    marker=conf['bubble_marker'],
                    alpha=conf['alpha'],
                    data=self.data)

        # create the colorbar
        cbar = plt.colorbar(ax=ax)
        cbar.ax.tick_params(labelsize=conf['colorbar_labelsize'])

        self.pic_save(conf, path_img, output_name, file_type)



