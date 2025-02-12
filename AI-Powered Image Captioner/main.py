import streamlit as st
from PIL import Image
from read_image import ImageCaptioningModel
from sound import say

def main():
    st.title("AI-Powered Image Captioning")
    uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])
    
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)
        
        try:
            # Instantiate the model and generate caption
            model = ImageCaptioningModel()
            caption = model.generate_caption(uploaded_file)
            st.write("**Generated Caption:**", caption)
            say(caption)
        except Exception as e:
            st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
“”“use streamlit run main.py to run”“”
