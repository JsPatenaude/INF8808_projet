import plotly.express as px
from preprocess import PreprocessHeatmap

def get_figure(df):
    pp = PreprocessHeatmap()
    heatmap_df = pp.preprocess_heatmap(df)

    hover_template = \
    '''
    <b style="font-size: 20px;>%{x}, %{y}h00</b>
    <br>
    <span style="font-size: 16px;>%{z:.0f} likes générés</span>
    <extra></extra>
    '''

    fig = px.imshow(heatmap_df)
    fig.update_layout(
        xaxis_title='Jour de la semaine',
        yaxis_title='Heure de la journée',
        yaxis_nticks=24,
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)'
    )
    fig.update_traces(hovertemplate=hover_template)
    return fig