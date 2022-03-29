import pandas as pd
import time

class PreprocessAbstract():
    def __init__(self):
        pass


class PreprocessVis1(PreprocessAbstract):
    def __init__(self):
        pass



class PreprocessVis4(PreprocessAbstract):
    def __init__(self):
        pass

    def savePostImages(self):
        from selenium import webdriver
        from selenium.webdriver.chrome.options import Options
        import requests

        chrome_options = Options()
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(options=chrome_options)
        driver.implicitly_wait(1)
        driver.maximize_window()

        df = pd.read_csv('../data/data.csv')
        df_most_likes = df.head(20).sort_values('likes')

        all_images_url = df_most_likes['url']

        for i, url in enumerate(all_images_url):
            # Get image
            driver.get(url)
            driver.implicitly_wait(2)
            image_div = driver.find_element_by_class_name('FFVAD')
            image_src = image_div.get_attribute('src')
            print(image_src)
            # Save image
            img_data = requests.get(image_src).content
            with open(f'../data/images/image_{i}.jpg', 'wb') as handler:
                handler.write(img_data)
            time.sleep(5)


if __name__ == "__main__":
    a = PreprocessVis4()
    a.savePostImages()
