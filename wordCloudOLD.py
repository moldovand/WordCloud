import matplotlib.pyplot as pPlot
from wordcloud import WordCloud, STOPWORDS
import numpy as npy
from PIL import Image
dataset = open("/Users/danielmoldovan/Documents/Daniel/PROGRAMMING/Environments/WordCloud/dmoldovan.txt", "r").read()
def create_word_cloud(string):
    maskArray = npy.array(Image.open("/Users/danielmoldovan/Documents/Daniel/PROGRAMMING/Environments/WordCloud/cloud.jpg"))
    cloud = WordCloud(background_color = "white", max_words = 300, mask = maskArray, stopwords = set(STOPWORDS))
    cloud.generate(string)
    cloud.to_file("/Users/danielmoldovan/Documents/Daniel/PROGRAMMING/Environments/WordCloud/wordCloud.png")
dataset = dataset.lower()
create_word_cloud(dataset)
