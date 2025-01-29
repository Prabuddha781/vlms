import numpy as np
import cv2
import runpod

def receive_image(image):
    try:        
        # Convert to numpy array
        nparr = np.frombuffer(image, np.uint8)
        
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

runpod.serverless.start({"handler": handler})