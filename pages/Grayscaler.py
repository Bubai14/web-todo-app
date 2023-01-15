import streamlit as st

# PIL is the object of pillow library needed for image modification
# pillow is automatically added as a streamlit transitive dependency.
from PIL import Image


with st.expander("Start Camera"):
    # Start the camera
    camera_image = st.camera_input("Camera")


if camera_image:
    # Create a pillow image instance
    image = Image.open(camera_image)

    # Convert the pillow image instance to grayscale
    gray_image = image.convert("L")

    # Render the grayscaled image on the webpage
    st.image(gray_image)