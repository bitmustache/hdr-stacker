import streamlit as st
import cv2
import numpy as np
from PIL import Image
import io
from dotenv import load_dotenv
import os

#load adsense environment variables from .env file
load_dotenv()

GOOGLE_ADSENSE_SCRIPT = os.getenv('GOOGLE_ADSENSE_SCRIPT')

def load_image(image_file):
    img = Image.open(image_file)
    return np.array(img)

def create_hdr(images):
    exposures = [cv2.cvtColor(img, cv2.COLOR_RGB2BGR).astype(np.float32) for img in images]
    merge_mertens = cv2.createMergeMertens()
    hdr = merge_mertens.process(exposures)
    hdr_8bit = np.clip(hdr * 255, 0, 255).astype('uint8')
    hdr_rgb = cv2.cvtColor(hdr_8bit, cv2.COLOR_BGR2RGB)
    return hdr_rgb

def main():
    st.title("HDR Photo Stacker")

    st.components.v1.html(
        {GOOGLE_ADSENSE_SCRIPT}
    )

    uploaded_files = st.file_uploader("Upload Photos", type=["png", "jpg", "jpeg"], accept_multiple_files=True)

    if uploaded_files:
        images = [load_image(file) for file in uploaded_files]

        if len(images) > 1:
            hdr_image = create_hdr(images)
            st.image(hdr_image, caption='HDR image', use_column_width=True)
        else: 
            st.warning("Please upload at least two photos to create an HDR image.")

if __name__ == "__main__":
    main()