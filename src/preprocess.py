from typing import final
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


    def get_hashtags(self, df, amount=50):
        desired_columns = ['desc', 'likes', 'comm', 'followers']
        df = self.keepColumns(df, desired_columns)
        df = df.dropna()

        # Get all unique hashtags
        all_hashtags = []
        for desc in df['desc']:
            if isinstance(desc, str):
                hashtags = [word for word in desc.split() if word.startswith('#')]
                all_hashtags = all_hashtags + hashtags

        # Get the most common hashtags
        counter = Counter(all_hashtags)
        most_common_hastags = counter.most_common(amount)

        # Calculate likes generated by each hashtag
        generated_likes = {}
        hashtag_followers = {}
        hashtag_comments = {}
        for desc, likes, followers, comments  in zip(df['desc'], df['likes'], df['followers'], df['comm']):
            if isinstance(desc, str):
                for hashtag in most_common_hastags:
                    if hashtag[0] in desc:
                        try:
                            generated_likes[hashtag[0]] += likes
                            hashtag_followers[hashtag[0]] += followers
                            hashtag_comments[hashtag[0]] += comments
                        except KeyError:
                            generated_likes[hashtag[0]] = likes
                            hashtag_followers[hashtag[0]] = followers
                            hashtag_comments[hashtag[0]] = comments

        # Create clean dataframe
        final_df = pd.DataFrame()
        final_df['hashtag'] = generated_likes.keys()
        final_df['likes'] = generated_likes.values()
        final_df['followers'] = hashtag_followers.values()
        final_df['comments'] = hashtag_comments.values()

        return final_df


class PreprocessHeatmap(PreprocessAbstract):
    def __init__(self):
        pass


    def preprocess_heatmap(self, df):
        heatmap_df = df[['likes', 'date', 'time']]
        heatmap_df = heatmap_df.dropna()
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
