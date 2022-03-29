import pandas as pd
import time

class PreprocessAbstract():
    def __init__(self):
        pass

    def onlyPicturesPosts(self, df):
        return df.loc[df['type'] == 'Photo']


class PreprocessVis1(PreprocessAbstract):
    def __init__(self):
        pass



class PreprocessVis4(PreprocessAbstract):
    def __init__(self):
        pass

    def savePostImages(self, df):

        df_most_likes = df.sort_values('likes').head(100)

        all_images_url = df_most_likes['url']

        for i, url in enumerate(all_images_url):
            print(f"{i}: {url}")



if __name__ == "__main__":
    df = pd.read_csv('../data/data.csv')
    a = PreprocessVis4()
    df = a.onlyPicturesPosts(df)
    a.savePostImages(df)
