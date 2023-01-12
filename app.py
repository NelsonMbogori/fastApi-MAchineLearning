from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('upload.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'})
    
    image_file = request.files['image']
    if not image_file.filename:
        return jsonify({'error': 'No image selected'})
    
    image = image_file.read()
    
    # Use your model to predict the label of the image here
    # prediction = model.predict(image)
    prediction = "dummy prediction"
    return jsonify({'prediction': prediction})

if __name__ == '__main__':
    app.run(debug=True)
