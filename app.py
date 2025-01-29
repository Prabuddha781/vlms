from flask import Flask, request
from flask_cors import CORS
import numpy as np
import cv2
import runpod

app = Flask(__name__)
CORS(app)

@app.route('/camera', methods=['POST'])
def receive_image():
    try:
        # Get image data from request
        image_data = request.get_data()
        
        # Convert to numpy array
        nparr = np.frombuffer(image_data, np.uint8)
        
        # Decode image
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        
        # Here you can process the image as needed
        # For now just return success
        return {'status': 'success'}, 200
        
    except Exception as e:
        return {'error': str(e)}, 400

# RunPod handler
def handler(job):
    job_input = job['input']

    camera_image = job_input.get('image', 'World')

    return receive_image(camera_image)

if __name__ == '__main__':
    runpod.serverless.start({"handler": handler})
    app.run(host='0.0.0.0', port=9000)

