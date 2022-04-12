import plotly.express as px
from preprocess import PreprocessBubble


def get_figure(df):
    pp = PreprocessBubble()
    df = pp.get_hashtags(df)

    fig = px.scatter(df, x='followers', y='comments', size='likes', hover_name='hashtag', size_max=30)
    return fig
