import pandas as pd
from collections import Counter
from datetime import datetime

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

        return df

        for desc in df['desc']:
            if isinstance(desc, str):
                for hashtag in most_common_hastags:
                    if hashtag in desc:
                        pass

        


class PreprocessHeatmap(PreprocessAbstract):
    def __init__(self):
        pass

    def preprocess_heatmap(self, df):
        heatmap_df = df[['likes', 'date', 'time']]
        heatmap_df['weekday'] = [datetime.strptime(str(date), '%Y-%m-%d').strftime('%A') for date in heatmap_df['date']]
        heatmap_df['hour'] = pd.to_datetime(heatmap_df['time'], format='%H:%M:%S').dt.hour
        heatmap_df = heatmap_df.pivot_table(values='likes', index=['hour'], columns=['weekday']).fillna(0)

        return heatmap_df


class PreprocessScatter(PreprocessAbstract):
    def __init__(self):
        pass
    
    def preprocess_type(self, df):
        df_types = df[df['type'].isin(['Photo', 'Album', 'Video'])]
        df_types['desc_length'] = df_types['desc'].str.len()
        return df_types[['likes', 'desc_length', 'type']]
        
    def preprocess_hashtags(self, df):
        df['desc_length'] = df['desc'].str.len()
        n_hashtags = []
        for desc in df['desc']:
            if isinstance(desc, str):
                hashtags = [word for word in desc.split() if word.startswith('#')]
                n_hashtags.append(len(hashtags))
            else:
                n_hashtags.append(0)

        df['n_hashtags'] = n_hashtags
        return df[['likes', 'desc_length', 'n_hashtags']]


class PreprocessHistogram(PreprocessAbstract):
    def __init__(self):
        pass

    def printPostImages(self, df):
        # This function is useful to print the URLs of posts so we can manually download images
        # (because it is illegal to webscrap images from Instagram)
        df_most_likes = df.sort_values('likes').head(100)
        all_images_url = df_most_likes['url']
        for i, url in enumerate(all_images_url):
            print(f"{i}: {url}")



if __name__ == "__main__":
    df = pd.read_csv('../data/data.csv')
    a = PreprocessHistogram()
    df = a.onlyPicturesPosts(df)
    a.savePostImages(df)
