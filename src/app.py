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

from dash import Dash, dcc, html, Input, Output, callback_context

import pandas as pd

import bubble_chart
import heatmap
import scatter
import histogram

df = pd.read_csv('../data/data.csv')

df_short = df.head(1000)

df_most_followers = df

app = Dash(__name__)
app.title = 'Projet | INF8808'


app.layout = html.Div(className='content', children=[
    html.Header(children=[
        html.H1('Hello World'),
    ]),
    html.Main(className='viz-container', children=[
        html.Div(className='selector-buttons', children=[
            html.Button('Bubble', id='bubble-button'),
            html.Button('Heatmap', id='heatmap-button'),
            html.Button('Scatter', id='scatter-button'),
            html.Button('Histogram', id='histogram-button'),
        ]),
        html.Div(id='bubble-div', style={'display': 'block'}, children=[
            html.H1('Bubble'),
            dcc.Graph(className='bubble-chart', figure=histogram.get_histogram_figure(), config=dict(
                scrollZoom=False,
                showTips=False,
                showAxisDragHandles=False,
                doubleClick=False,
                displayModeBar=False
                )
            )
        ]),
        html.Div(id='heatmap-div', style={'display': 'none'}, children=[
            html.H1('Heatmap'),
            dcc.Graph(className='heatmap-chart', figure=None, config=dict(
                scrollZoom=False,
                showTips=False,
                showAxisDragHandles=False,
                doubleClick=False,
                displayModeBar=False
                )
            )
        ]),
        html.Div(id='scatter-div', style={'display': 'none'}, children=[
            html.H1('Scatter'),
            dcc.Graph(className='scatter-chart', figure=None, config=dict(
                scrollZoom=False,
                showTips=False,
                showAxisDragHandles=False,
                doubleClick=False,
                displayModeBar=False
                )
            )
        ]),
        html.Div(id='histogram-div', style={'display': 'none'}, children=[
            html.H1('Histogram'),
            dcc.Graph(className='histogram-chart', figure=histogram.get_histogram_figure(), config=dict(
            scrollZoom=False,
            showTips=False,
            showAxisDragHandles=False,
            doubleClick=False,
            displayModeBar=False
            )
        )
        ])
    ])
])

@app.callback(
    Output('bubble-div', 'style'),
    Output('heatmap-div', 'style'),
    Output('scatter-div', 'style'),
    Output('histogram-div', 'style'),
    Input('bubble-button', 'n_clicks'),
    Input('heatmap-button', 'n_clicks'),
    Input('scatter-button', 'n_clicks'),
    Input('histogram-button', 'n_clicks'),
    prevent_initial_call=True
)
def selector_button_clicked(bubble_button, heatmap_button, scatter_button, histogram_button):
    bubble_style = {'display': 'none'}
    heatmap_style = {'display': 'none'}
    scatter_style = {'display': 'none'}
    histogram_style = {'display': 'none'}

    changed_id = [p['prop_id'] for p in callback_context.triggered][0]

    if 'bubble-button' in changed_id:
        bubble_style = {'display': 'block'}

    elif 'heatmap-button' in changed_id:
        heatmap_style = {'display': 'block'}

    elif 'scatter-button' in changed_id:
        scatter_style = {'display': 'block'}

    elif 'histogram-button' in changed_id:
        histogram_style = {'display': 'block'}

    return bubble_style, heatmap_style, scatter_style, histogram_style
