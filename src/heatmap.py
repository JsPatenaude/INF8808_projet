import plotly.express as px
from preprocess import PreprocessHeatmap

def get_figure(df):
    pp = PreprocessHeatmap()
    heatmap_df = pp.preprocess_heatmap(df)

    fig = px.imshow(heatmap_df)
    return fig