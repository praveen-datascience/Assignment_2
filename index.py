
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 07:30:29 2023
@author: praveen
"""
import pandas as pd
import matplotlib.pyplot as plt

def read_my_excel(filename):
     """ This function is used to read excel file and return dataframe"""
    excel_result = pd.read_excel(filename)
    return excel_result

def filter_desired_columns(dataframe_name,column_names):
    """ This function is used to filter the desired columns"""
    return dataframe_name.loc[:, column_names]

def filter_desired_rows(dataframe_name,row_locations):
    """ This function is used to filter the desired rows and rounding data  to 4 figures"""
    return dataframe_name.iloc[row_locations].round(4)

def plot_bar_chart(dataframe,index_name,title,xlabel,ylabel):
    """ This function is used to plot bar chart"""
    # set the index of the dataframe to 'Country Name' column
    dataframe = dataframe.set_index(index_name)
    # plot the bar chart
    ax = dataframe.plot(kind='bar', figsize=(10,6))
    # set the title
    ax.set_title(title)
    # set the x label
    ax.set_xlabel(xlabel)
    # set the y label
    ax.set_ylabel(ylabel)
    # Move the legend to the top right corner
    ax.legend(loc='upper right')
    # Reorder the legend entries so that the years appear in ascending order
    handles, labels = ax.get_legend_handles_labels()
    ax.legend(reversed(handles), reversed(labels), loc='upper right')
    # show the plot
    plt.show()

#read csv file
df_forest = read_my_excel("forest_area_updated.xls")
df_co2emission = read_my_excel("co2_emission_updated.xls")

#check first 5 rows
#print(df_forest.head())
#print(df_co2emission.head())

#using describe method try to analyze the whole statistical data
print(df_forest.describe())
print(df_co2emission.describe())

#keep only desired columns
df_forest = filter_desired_columns(df_forest,['Country Name', 'Country Code', '1991', '1995', '1999'])
df_co2emission = filter_desired_columns(df_co2emission,['Country Name', 'Country Code', '1991', '1995', '1999'])

# read forest data  only 1 African country, Australiya, Asian country and South American country 
df_forest_specific_rows = filter_desired_rows(df_forest,[4,13,17, 29])

# read co2 emmsion only 1 African country, Australiya, Asian country and South American country 
df_emmision_specific_rows = filter_desired_rows(df_co2emission,[4,13,17, 29])

#display barchart for forest area data
plot_bar_chart(df_forest_specific_rows,'Country Name','Forest Area by Country and Year','Country and Year','Forest area (% of land area)')

#display barchart for co2 emission data
plot_bar_chart(df_emmision_specific_rows,'Country Name','CO2 Emission by Country and Year','Country and Year','CO2 emissions (kt)')


