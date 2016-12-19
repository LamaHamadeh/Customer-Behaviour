# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 12:58:32 2016

@author: ADB3HAMADL
"""

"""
Created on Fri Dec 16 13:01:27 2016
Author: Lama Hamadeh
Software: I use Spyder 3.0.2 (Python 3.5) to write the following code
The aim: Analyse the data and look for the behavioural differences between investors and non-investors
The Question:
We have attached a small subset of data from our front end events database. Dataset focuses on behavioural activity before 
user makes their first investment. Each of the lines is a distinct user's behaviour before making the first investment. 
You will note that not everyone from this dataset made the first investment. What we would like you to do is to analyse 
the data and look for the behavioural differences between investors and non-investors.
"""

#---------------------------------------------------------
#Import the necessary modules and packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn.cluster import KMeans
import matplotlib
matplotlib.style.use('ggplot')
#---------------------------------------------------------

#Import the dataset from the csv file
df=pd.read_csv('/Users/ADB3HAMADL/Desktop/Anaconda_Packages/user_to_1st_time_investor/user to 1st time investor.csv')
df.dropna(axis = 0, how = 'any', inplace = True)

#print(df) #take a look at the dataset

# The dataset focuses on behavioural activity before users make their first investment

#print(df.dtypes) #check the types of the dataset features

print(len(df))  #The whole dataset contains an overall 263501 customers
#---------------------------------------------------------

#Create a slice called df_investor that filters to only include the investors dataset records 
df_investor = df[(df.investor_status == 'investor')]
                 
print(len(df_investor)) #The dataset contains 1359 investors

print(df_investor.head())
print(df_investor.describe())
print(df_investor.dtypes)

#Make anther filter to the investor dataset slice where it contains only the 'time' values related to investors customers.
df_investor.drop(['guid','investor_status','time_to_sign_up_from_first_visit_days','first_visit_to_first_investment_days',
'distinct_days_visited_website','distinct_properties_viewed','interactions_on_property_page','dashboard_interactions'],inplace=True,axis=1)
print(df_investor.dtypes)
print(df_investor.plot.hist())
#---------------------------------------------------------

# Remove top 5 and bottom 5 samples for each column:
drop = {}
for col in df_investor.columns:
  # Bottom 5
  sort = df_investor.sort_values(by=col, ascending=True)
  if len(sort) > 5: sort=sort[:5]
  for index in sort.index: drop[index] = True # Just store the index once

  # Top 5
  sort = df_investor.sort_values(by=col, ascending=False)
  if len(sort) > 5: sort=sort[:5]
  for index in sort.index: drop[index] = True # Just store the index once

print(len(df_investor))

print "Dropping {0} Outliers...".format(len(drop))
df_investor.drop(inplace=True, labels=drop.keys(), axis=0)
print df_investor.describe()

#---------------------------------------------------------
T = preprocessing.MinMaxScaler().fit_transform(df_investor)

def doKMeans(data, clusters=0):
  #
  # Do the KMeans clustering here, passing in the # of clusters parameter
  # and fit it against your data. Then, return a tuple containing the cluster
  # centers and the labels
  #
  # .. your code here ..
  model = KMeans(n_clusters=clusters)
  labels = model.fit_predict(data)
  return model.cluster_centers_, model.labels_

# Do KMeans
n_clusters = 3
centroids, labels = doKMeans(T, n_clusters)

# Print out your centroids. They're currently in feature-space, which
# is good. 
print centroids

#---------------------------------------------------------
 # Do PCA *after* to visualize the results. Project the centroids as well as 
# the samples into the new 2D feature space for visualization purposes.

def doPCA(data, dimensions=2):
  from sklearn.decomposition import RandomizedPCA
  model = RandomizedPCA(n_components=dimensions)
  model.fit(data)
  return model

display_pca = doPCA(T)
T = display_pca.transform(T)
CC = display_pca.transform(centroids)
#---------------------------------------------------------
# Visualize all the samples. Give them the color of their cluster label

# TODO: Parameters to play around with
PLOT_TYPE_TEXT = False    # If you'd like to see indices
PLOT_VECTORS = True       # If you'd like to see your original features in P.C.-Space


matplotlib.style.use('ggplot') # Look Pretty
c = ['red', 'green', 'blue', 'orange', 'yellow', 'brown']

def drawVectors(transformed_features, components_, columns, plt):
  num_columns = len(columns)

  # This function will project your *original* feature (columns)
  # onto your principal component feature-space, so that you can
  # visualize how "important" each one was in the
  # multi-dimensional scaling
  
  # Scale the principal components by the max value in
  # the transformed set belonging to that component
  xvector = components_[0] * max(transformed_features[:,0])
  yvector = components_[1] * max(transformed_features[:,1])

  ## Visualize projections

  # Sort each column by its length. These are your *original*
  # columns, not the principal components.
  import math
  important_features = { columns[i] : math.sqrt(xvector[i]**2 + yvector[i]**2) for i in range(num_columns) }
  important_features = sorted(zip(important_features.values(), important_features.keys()), reverse=True)
  print "Projected Features by importance:\n", important_features

  ax = plt.axes()

  for i in range(num_columns):
    # Use an arrow to project each original feature as a
    # labeled vector on your principal component axes
    plt.arrow(0, 0, xvector[i], yvector[i], color='b', width=0.0005, head_width=0.02, alpha=0.75, zorder=600000)
    plt.text(xvector[i]*1.2, yvector[i]*1.2, list(columns)[i], color='b', alpha=0.75, zorder=600000)
  return ax
  
  
  
fig = plt.figure()
ax = fig.add_subplot(111)
if PLOT_TYPE_TEXT:
  # Plot the index of the sample, so you can further investigate it in your dset
  for i in range(len(T)): ax.text(T[i,0], T[i,1], df.index[i], color=c[labels[i]], alpha=0.75, zorder=600000)
  ax.set_xlim(min(T[:,0])*1.2, max(T[:,0])*1.2)
  ax.set_ylim(min(T[:,1])*1.2, max(T[:,1])*1.2)
else:
  # Plot a regular scatter plot
  sample_colors = [ c[labels[i]] for i in range(len(T)) ]
  ax.scatter(T[:, 0], T[:, 1], c=sample_colors, marker='o', alpha=0.2)


# Plot the Centroids as X's, and label them
ax.scatter(CC[:, 0], CC[:, 1], marker='x', s=169, linewidths=3, zorder=1000, c=c)
for i in range(len(centroids)): ax.text(CC[i, 0], CC[i, 1], str(i), zorder=500010, fontsize=18, color=c[i])


# Display feature vectors for investigation:
if PLOT_VECTORS: drawVectors(T, display_pca.components_, df_investor.columns, plt)


# Add the cluster label back into the dataframe and display it:
df_investor['label'] = pd.Series(labels, index=df_investor.index)
print df_investor
#--------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------

#Create a slice called df_non_investor that filters to only include the non investors dataset records 
df_non_investor = df[(df.investor_status == 'non-investor')]
                 
print(len(df_non_investor)) #The dataset contains 1359 investors

print(df_non_investor.head())
print(df_non_investor.describe())
print(df_non_investor.dtypes)

#Make anther filter to the investor dataset slice where it contains only the 'time' values related to investors customers.
df_non_investor.drop(['guid','investor_status','time_to_sign_up_from_first_visit_days','first_visit_to_first_investment_days',
'distinct_days_visited_website','distinct_properties_viewed','interactions_on_property_page','dashboard_interactions'],inplace=True,axis=1)
print(df_non_investor.dtypes)
print(df_non_investor.plot.hist())
#---------------------------------------------------------

# Remove top 5 and bottom 5 samples for each column:
drop = {}
for col in df_non_investor.columns:
  # Bottom 5
  sort = df_non_investor.sort_values(by=col, ascending=True)
  if len(sort) > 5: sort=sort[:5]
  for index in sort.index: drop[index] = True # Just store the index once

  # Top 5
  sort = df_non_investor.sort_values(by=col, ascending=False)
  if len(sort) > 5: sort=sort[:5]
  for index in sort.index: drop[index] = True # Just store the index once

print(len(df_non_investor))

print "Dropping {0} Outliers...".format(len(drop))
df_non_investor.drop(inplace=True, labels=drop.keys(), axis=0)
print df_non_investor.describe()

#---------------------------------------------------------
T = preprocessing.MinMaxScaler().fit_transform(df_non_investor)

def doKMeans(data, clusters=0):
  #
  # Do the KMeans clustering here, passing in the # of clusters parameter
  # and fit it against your data. Then, return a tuple containing the cluster
  # centers and the labels
  #
  # .. your code here ..
  model = KMeans(n_clusters=clusters)
  labels = model.fit_predict(data)
  return model.cluster_centers_, model.labels_

# Do KMeans
n_clusters = 3
centroids, labels = doKMeans(T, n_clusters)

# Print out your centroids. They're currently in feature-space, which
# is good. 
print centroids

#---------------------------------------------------------
 # Do PCA *after* to visualize the results. Project the centroids as well as 
# the samples into the new 2D feature space for visualization purposes.

def doPCA(data, dimensions=2):
  from sklearn.decomposition import RandomizedPCA
  model = RandomizedPCA(n_components=dimensions)
  model.fit(data)
  return model

display_pca = doPCA(T)
T = display_pca.transform(T)
CC = display_pca.transform(centroids)
#---------------------------------------------------------
# Visualize all the samples. Give them the color of their cluster label

# TODO: Parameters to play around with
PLOT_TYPE_TEXT = False    # If you'd like to see indices
PLOT_VECTORS = True       # If you'd like to see your original features in P.C.-Space


matplotlib.style.use('ggplot') # Look Pretty
c = ['red', 'green', 'blue', 'orange', 'yellow', 'brown']

def drawVectors(transformed_features, components_, columns, plt):
  num_columns = len(columns)

  # This function will project your *original* feature (columns)
  # onto your principal component feature-space, so that you can
  # visualize how "important" each one was in the
  # multi-dimensional scaling
  
  # Scale the principal components by the max value in
  # the transformed set belonging to that component
  xvector = components_[0] * max(transformed_features[:,0])
  yvector = components_[1] * max(transformed_features[:,1])

  ## Visualize projections

  # Sort each column by its length. These are your *original*
  # columns, not the principal components.
  import math
  important_features = { columns[i] : math.sqrt(xvector[i]**2 + yvector[i]**2) for i in range(num_columns) }
  important_features = sorted(zip(important_features.values(), important_features.keys()), reverse=True)
  print "Projected Features by importance:\n", important_features

  ax = plt.axes()

  for i in range(num_columns):
    # Use an arrow to project each original feature as a
    # labeled vector on your principal component axes
    plt.arrow(0, 0, xvector[i], yvector[i], color='b', width=0.0005, head_width=0.02, alpha=0.75, zorder=600000)
    plt.text(xvector[i]*1.2, yvector[i]*1.2, list(columns)[i], color='b', alpha=0.75, zorder=600000)
  return ax
  
  
  
fig = plt.figure()
ax = fig.add_subplot(111)
if PLOT_TYPE_TEXT:
  # Plot the index of the sample, so you can further investigate it in your dset
  for i in range(len(T)): ax.text(T[i,0], T[i,1], df.index[i], color=c[labels[i]], alpha=0.75, zorder=600000)
  ax.set_xlim(min(T[:,0])*1.2, max(T[:,0])*1.2)
  ax.set_ylim(min(T[:,1])*1.2, max(T[:,1])*1.2)
else:
  # Plot a regular scatter plot
  sample_colors = [ c[labels[i]] for i in range(len(T)) ]
  ax.scatter(T[:, 0], T[:, 1], c=sample_colors, marker='o', alpha=0.2)


# Plot the Centroids as X's, and label them
ax.scatter(CC[:, 0], CC[:, 1], marker='x', s=169, linewidths=3, zorder=1000, c=c)
for i in range(len(centroids)): ax.text(CC[i, 0], CC[i, 1], str(i), zorder=500010, fontsize=18, color=c[i])


# Display feature vectors for investigation:
if PLOT_VECTORS: drawVectors(T, display_pca.components_, df_non_investor.columns, plt)


# Add the cluster label back into the dataframe and display it:
df_non_investor['label'] = pd.Series(labels, index=df_non_investor.index)
print df_non_investor


#---------------------------------------------------------

plt.show()






