import csv
import numpy as np
import chart_studio.plotly as py
import plotly.graph_objs as go
import chart_studio
import pandas as pd
chart_studio.tools.set_credentials_file(username='Fake.Username',api_key='55555')
csv_file = "univ_reduced.csv"
#df is out pandas dataframe
df = pd.read_csv(csv_file)
df = df[df.SAT_AVG_ALL.notnull()]
df = df[df.INSTNM.notnull()]
df = df[df.UGDS_WHITE.notnull()]
df = df[df.MD_EARN_WNE_P10.notnull()]
df = df[~df.MD_EARN_WNE_P10.str.contains('PrivacySuppressed')]
name = df['INSTNM'].values
sat_average = df['SAT_AVG_ALL'].values
salary = df['MD_EARN_WNE_P10'].values
percentage_white = df['UGDS_WHITE'].values
trace1 = go.Scatter3d(
    x=sat_average,
    y=salary,
    z=percentage_white,
    text=name,
    mode='markers',
    marker=dict(
        size=4,
        color=percentage_white, # set color to an array/list of desired values
        colorscale='Viridis',   # choose a colorscale
        opacity=0.8
    )
)
my_data = [trace1]
my_layout = go.Layout(
    title='University Data',
    scene=dict(
        xaxis=dict(
            title='SAT Average'
        ),
        yaxis=dict(
            title='Average Salary'
        ),
        zaxis=dict(
            title='Percentage White'
        )
    )
)
fig = go.Figure(data=my_data, layout=my_layout)
py.plot(fig, filename='univ_vis') #if using a text editor call py.plot(fig, filename='univ_vis')
#https://drive.google.com/drive/folders/1WCZQmB_dAHCr4lHE027qEcvMTPLchs8D?usp=sharing
