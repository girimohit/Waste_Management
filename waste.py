import streamlit as st
from PIL import Image
import tensorflow as tf

# from tensorflow.keras.models import load_model
# from tensorflow.python.keras.models import load_model
from keras.models import load_model
from streamlit_webrtc import VideoTransformerBase, webrtc_streamer
import cv2


# MODEL_PATH = "waste_model.h5"
# DATA_PATH = "waste1.jpg"
MODEL_PATH = "./classifier/waste_model.h5"
DATA_PATH = "./classifier/waste1.jpg"


class ImageProcessor(VideoTransformerBase):
    def __init__(self):
        self.model = load_model()

    def transform(self, frame):
        # Display the camera feed
        st.image(frame.to_ndarray(format="jpeg"), channels="BGR")
        # Display instructions for the user
        st.info("Click the 'Capture Image' button to take a picture.")
        # Create a button to capture the image
        if st.button("Capture Image", key="b1"):
            # Convert the captured frame to a PIL Image
            img = Image.fromarray(frame.to_ndarray(format="rgb"))
            # Perform image processing
            img_array = image_processing(img)
            # Make prediction using the pre-trained model
            result = self.model.predict(img_array)
            prediction = "Recyclable Waste" if result[0][0] == 1 else "Organic Waste"
            # Display the prediction
            st.subheader("This Waste is:")
            st.success(prediction)
            st.write("(Prediction successfully made!)")


# st.cache_data
def load_data(image_path):
    """Function to load image"""
    img = Image.open(image_path)
    return img


# @st.cache(allow_output_mutation=True)
def load_models(model_path):
    """Function to load model"""
    model = load_model(model_path, compile=False)
    return model


def image_processing(img):
    """Function for image processing"""
    img_resized = img.resize((64, 64))
    img_array = tf.keras.preprocessing.image.img_to_array(img_resized)
    img_array = img_array.reshape((1, 64, 64, 3))
    return img_array


# Main Streamlit app
st.title("AI-Waste Classification")
st.markdown(
    "**This application will let you verify if your waste may be recyclable or not.**"
)


st.sidebar.title("Select options:")
page = st.sidebar.selectbox(
    "Choose a page:",
    [
        "Capture Image",
        "Upload an Image",
    ],
)

if page == "Capture Image":
    st.title("Capture an image of waste to classify")
    st.markdown("**To get a prediction please capture a clear image of some waste.**")

    # Start capturing video from the camera
    cap = cv2.VideoCapture(0)

    # Placeholder to display the camera feed
    camera_placeholder = st.empty()

    # Placeholder for the captured image
    captured_image_placeholder = st.empty()

    # Display the camera feed until the user clicks the capture button
    # while True:
    ret, frame = cap.read()

    # Convert the frame to RGB (Streamlit uses RGB images)
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Display the camera feed
    camera_placeholder.image(frame_rgb, channels="RGB", use_column_width=True)

    # Check if the capture button is clicked
    if st.button("Capture Image", key=f"b3"):
        # Convert the captured frame to PIL Image
        captured_image = Image.fromarray(frame_rgb)
        img_array = image_processing(captured_image)
        st.subheader("This Waste is:")
        # if st.checkbox('Show Prediction of your image'):
        model = load_models(MODEL_PATH)
        result = model.predict(img_array)
        prediction = (
            "**Recyclable Waste**" if result[0][0] == 1 else "**Organic Waste**"
        )
        st.success(prediction)
        st.write("(Classified successfully!)")

    # Release the camera
    cap.release()

if page == "Upload an Image":
    st.markdown(
        "**To get a prediction please upload your own clear image of some waste.**"
    )
    st.header("AI-Classification Of Your Waste")
    uploaded_file = st.file_uploader("Choose your image", type=["jpg", "png"])
    if uploaded_file is not None:
        img = Image.open(uploaded_file)
        st.info("Your image:")
        st.image(img, caption="(Uploaded image)", use_column_width=True)
        img_array = image_processing(img)
        st.subheader("This Waste is:")
        # if st.checkbox('Show Prediction of your image'):
        model = load_models(MODEL_PATH)
        result = model.predict(img_array)
        prediction = (
            "**Recyclable Waste**" if result[0][0] == 1 else "**Organic Waste**"
        )
        st.success(prediction)
        st.write("(Classified successfully!)")

# Run on custom prot
# streamlit run waste.py --server.port 3620
