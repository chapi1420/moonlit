import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import plotly.express as px
import plotly.graph_objects as go
import datetime

#data is innitially loaded into pandas DataFrame
def load(data_path):
    df = pd.read_csv(data_path)
    #timestamp data type changed
    df['Timestamp'] = pd.to_datetime(df['Timestamp'])
    return df

def data_summary(data):
    df = load(data)
    numerics = df.select_dtypes(include=[np.number].columns)
    return df[numerics].describe()


















