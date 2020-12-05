import matplotlib.pyplot as pPlot
from wordcloud import WordCloud, STOPWORDS
import numpy as npy
from PIL import Image
# some minor edit
dataset = open("dmoldovan.txt", "r").read()
def create_word_cloud(string):
    maskArray = npy.array(Image.open("cloud.jpg"))
    cloud = WordCloud(background_color = "white", max_words = 300, mask = maskArray, stopwords = set(STOPWORDS))
    cloud.generate(string)
    cloud.to_file("wordCloudart.png")
dataset = dataset.lower()
create_word_cloud(dataset)
