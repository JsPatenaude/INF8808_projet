import cv2
import glob
import numpy as np
import collections

from scipy.cluster.vq import kmeans
from sklearn.cluster import KMeans

import pandas as pd
import plotly.express as px

IMG_PATH = '../data/images/'
IMG_SIZE = 317
N_CLUSTERS = 9


def get_dominant_colors(img_path):

    all_dominant_colors = []

    for img_file in glob.glob(img_path + '*.jpg'):
        img = cv2.imread(img_file)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = cv2.resize(img,(IMG_SIZE, IMG_SIZE))
        
        # Average color
        avg_colors = np.average(np.average(img, axis=0), axis=0)
        int_averages = np.array(avg_colors, dtype=np.uint8)
        dominant_color = int_averages

        dominant_color_img = np.zeros((IMG_SIZE, IMG_SIZE, 3), np.uint8)
        color = tuple(reversed(dominant_color))
        dominant_color_img[:] = color

        all_dominant_colors.append(color)

    return all_dominant_colors


def cluster_colors(all_dominant_colors, n_clusters):
    r = []
    g = []
    b = []

    for color in all_dominant_colors:
        r_value, g_value, b_value = color
        r.append(float(r_value))
        g.append(float(g_value))
        b.append(float(b_value))
    
    df = pd.DataFrame({'Red': r, 'Green': g, 'Blue' : b})

    cluster_centers_colors, _ = kmeans(df[['Red','Green', 'Blue']], n_clusters)

    kmeans_model = KMeans(n_clusters, random_state=1).fit(df)
    df['cluster_label'] = kmeans_model.labels_

    return df, cluster_centers_colors



def get_figure(df):
    all_dominant_colors = get_dominant_colors(str(IMG_PATH))
    df, clusters = cluster_colors(all_dominant_colors, N_CLUSTERS)
    colors = [f'rgb({int(color[0])}, {int(color[1])}, {int(color[2])})' for color in clusters]
    
    df['color'] = ''
    for i, row in df.iterrows():
        color = colors[row['cluster_label']]
        df.at[i, 'color'] = color
    df = df.sort_values('cluster_label')

    hover_template = \
    '''
    <b style="font-size: 20px;">%{x}</b>
    <br>
    <br>
    <b style="font-size: 16px;">Occurences: </b><span style="font-size: 16px;">%{y}</span> 
    <extra></extra>
    '''

    fig = px.histogram(df, x='color')
    fig.update_layout(
        xaxis_title='Couleur RGB',
        yaxis_title='Nombre d\'images ayant cette couleur dominante',
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)'
    )
    fig.update_xaxes(categoryorder='total descending', showgrid=False)
    fig.update_yaxes(showgrid=False)
    color_count = collections.Counter(fig['data'][0]['x']).most_common()
    colors_sorted = [color[0] for color in color_count] 
    fig.update_traces(marker_color=colors_sorted, hovertemplate=hover_template)
    
    return fig

