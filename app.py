import streamlit as st
from image_generator import generate_post
from cloudinary_uploader import upload_to_cloudinary
from dotenv import load_dotenv
import requests
import os

load_dotenv()

# Instagram posting function
def post_to_instagram(image_url, caption):
    user_id = os.getenv("INSTAGRAM_USER_ID")
    access_token = os.getenv("ACCESS_TOKEN")

    # Step 1: Create media container
    media_url = f"https://graph.facebook.com/v19.0/{user_id}/media"
    res = requests.post(media_url, data={
        "image_url": image_url,
        "caption": caption,
        "access_token": access_token
    }).json()

    if "error" in res:
        return res  # early return if API fails

    creation_id = res.get("id")

    # Step 2: Publish media
    publish_url = f"https://graph.facebook.com/v19.0/{user_id}/media_publish"
    pub_res = requests.post(publish_url, data={
        "creation_id": creation_id,
        "access_token": access_token
    }).json()

    return pub_res

# --- Streamlit UI ---
st.set_page_config(page_title="Solace Pixel Post Generator", layout="centered")
st.title("🧵 Solace Pixel")
st.caption("Create pixel-style Islamic Instagram posts with one click.")

image_file = st.file_uploader("Upload image (Minecraft, pixel art, etc)", type=["jpg", "png"])
quote = st.text_area("Enter quote")
reference = st.text_input("Enter reference (e.g., Qur’an 94:6)")
caption = st.text_area("Instagram caption")
hashtags = st.text_area("Hashtags (e.g. #islamic #pixelquote #minecraft)")

submit = st.button("Generate & Upload")

if submit:
    if image_file and quote and reference:
        with open("uploaded_image.jpg", "wb") as f:
            f.write(image_file.read())

        output_path = generate_post("uploaded_image.jpg", quote, reference)
        cloud_url = upload_to_cloudinary(output_path)
        full_caption = f"{caption}\n\n{hashtags}"
        response = post_to_instagram(cloud_url, full_caption)

        if "id" in response:
            st.success("✅ Successfully posted to Instagram!")
        else:
            st.error(f"❌ Failed to post: {response.get('error', {}).get('message', 'Unknown error')}")

        st.image(output_path, caption="Final image", use_column_width=True)
        st.write(response)
    else:
        st.warning("Please fill in all fields and upload an image.")
