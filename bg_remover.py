from io import BytesIO
from PIL import Image
from rembg import remove
import streamlit as st




st.set_page_config(page_title="BG Remover", page_icon="🖼️")
st.title("Your Best BG-remover")
st.write(":dog: This app uses the rembg library to remove the background from your images easily. Upload your image, and the app will process it to remove the background, allowing you to download the result with a clear, background-free image.")
st.sidebar.write("**How to use:**")

st.sidebar.write("1. Upload an image by clicking the 'Browse files' button.")

col1, col2 = st.columns(2)

def convert_image(img):
    buf = BytesIO()
    img.save(buf, format="PNG")
    buf.seek(0)  # Reset buffer position to the beginning
    byte_im = buf.getvalue()
    return byte_im

def fix_image(image):
    image = Image.open(image)
    col1.write("Original image :camera:")
    col1.image(image)

    fixed = remove(image)
    col2.write("Removed background image :scissors:")
    col2.image(fixed)
    # st.sidebar.markdown("\\n")
    st.sidebar.download_button(
        "Download your file here", convert_image(fixed), "fixed.png", "image/png"
    )

image_upload = st.sidebar.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

if image_upload is not None:
    fix_image(image_upload)
else:
    st.write("Please upload an image to remove the background.")
