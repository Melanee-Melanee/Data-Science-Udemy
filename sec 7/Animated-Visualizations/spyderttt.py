# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 16:28:17 2021

@author: sony
"""
import pandas as pd
import plotly.express as px
import plotly.offline as py
from bubbly.bubbly import bubbleplot
data = px.data.gapminder()
data.head()
import warnings
warnings.filterwarnings('ignore')

figure = bubbleplot(dataset = data,
                    y_column = 'gdpPercap',
                    x_column = 'lifeExp', 
                    bubble_column = 'continent',
                    time_column = 'year',
                    size_column = 'pop',
                    color_column = 'continent',
    title = 'Life Expectancy vs GDP',
    y_logscale = True,
    scale_bubble = 5,
    height = 650)
py.iplot(figure, config={'scrollzoom': True})