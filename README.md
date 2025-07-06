# 🧵 Solace Pixel – Automated Islamic Quote Poster for Instagram & Facebook

Solace Pixel is a **Streamlit-based tool** designed to help creators generate pixel-themed Islamic posts and publish them automatically to **Instagram** and **Facebook Pages** using the **Meta Graph API**. It combines image generation, Cloudinary image hosting, and social media automation — all with a clean, dynamic UI.

## 📌 Use Case

This tool is built for:

- 🧕 **Islamic content creators** who want to share verses, quotes, or reflections using pixel-style visuals.
- 🎮 **Gaming-themed da’wah pages** using Minecraft/pixel art as a creative medium.
- ⏱️ Anyone looking to **automate their social media content posting** with minimal effort.

## 🔁 What It Does

1. Upload a **pixel-style image** (e.g., Minecraft scene or pixel art).
2. Add:
   - Islamic **quote**
   - Reference (e.g., Qur’an 94:6)
   - Caption and hashtags for Instagram
3. It generates a **4:5 portrait Instagram-ready post** with custom pixel fonts.
4. Uploads the image to **Cloudinary**
5. Posts it **automatically to Instagram** (and optionally Facebook) using your access token.

## 🔐 .env Setup

You’ll need the following environment variables saved in a `.env` file:

```env
# Instagram Graph API
ACCESS_TOKEN=your_long_lived_access_token
INSTAGRAM_USER_ID=your_instagram_user_id

# Cloudinary (for image hosting)
CLOUDINARY_CLOUD_NAME=your_cloud_name
CLOUDINARY_API_KEY=your_api_key
CLOUDINARY_API_SECRET=your_api_secret
```

> 📌 To get Instagram API credentials, you must connect your Instagram account to a Facebook Page and create a Meta App.

## 📦 Requirements

Install dependencies using:

```bash
pip install -r requirements.txt
```

Contents of `requirements.txt`:

```txt
streamlit
Pillow
requests
python-dotenv
cloudinary
```

## 🖼️ Fonts

You must include your custom fonts in the project directory. For example:

```bash
/fonts/
├── PPNeueBit-Bold.otf
├── PPMondwest-Regular.otf
```

Update the font paths in `image_generator.py` if needed.

## 🧠 How the App Works Internally

1. **Frontend**: Built with Streamlit (`app.py`)
2. **Image Composition**: `image_generator.py` uses PIL to format the image to 1080x1350 with centered text below.
3. **Image Hosting**: `cloudinary_uploader.py` uploads final image to Cloudinary.
4. **Instagram Posting**:
    - Step 1: Send image URL to `/media` endpoint
    - Step 2: Use the returned creation ID to post via `/media_publish`

## ▶️ How to Run Locally

### 1. Clone the repo

```bash
git clone https://github.com/MujtabaIT2002/Solace-Pixel.git
cd Solace-Pixel
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Add your `.env` file

Create a `.env` file in the root directory and paste your API credentials (see above).

### 4. Run the app

```bash
streamlit run app.py
```

This will open the app in your browser at `http://localhost:8501`.

## 🛠️ Customization Tips

- You can switch fonts in `image_generator.py` to reflect different styles (classic, pixelated, serif).
- Add support for **Facebook posting** by attaching your Facebook Page ID in the API.
- Add scheduling logic using tools like **cron** or **Streamlit Schedule** for automation.
