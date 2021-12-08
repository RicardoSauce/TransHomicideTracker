#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Ricardo Saucedo
#PPHA 30536: Data and Public Policy II 
#Observing Transgender Homicide Rates in the U.S. and inherent links to state
#voting history in presidential elections.
 

#load in imports
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd#https://geopandas.org/mapping.html
from mpl_toolkits.axes_grid1 import make_axes_locatable
from urllib.request import urlopen
import json
import us




#do file loading processes
path = os.getcwd()
state_names = us.states.mapping('abbr','name')
def load_parse_Data(path):
    trans_homicide= pd.read_csv(os.path.join(path, 'Trans_Homicide_2020_copy.csv'), engine = 'python', skipinitialspace=True) 
    trans_homicide['city'], trans_homicide['state'] = trans_homicide['City, State'].str.split(',',1).str
    return trans_homicide


# In[ ]:





# In[9]:


# Load in my 2020 data
state_names = us.states.mapping('abbr','name')
trans_homicide = load_parse_Data(path)
trans_homicide = trans_homicide.drop('City, State', axis = 1)
trans_homicide['state'] = trans_homicide['state'].str.replace('Puerto Rico','PR')
trans_homicide.columns = ['year','Name','city','state']
trans_homicide = trans_homicide.set_index('year')
for k,v in state_names.items():
    trans_homicide['state'] = trans_homicide['state'].replace(k,v, regex=True)

#create counts per each state
counts_per_state_2020 = trans_homicide.groupby('state').size()
counts_2020 = pd.DataFrame(counts_per_state_2020).reset_index()
counts_2020.columns = ['NAME', 'count']
counts_2020['state'] = counts_2020.NAME
state_list = list(counts_2020.state)
cleaned_state = []
for i in state_list:
    clean = i.lstrip()
    cleaned_state.append(clean)
print(cleaned_state)




#prepare geospatial data
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
na = world.loc[(world['name'] == 'United States of America') | (world['name'] == 'Puerto Rico')]
#download US states
url = 'https://eric.clst.org/assets/wiki/uploads/Stuff/gz_2010_us_040_00_500k.json'
states = gpd.read_file(url)
print(states)



test = states.loc[states['NAME'].isin(['Arkansas', 'California', 'Colorado', 'Florida', 'Illinois', 'Louisiana', 'Maryland', 'Missouri', 'New York', 'North Carolina', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Puerto Rico', 'Texas', 'Washington'])]
test = test.sort_values(by='NAME')
print(test)




#drop states that did not have any record in their year
#states = states.loc[states['NAME'].isin(state_list)]
print(states)




# recreate choropleth map of the united states

fig, ax = plt.subplots(figsize=(16,16))
na.plot(ax=ax, color ='white', edgecolor='black')
#world['world_pop_share'] = world['pop_est'] / sum(world['pop_est'])

#call on axis
divider = make_axes_locatable(ax)
#color mark
#size it to the right, 5%, 
cax = divider.append_axes('right', size='5%', pad=0.1)
    
ax = states.plot(ax=ax, column='counts', legend=True, cax=cax)

ax.axis('off')
ax.set_title('US Transgender Homicides in 2020');






