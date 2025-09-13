import pandas as pd
import numpy as nu
import matplotlib as mat
import tensorflow as tf
import keras
from keras import layers, models, optimizers
from keras.utils import load_img, img_to_array, save_img
from keras.preprocessing.image import ImageDataGenerator
from bs4 import BeautifulSoup
import requests

class __main__:

    # Scan images 
    def scan_img(self):
        global Image_Core
        Image_Core = pd.read_json()
        return(Image_Core)


    # Web scrape images from popular grocery stores
    def scrape_img(self):
        store = input("What Store do you shop from? ")
        imgs = requests.get(f"https://{store}.com/")
        soup = BeautifulSoup(imgs.content, "html.parser")
        prod= requests.get(f"https://{store}.com/search?q={Image_Core}")
        soup_2 = BeautifulSoup(prod.text, "html.parser")
        return(soup, soup_2)

    # learn useage patterns 

