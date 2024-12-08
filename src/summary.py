import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import plotly.express as px
import plotly.graph_objects as go
import datetime
import sys
import os


def load(data_path):
    '''loads the data into a DataFramme and changes timestamp datatype
        if the input is DataFrame, it returns it direcly
        If the input is a file path, it reads the file into a DataFrame'''
    if isinstance(data_path, pd.DataFrame):
        df['Timestamp'] = pd.to_datetime(df['Timestamp'])
        return data_path
    elif isinstance(data_path, str):
        df = pd.read_csv(data_path)
        df['Timestamp'] = pd.to_datetime(df['Timestamp'])  
    else: 
        raise ValueError("input should be DataFrame or a file path(string).")
    return df

def data_summary(data):
    '''sumarizes data by providing the mean, mode, median and 
    std alues with counts of non-null entries in each column'''
    df = load(data)
    numerics = df.select_dtypes(include=[np.number].columns)
    return df[numerics].describe()
    

















