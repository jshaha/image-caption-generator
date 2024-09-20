import base64
import requests
from PIL import Image
from io import BytesIO

# URL of the Colab API (replace with your ngrok URL)
COLAB_API_URL = 'http://xxxxxx.ngrok.io/generate_caption'

def send_image_to_colab(image_path):
    # Open and encode the image to base64
    with open(image_path, "rb") as img_file:
        img_base64 = base64.b64encode(img_file.read()).decode('utf-8')
    
    # Send the image to Colab API
    response = requests.post(COLAB_API_URL, json={'image': img_base64})
    
    # Get the caption from the response
    caption = response.json().get('caption', 'No caption generated')
    
    return caption
