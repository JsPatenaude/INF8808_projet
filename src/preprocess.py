import pandas as pd
from collections import Counter

# compte,nom,followers,cree,date,time,type,likes,comm,vues,url,desc

class PreprocessAbstract():
    def __init__(self):
        pass

    def onlyPicturesPosts(self, df):
        return df.loc[df['type'] == 'Photo']
    
    def keepColumns(self, df, columns):
        return df[columns]


class PreprocessBubble(PreprocessAbstract):
    def __init__(self):
        pass

    def get_hashtags(self, df):
        desired_columns = ['compte', 'desc', 'likes']
        df = self.keepColumns(df, desired_columns)

        
        all_hashtags = []
        
        for desc in df['desc']:
            if isinstance(desc, str):
                hashtags = [word for word in desc.split() if word.startswith('#')]
                all_hashtags = all_hashtags + hashtags

        counter = Counter(all_hashtags)
        most_common_hastags = counter.most_common(50)





        for desc in df['desc']:
            if isinstance(desc, str):
                for hashtag in most_common_hastags:
                    if hashtag in desc:
                        pass

        return df


class PreprocessHeatmap(PreprocessAbstract):
    def __init__(self):
        pass


class PreprocessScatter(PreprocessAbstract):
    def __init__(self):
        pass
    
    def preprocess_type():
        pass

    def preprocess_hashtags():
        pass


class PreprocessHistogram(PreprocessAbstract):
    def __init__(self):
        pass

    def printPostImages(self, df):
        # This function is useful to print the URLs of posts so we can manually download images
        # (because it is illegal (scary 😱😱😱) to webscrap images from Instagram)
        df_most_likes = df.sort_values('likes').head(100)
        all_images_url = df_most_likes['url']
        for i, url in enumerate(all_images_url):
            print(f"{i}: {url}")



if __name__ == "__main__":
    df = pd.read_csv('../data/data.csv')
    a = PreprocessHistogram()
    df = a.onlyPicturesPosts(df)
    a.savePostImages(df)
