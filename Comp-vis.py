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
    imgs = request.get("https://www.google.com/search?q=groceries&tbm=isch")
    soup = BeautifulSoup(imgs.text, "html.parser")
    return(soup)