import streamlit as st
import cv2 
import numpy as np
from PIL import Image

def load_image(image_file):
    img = Image.open(image_file)
    return np.array(img)

