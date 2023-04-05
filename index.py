# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 07:30:29 2023
@author: praveen
"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

def read_my_excel(filename):
    """ This function is used to read excel file and return dataframe """
    excel_result = pd.read_excel(filename)
    return excel_result

def  get_years_countries(dataframe):
    # Split the DataFrame into two separate DataFrames, one with years and another with countries
    df_countries = dataframe.iloc[1:, 0:1]  # select the first column containing years
    df_years =   dataframe.iloc[:, 4:]  # select all columns starting from 4th column
    return df_countries,df_years

def filter_desired_columns(dataframe_name,column_names):
    """ This function is used to filter the desired columns"""
    return dataframe_name.loc[:, column_names]

def filter_desired_rows(dataframe_name,row_locations):
    """ This function is used to filter the desired rows and rounding data  to 4 figures """
    return dataframe_name.iloc[row_locations].round(4)

def fill_missing_val(dataframe_name,colname):
    """ This function is used to fill missing values with it's mean value """
    dataframe_name[colname].fillna(dataframe_name[colname].mean(), inplace=True)

def plot_bar_chart(dataframe,index_name,title,xlabel,ylabel):
    """ This function is used to plot bar chart """
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
df_mortality = read_my_excel("mortality_rate_updated.xls")
df_electricity = read_my_excel("electricity_access.xls")

#one with years and another with countries
country_df,years_df = get_years_countries(df_forest)
#check first 5 rows
#print(df_forest.head())
#print(df_co2emission.head())
#using describe method try to analyze the whole statistical data
print(df_forest.describe())
print(df_co2emission.describe())
print(df_mortality.describe())
print(df_electricity.describe())

#keep only desired columns
df_forest = filter_desired_columns(df_forest,['Country Name', 'Country Code', '1991', '1995', '1999'])
df_co2emission = filter_desired_columns(df_co2emission,['Country Name', 'Country Code', '1991', '1995', '1999'])
df_mortality = filter_desired_columns(df_mortality,['Country Name', 'Country Code', '1991', '1995', '1999'])
df_electricity = filter_desired_columns(df_electricity,['Country Name', 'Country Code', '1991', '1995', '1999'])

# read forest data  only for few countries  
df_forest_specific_rows = filter_desired_rows(df_forest,[4,13,17, 29])

# read co2 emmsion only for few countries 
df_emmision_specific_rows = filter_desired_rows(df_co2emission,[4,13,17, 29])

# read mortality only for few countries 
df_mortality_specific_rows = filter_desired_rows(df_mortality,[4,13,17, 29])

# read electricity only for few countries 
df_electricity_specific_rows = filter_desired_rows(df_electricity,[4,13,17, 29])

#cleanup empty values with 0
df_electricity_specific_rows.fillna(0, inplace=True)

# fill missing values with column mean
fill_missing_val(df_forest,'1991')
fill_missing_val(df_forest,'1995')
fill_missing_val(df_forest,'1999')

fill_missing_val(df_co2emission,'1991')
fill_missing_val(df_co2emission,'1995')
fill_missing_val(df_co2emission,'1999')

fill_missing_val(df_mortality,'1991')
fill_missing_val(df_mortality,'1995')
fill_missing_val(df_mortality,'1999')

#display barchart for forest area data
plot_bar_chart(df_forest_specific_rows,'Country Name','Forest Area by Country and Year','Country and Year','Forest area (% of land area)')

#display barchart for co2 emission data
plot_bar_chart(df_emmision_specific_rows,'Country Name','CO2 Emission by Country and Year','Country and Year','CO2 emissions (kt)')

#co2 vs forest
def plot_scatter(year,dataframe_1,dataframe2):
    # create a scatterplot between CO2 emission and forest land
    sns.scatterplot(x=dataframe_1[year], y=dataframe2[year])
    # calculate the correlation coefficient and p-value
    corr, p_value = pearsonr(dataframe_1[year], dataframe2[year])
    print('Correlation coefficient:', corr)
    print('p-value:', p_value)

#call scatter
plot_scatter('1991',df_co2emission,df_forest)
plot_scatter('1991',df_mortality_specific_rows,df_electricity_specific_rows)







