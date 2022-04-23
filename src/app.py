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

from cv2 import DFT_REAL_OUTPUT
from dash import Dash, dcc, html, Input, Output, callback_context
import dash_daq as daq

import pandas as pd

import bubble_chart
import heatmap
import scatter
import histogram

df = pd.read_csv('../data/data.csv')

df_short = df.head(25000)

df_most_followers = df

app = Dash(__name__)
app.title = 'Projet | INF8808'
server = app.server

app.layout = html.Div(className='content', children=[
    html.Header(style={'display': 'flex', 'flex-direction': 'row', 'justify-content': 'center', 'gap': '1%', 'flex-wrap': 'wrap'}, children=[
        html.H1('Comment maximiser son rendement en tant que micro-influenceur sur'),
        html.Img(src='assets/instagram_logo.png', style={'width': '220px', 'height': '100px'})
    ]),
    html.Main(className='viz-container', style={'margin-left': '20%', 'margin-right': '20%'}, children=[
        html.Div(className='selector-buttons', style={'display': 'flex', 'flex-direction': 'row', 'justify-content': 'center', 'gap': '2%'}, children=[
            html.Button('Graphique à bulles', id='bubble-button'),
            html.Button('Carte de chaleur', id='heatmap-button'),
            html.Button('Nuage de points', id='scatter-button'),
            html.Button('Histogramme', id='histogram-button'),
        ]),
        html.Div(id='bubble-div', style={'display': 'block'}, children=[
            html.H2('Popularité de différents hashtags par rapport au nombre de likes, commentaires et followers générés'),
            dcc.Graph(id='bubble-chart', figure=bubble_chart.get_figure(df_short), config=dict(
                scrollZoom=False,
                showTips=False,
                showAxisDragHandles=False,
                doubleClick=False,
                displayModeBar=False
                )
            )
        ]),
        html.Div(id='heatmap-div', style={'display': 'none'}, children=[
            html.H2('Carte de chaleur de likes par rapport au jour de la semaine et heure de la journée'),
            dcc.Graph(id='heatmap-chart', figure=heatmap.get_figure(df_short), config=dict(
                scrollZoom=False,
                showTips=False,
                showAxisDragHandles=False,
                doubleClick=False,
                displayModeBar=False
                )
            )
        ]),
        html.Div(id='scatter-div', style={'display': 'none'}, children=[
            html.H2('Nombre de likes par rapport à la longueur de la description pour différents types de publication'),
            html.Div(style={'display': 'flex', 'flex-direction': 'row', 'justify-content': 'center', 'gap': '5%'}, children=[
                html.Span('Type de publication'),
                daq.BooleanSwitch(id='scatter-select', on=False),
                html.Span('Nombre de hashtags'),
            ]),
            html.Div(id='scatter-chart-type-div', style={'display': 'block'}, children=[
                dcc.Graph(id='scatter-chart-type', figure=scatter.get_figure_type(df_short), config=dict(
                scrollZoom=False,
                showTips=False,
                showAxisDragHandles=False,
                doubleClick=False,
                displayModeBar=False
                )
            )
            ]),
            html.Div(id='scatter-chart-hashtag-div', style={'display': 'none'}, children=[
                dcc.Graph(id='scatter-chart-hashtag', figure=scatter.get_figure_hashtag(df_short), config=dict(
                scrollZoom=False,
                showTips=False,
                showAxisDragHandles=False,
                doubleClick=False,
                displayModeBar=False
                )
            )
            ])     
        ]),
        html.Div(id='histogram-div', style={'display': 'none'}, children=[
            html.H2('Couleur les plus populaires sur les photos Instagram'),
            dcc.Graph(id='histogram-chart', figure=histogram.get_figure(df_short), config=dict(
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


@app.callback(
    Output('scatter-chart-type-div', 'style'),
    Output('scatter-chart-hashtag-div', 'style'),
    Input('scatter-select', 'on')
)
def select_scatter_type(value):
    if value:
        return {'display': 'none'}, {'display': 'block'}
    else:
        return {'display': 'block'}, {'display': 'none'}


if __name__ == '__main__':
    app.run_server()
