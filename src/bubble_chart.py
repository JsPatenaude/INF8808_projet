import plotly.express as px
from preprocess import PreprocessBubble


def get_figure(df):
    pp = PreprocessBubble()
    df = pp.get_hashtags(df)

    hover_template = \
    '''
    <b style="font-size: 20px;">%{customdata[0]}</b>
    <br>
    <span style="font-size: 16px;>%{customdata[1]} likes générés</span>
    <br>
    <span style="font-size: 16px;>%{customdata[2]} commentaires générés</span>
    <br> 
    <span style="font-size: 16px;>%{customdata[3]} abonnés générés</span>  
    <extra></extra>
    '''

    fig = px.scatter(df, x='followers', y='comments', size='likes', hover_name='hashtag', size_max=30, custom_data=['hashtag', 'likes', 'comments', 'followers'])
    fig.update_layout(
        xaxis_title='Nombre de commentaires générés',
        yaxis_title='Nombre d\'abonnés générés',
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)'
    )
    fig.update_xaxes(showgrid=False)
    fig.update_yaxes(showgrid=False)
    fig.update_traces(hovertemplate=hover_template)
    return fig
