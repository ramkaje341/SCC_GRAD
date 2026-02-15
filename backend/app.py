from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
import os
from PIL import Image
import torch
from torchvision import transforms

app = Flask(__name__)

# Setup file upload folder and allowed extensions
UPLOAD_FOLDER = 'uploads/'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Define a simple transform for images
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor()
])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Load your PyTorch model here
# model = torch.load("model.pth")
# model.eval()

@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return jsonify({"error": "No image part"}), 400

    file = request.files['image']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        # Load the image and preprocess
        image = Image.open(file_path).convert('RGB')
        image_tensor = transform(image).unsqueeze(0)  # Add batch dimension

        # Make prediction using the model
        # with torch.no_grad():
        #     outputs = model(image_tensor)
        #     _, predicted = torch.max(outputs, 1)
        #     predicted_grade = f"Grade {predicted.item()}"

        # Temporary placeholder until model is ready
        predicted_grade = "Grade 1"

        return jsonify({"grade": predicted_grade})

    return jsonify({"error": "Invalid file type"}), 400

if __name__ == "__main__":
    app.run(debug=True)
