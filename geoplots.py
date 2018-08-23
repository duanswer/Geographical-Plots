# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 10:09:38 2018

@author: Eduardo Answer <eduardonzinga111@hotmail.com>
"""

try:
    import numpy as np
except ImportError:
    print("Numpy is not installed")
    
print (np.__version__)

import plotly.plotly as py
import plotly.graph_objs as go
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot

init_notebook_mode(connected=True)

#import cufflinks as cf
import pandas as pd

data = dict(type = 'choropleth', 
            locations =['AZ', 'CA', 'NY'], 
            locationmode = 'USA-states',
            colorscale = 'Portland',
            text = ['Estado1', 'Estado2', 'Estado3'],
            z = [1.0, 2.0, 3.0],
            colorbar = {'title': 'Título'})

layout = dict(geo = {'scope': 'usa'})

choromap = go.Figure(data=[data], layout = layout)

plot(choromap)


df.iplot(kind='surface', colorscale='rgb')

