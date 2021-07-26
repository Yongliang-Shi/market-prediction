# General Library
import numpy as np
import pandas as pd

# 
import pandas_datareader.data as web

# Create the functions to download the stock

def acquire_stock_adjclosing(stocks, start_date, end_date, source='yahoo'):
    '''
    Return the adjusted closing prices of the interested stocks.
    Parameters: 
        - stocks(list): a list of the stock symbols
        - start_date(str): the start date in standard format
        - end_date(str): the end date in standard format
        - source(str): specify where the data is downloaded and the default source is yahoo finance
    '''
    df_adjclosing = web.DataReader(stocks, data_source=source, start=start_date, end=end_date)['Adj Close']
    df_adjclosing.columns = stocks
    return df_adjclosing

def load_jane_street_train():
    '''
    Return a dataframe that contains 
    '''
    # Load the train dataset by default
    df_train = pd.read_csv("Database/train.csv")
    # Create an iterator containing the names of the float64 columns
    colsf64 = df_train.select_dtypes(include='float64').columns
    # Create an iterator containing the names of the int64 columns
    colsi64 = df_train.select_dtypes(include='int64').columns
    # Create the dictionary to define the dtypes of the columns
    mapperf32 = {col: np.float32 for col in colsf64}
    mapperi32 = {col: np.int32 for col in colsi64}
    # Cast the df_train to the defined dtypes
    df_train = df_train.astype(mapperf32)
    df_train = df_train.astype(mapperi32)
    return df_train
