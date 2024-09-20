from flask import Flask, request, render_template
import requests
import base64
import os

app = Flask(__name__)

# Replace this with the ngrok URL from your local environment (this will be for Colab to connect)
LOCAL_NGROK_URL = "https://9dde-2607-f140-400-3f-c5a2-98aa-cc78-4eda.ngrok-free.app"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Get the uploaded image
        image = request.files['image']
        image_path = os.path.join("static/uploads", image.filename)
        image.save(image_path)  # Save the image locally
        
        # Convert the image to base64
        with open(image_path, "rb") as img_file:
            img_base64 = base64.b64encode(img_file.read()).decode('utf-8')
        
        # Send the image to the Colab server for caption generation
        # This is the ngrok URL that will expose your local server to Colab
        COLAB_API_URL = f"{LOCAL_NGROK_URL}/generate_caption"

        response = requests.post(COLAB_API_URL, json={'image': img_base64})
        caption = response.json().get('caption', 'No caption generated')

        # Display the image and generated caption in the HTML template
        return render_template("index.html", image=image_path, caption=caption)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(port=5000, debug=True)
