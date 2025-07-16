import streamlit as st
from PIL import Image
import pytesseract

# Ganti path ini sesuai lokasi Tesseract di komputermu
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\alwan.farhan\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

st.set_page_config(page_title="OCR Image Text Scanner", layout="centered")

st.title("📷 OCR Image Text Scanner")
st.markdown("Upload gambar dan ekstrak teks yang ada di dalamnya secara otomatis.")

uploaded_file = st.file_uploader("🖼️ Upload gambar", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Gambar yang diupload", use_column_width=True)

    with st.spinner("🔍 Mengekstrak teks dari gambar..."):
        extracted_text = pytesseract.image_to_string(image)

    st.subheader("📄 Hasil Ekstraksi Teks:")
    if extracted_text.strip():
        st.text_area("Teks yang Terdeteksi", value=extracted_text, height=300)
    else:
        st.warning("Tidak ada teks yang terdeteksi dalam gambar.")
