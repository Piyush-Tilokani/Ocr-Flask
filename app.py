from flask import Flask, render_template, request, jsonify
from ocr import detect_text

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/process_image', methods=['POST'])
def process_image():
    if 'image' in request.files:
        # Process the uploaded image
        image = request.files['image']
        image.save('uploads/image.jpg')
        detected_text = detect_text('uploads/image.jpg')
        
        print(type(detected_text))
        print('Detected text testing \n\n\n\n\n\n')
        print(detected_text)

        # Return the detected text as JSON response
        return jsonify({'detected_text': detected_text}), 200
    else:
        return 'No image received.', 400

if __name__ == '__main__':
    app.run(debug=True)
