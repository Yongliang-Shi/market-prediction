# General libraries
import numpy as np
import pandas as pd

# Datetime library
from datetime import date

# Environment File
import env

# Database path
database = env.database


def combine_usexchanges():
    '''
    This function combines the general information of all stocks 
    from NASDAQ, NYSE, and AMEX stock exchanges, saves it as csv file
    and return it as a pandas dataframe
    '''
    # save today's date as a string format mmddyy
    today = date.today().strftime("%m%d%y")
    
    # Read the general information of all stocks from NYSE, NASDAQ, and AMEX
    nyse = pd.read_csv(f"{database}nyse_stocks_{today}.csv")
    nasdaq = pd.read_csv(f"{database}nasdaq_stocks_{today}.csv")
    amex = pd.read_csv(f"{database}amex_stocks_{today}.csv")
    
    # Add new columns to indicate where the stock is listed
    nyse = nyse.assign(stock_exchange = 'NYSE')    
    nasdaq = nasdaq.assign(stock_exchange = 'NASDAQ')    
    amex = amex.assign(stock_exchange = 'AMEX')
    
    # Combine the stocks from all three exchanges
    df = pd.concat([nyse, nasdaq, amex])
    
    # Save as the csv file
    df.to_csv(f"{database}usstockexchanges_{today}.csv")
    
    # Return the dataframe
    return df

def clean_daily_portfolio_adjustments(df):
    '''
    The function takes the daily portfolio adjustments made by the ARK investment team
    and return the clean table. 
    '''
    # Drop the null values
    df = df.drop([0,1])
    df = df.drop(columns='Unnamed: 8')
    
    # Rename the columns
    col_names = list(df.iloc[0].str.lower().values)
    df.columns = col_names
    
    # Delete the redundant row
    df = df.drop([2])
    
    # Reset the index
    df = df.reset_index()
    df = df.drop(columns='index')
    
    return df
