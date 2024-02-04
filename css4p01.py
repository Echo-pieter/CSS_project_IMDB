# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 18:24:26 2024

@author: Pieter Terre'Blanche
"""

# NB the assumption made was to ignore missing entries, instead of filling them


import pandas as pd
import numpy as np


# first import the data as a data frame, note that the index column is set
# equal to the rank column, so that there is no redundant column
movie_df = pd.read_csv('movie_dataset.csv', index_col=0)

# investigate the information of the csv file 
print(movie_df.info())


'''
Accorind to the .info method there are missing values in the Revenue(Millions) 
and Metascore columns
'''


# below two copies of the dataframe are made and are cleaned differently, since
# they will be used in different questions/scenarios.




# create a copy of the dataframe where the rows are removed with missing
# Renvenue values
movie_df_non_empty_revenue = movie_df.dropna(subset=['Revenue (Millions)'])


# the data frame created above with no empty values in the Revenue (Millions)
# column will be used in Questions 2 and 3 for the financial calculations







# create a copy of the dataframe where the rows are removed with missing
# Revenue values and Metascore values

movie_df_non_empty = movie_df.dropna()


# the data frame created above will be used in Question 12 for the correlation
# between numerical feautures




#-----------------------------------------------------------------------------


# Question 1

# The loc method is used to find the title value of the row with the highest rating 
highest_rated = movie_df.loc[movie_df['Rating'].idxmax(), 'Title']


# Question 2

# the dataframe with no empty Revenue values a.k.a movie_df_non_empty_revenue
# is used with the mean function


# determine the average revenue for all the movies
avg_revenue = movie_df_non_empty_revenue['Revenue (Millions)'].mean()



# Question 3



# first filter the data frame for only movies between 2015 and 2017
movies_df_non_empty_revenue_2015_2017 = movie_df_non_empty_revenue[
                               (movie_df_non_empty_revenue['Year'] >= 2015) &
                               (movie_df_non_empty_revenue['Year'] <= 2017)]


# use the mean function 

avg_revenue_2015_2017 = movies_df_non_empty_revenue_2015_2017['Revenue (Millions)'].mean()


# Question 4

# first the data frame is filtered so that only movies released in 2016
# are included after which the len function is used to determine how much
# rows are inside the filtered data frame

movie_count_2016 = len(movie_df[movie_df['Year'] == 2016])


# Question 5

# the data frame is filtered to only contain movies directed by Christoper
# Nolan and the len function is used to count the number of rows inside
# the filtered data frame

Christoper_nolan_movies_count = len(movie_df[movie_df['Director'] == 'Christopher Nolan'])


# Question 6

# the dataframe is filtered to only include movies with a rating of 8.0 and
# above after which the number of rows in the resulting dataframe is determined

rating_count_8 = len(movie_df[movie_df['Rating'] >= 8.0])


# Question 7

# the dataframe is filtered to only include movies directed by Christoper Nolan
# next the median function is applied to the Rating column of the resulting
# dataframe

median_Chritoper_nolan_movie_rating = movie_df[movie_df['Director'] == 'Christopher Nolan']['Rating'].median()



# Question 8


# group based on the year column and then use the aggregate mean function
# to determine the mean rating per year
year_group = movie_df.groupby('Year')
average_rating_per_year = year_group['Rating'].mean()

# find the index value (year) of the entry with the highest mean value
highest_year_rating = average_rating_per_year.idxmax()



# Question 9

# filter the dataframe to only include movies made in 2006 and count the 
# number of rows in the dataframe
movie_count_2006 = len(movie_df[movie_df['Year'] == 2006])

# determine the percentage increase
percentage_increase = (movie_count_2016-movie_count_2006)/movie_count_2006*100




# Question 10

# extract the column of actors names
actors_col = movie_df['Actors']

# split the actor names into a new dataframe
actors_split = actors_col.str.split(',', expand=True)

# convert the dataframe to a numpy matrix
actors_split_matrix = actors_split.to_numpy()

# make the numpy matrix a 1D array
actors_split_array = actors_split_matrix.flatten()

# remove any empty entries from the actors array
actors_split_array = actors_split_array[actors_split_array != np.array(None)]

# convert the numpy array to a Pandas series
actors_series = pd.Series(actors_split_array)

# remove any spaces before and after the names of the actors
actors_series = actors_series.str.strip()

# determine the number of times the actor names appear
actors_count = actors_series.value_counts()



# Question 11

# extract the column with the movie genres
genres_column = movie_df['Genre']

# split the genres into a new dataframe
genres_split = genres_column.str.split(',', expand=True)

# convert the dataframe to a numpy matrix
genres_matrix = genres_split.to_numpy()

# convert the matrix to a 1D array
genres_array = genres_matrix.flatten()

# remove the None entries from teh array
genres_array = genres_array[genres_array != np.array(None)]

# convert the array into a Pandas series
genres_series = pd.Series(genres_array)

# remove the spaces before and after the entries in the series
genres_series = genres_series.str.strip()

# determine the number of unique genres
genres_unique = genres_series.unique()

# count the number of unique genres
genres_unique_count = len(genres_unique)






# Question 12

# use the pandas corr funciton to determine the correlation between the
# numerical features

# do a correlation between the numerical features
num_features_corr = movie_df_non_empty.corr(numeric_only=True)




# see the average numerical values for the different categories
column_names = ['Genre', 'Runtime (Minutes)', 'Rating', 'Votes', 'Revenue (Millions)', 'Metascore']
avg_num_vals_categories = pd.DataFrame(columns=column_names)


# use a loop to iterate over the different genres

for genre in genres_unique:
    genre_group = movie_df_non_empty[movie_df_non_empty['Genre'].str.contains(genre)]
    genre_group_avg = genre_group[['Runtime (Minutes)','Rating', 'Votes', 'Revenue (Millions)', 'Metascore']].mean()
    genre_group_avg = genre_group_avg[::-1]
    genre_group_avg['Genre'] = genre
    genre_group_avg = genre_group_avg[::-1]
    
    avg_num_vals_categories.loc[len(avg_num_vals_categories.index)] = genre_group_avg
    
    
    
    
    















