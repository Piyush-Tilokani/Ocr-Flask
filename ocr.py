import os;
import json

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'ocr-project-416007-7da240be004c.json'

from google.cloud import vision
from google.cloud.vision_v1 import types

def detect_text(image_path):
    """Detects text in the image file."""
    client = vision.ImageAnnotatorClient()

    with open(image_path, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)
    response = client.text_detection(image=image)
    texts = response.text_annotations

    ret = []
    print('Texts:')
    for text in texts:
        print(text.description)
        ret.append(text.description)
    return json.dumps(ret)

def detect_text_uri(uri):
    """Detects text in the file located in Google Cloud Storage or on the Web."""
    from google.cloud import vision

    client = vision.ImageAnnotatorClient()
    image = vision.Image()
    image.source.image_uri = uri

    response = client.text_detection(image=image)
    texts = response.text_annotations
    print("Texts:")

    ret = []
    for text in texts:
        print(f'\n"{text.description}"')
        ret.append(text.description)
        vertices = [
            f"({vertex.x},{vertex.y})" for vertex in text.bounding_poly.vertices
        ]

        print("bounds: {}".format(",".join(vertices)))

    if response.error.message:
        raise Exception(
            "{}\nFor more info on error messages, check: "
            "https://cloud.google.com/apis/design/errors".format(response.error.message)
        )
    

# # Usage
# image_path = 'IMG_0245.jpg'
# detect_text(image_path)


# print(detect_text_uri('images/img1.jpeg'))
# print(detect_text_uri('images/img2.jpeg'))
# print(detect_text_uri('images/img3.jpeg'))
# print(detect_text_uri('images/img4.jpeg'))