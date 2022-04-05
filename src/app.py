'''
    File name: app.py
    Authors:
        Julien Aubuchon (1954203)
        Marc Bussière (1959434)
        Jean-Sébastien Patenaude (1961302)
        Ava Tingaud (2179192)
        Jeanne Tremblay (1855923)

    Course: INF8808
    Python Version: 3.8
'''

import dash
import dash_html_components as html
import pandas as pd
import bubble_chart

df = pd.read_csv('../data/data.csv')

df_short = df.head(1000)
bubble_chart.get_bubble_figure(df_short)

df_most_followers = df

app = dash.Dash(__name__)
app.title = 'Projet | INF8808'


app.layout = html.Div(className='content', children=[
    html.Header(children=[
        html.H1('Hello World'),
    ]),
    # html.Main(className='viz-container', children=[
    #     dcc.Graph(className='graph', figure=fig, config=dict(
    #         scrollZoom=False,
    #         showTips=False,
    #         showAxisDragHandles=False,
    #         doubleClick=False,
    #         displayModeBar=False
    #         ))
    # ])
])
