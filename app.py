import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model
from PIL import Image

model = load_model("stroke_model.keras")

st.set_page_config(page_title="Stone Detection", layout="centered")

st.title("Kidney Stone Detection")
st.write("Upload an Axial CT scan image for kidney stone detection")

uploaded = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])

if uploaded:
    img = Image.open(uploaded).convert("RGB")
    st.image(img, caption="Uploaded Image", width=300)

    img_resized = img.resize((224, 224))
    img_array = np.array(img_resized) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    with st.expander("🔍 Model Input Preview (224×224)"):
        st.image(img_resized, width=200)

    with st.spinner("Analyzing image..."):
        pred = float(model.predict(img_array)[0][0])

    st.subheader("🩺 Result")

    if pred > 0.5:
        st.error(f"Stone Detected — Confidence: {pred:.2f}")
    elif pred > 0.35:
        st.warning(f"Possible Stone — Low Confidence: {pred:.2f}")
    else:
        st.success(f"Normal — Confidence: {1 - pred:.2f}")







