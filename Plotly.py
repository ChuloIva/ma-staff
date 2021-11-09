#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import chart_studio.plotly as py
import numpy as np
import plotly.graph_objs as go

import cufflinks as cf
import seaborn as sns
import plotly.express as px
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
init_notebook_mode(connected=True)
cf.go_offline()
get_ipython().run_line_magic('matplotlib', 'inline')

trace = {"x":[1,2],"y":[1,2] }

data = [trace]
layout = {}
fig = go.Figure(data= data, layout =layout)
fig.iplot()


# py.data.experiment()


# In[ ]:




