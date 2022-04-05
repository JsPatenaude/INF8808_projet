import cv2
import numpy as np
import glob
import matplotlib.pyplot as plt
import numpy as np
from scipy.cluster.vq import kmeans, whiten
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
    print(cluster_centers_colors)

    kmeans_model = KMeans(n_clusters, random_state=1).fit(df)
    df['cluster_label'] = kmeans_model.labels_

    return df, cluster_centers_colors



def get_histogram_figure():
    all_dominant_colors = get_dominant_colors(str(IMG_PATH))
    df, clusters = cluster_colors(all_dominant_colors, N_CLUSTERS)

    fig = px.histogram(df, x='cluster_label')

    # TODO add colors from clusters

    return fig



if __name__ == "__main__":
    all_dominant_colors = get_dominant_colors(str(IMG_PATH))
    df, clusters = cluster_colors(all_dominant_colors, N_CLUSTERS)

