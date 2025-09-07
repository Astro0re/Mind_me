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

# Web scrape images from popular grocery stores
def scrape_img():
    store = input("What Store do you shop from? ")
    imgs = requests.get(f"https://{store}.com/")
    soup = BeautifulSoup(imgs.text, "html.parser")
    product = input("What product do you want to find? ")
    prod= request.get(f"https://{store}.com/search?q={product}")
    soup_2 = BeautifulSoup(prod.text, "html.parser")
    return(soup, soup_2)