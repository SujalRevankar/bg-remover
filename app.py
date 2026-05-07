from flask import Flask, request, send_file, render_template
from rembg import remove
from PIL import Image
import io

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/remove-bg", methods=["POST"])
def remove_bg():
    file = request.files["image"]
    input_image = Image.open(file.stream)
    output_image = remove(input_image)

    img_io = io.BytesIO()
    output_image.save(img_io, format="PNG")
    img_io.seek(0)

    return send_file(img_io, mimetype="image/png", download_name="no_background.png")

if __name__ == "__main__":
    app.run(debug=True)
