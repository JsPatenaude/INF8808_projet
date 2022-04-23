from preprocess import PreprocessScatter
import plotly.express as px

def get_figure_type(df):
    pp = PreprocessScatter()
    type_df = pp.preprocess_type(df)
    fig = px.scatter(type_df, x='desc_length', y='likes', color='type', custom_data=['type'])

    hover_template = \
    '''
    <b>Type de publication: </b>%{customdata[0]}
    <br>
    <b>Longueur de la description: </b>%{x} caractères
    <br>
    <b>Likes générés: </b>%{y:,.0f}
    <extra></extra>
    '''

    fig.update_layout(
        xaxis_title='Longueur de la description',
        yaxis_title='Nombre de likes générés par la publication',
        legend_title_text='Type de publication',
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)'
    )
    fig.update_xaxes(showgrid=False)
    fig.update_yaxes(showgrid=False)
    fig.update_traces(hovertemplate=hover_template)
    return fig

def get_figure_hashtag(df):
    pp = PreprocessScatter()
    hashtags_df = pp.preprocess_hashtags(df)

    hover_template = \
    '''
    <b>Nombre de hashtags dans la description: </b>%{customdata[0]}
    <br>
    <b>Longueur de la description: </b>%{x} caractères
    <br>
    <b>Likes générés: </b>%{y:,.0f}
    <extra></extra>
    '''

    fig = px.scatter(hashtags_df, x='desc_length', y='likes', color='n_hashtags', custom_data=['n_hashtags'])
    fig.update_layout(
        xaxis_title='Longueur de la description',
        yaxis_title='Nombre de likes générés par la publication',
        coloraxis_colorbar=dict(
            title='Nombre de hashtags'
        ),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)'
    )
    fig.update_xaxes(showgrid=False)
    fig.update_yaxes(showgrid=False)
    fig.update_traces(hovertemplate=hover_template)
    return fig 
