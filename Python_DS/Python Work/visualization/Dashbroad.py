#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 16:20:45 2017

@author: ranjeetapegu
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
#%matplotlib inline
import warnings
warnings.filterwarnings('ignore')
Movies =pd.read_csv("/Users/ranjeetapegu/Documents/python/dataset/Python Visualisation/Movie-Ratings.csv")
len(Movies)
Movies.columns=["Film","Genre","CriticRating","AudienceRating","BudgetMillions","Year"]

#Movies.Film = Movies.Film.astype('categorgy')
Movies.Year = Movies.Year.astype('category')
Movies.Genre = Movies.Genre.astype('category')

sns.set_style('white', {'axes.facecolor':'black'})
f, ax = plt.subplots(2,2,figsize=(10,10))
#plot 1
f1 =sns.violinplot(Movies.Year, Movies.CriticRating,ax=ax[0,0], palette = 'YlOrRd')

#plot 2
f2= sns.kdeplot(Movies.CriticRating, Movies.AudienceRating, 
                shade_lowest=False,shade=True,cmap='Blues_r', ax=ax[0,1])
f2b= sns.kdeplot(Movies.CriticRating, Movies.AudienceRating, 
                cmap='gray_r', ax=ax[0,1])

#plot 3
f3 = sns.kdeplot( Movies.BudgetMillions,Movies.CriticRating, ax=ax[1,0], shade=True,\
                 Shade_lowest=True, cmap='inferno')
f3b = sns.kdeplot( Movies.BudgetMillions,Movies.CriticRating, ax=ax[1,0],cmap='cool')
#plot 4

f4= sns.kdeplot( Movies.BudgetMillions,Movies.AudienceRating, ax= ax[1,1],shade=True,\
                 Shade_lowest=True, cmap='inferno')
f4b = sns.kdeplot( Movies.BudgetMillions,Movies.AudienceRating, ax=ax[1,1],cmap='cool')


f3.set(ylim=(-20,150))
f4.set(ylim=(-20,150))