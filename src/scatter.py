from preprocess import PreprocessScatter
import plotly.express as px

def get_figure_type(df):
    pp = PreprocessScatter()
    type_df = pp.preprocess_type(df)
    return px.scatter(type_df, x='desc_length', y='likes', color='type')

def get_figure_hashtag(df):
    pp = PreprocessScatter()
    hashtags_df = pp.preprocess_hashtags(df)
    return px.scatter(hashtags_df, x='desc_length', y='likes', color='n_hashtags') 
