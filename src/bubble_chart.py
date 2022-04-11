import plotly.express as px
from preprocess import PreprocessBubble


def get_figure(df):
    pp = PreprocessBubble()
    df = pp.get_hashtags(df)

    fig = px.scatter(df, size='likes')
    return fig