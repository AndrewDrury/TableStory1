from flask import Flask
from flask import request
import tensorflow as tf
import cv2
import detector_utils as detector_utils
import numpy as np
import os
import json
UPLOAD_FOLDER = 'uploads'
from predict import predict
import base64
from mimetypes import guess_extension
from urllib.request import urlretrieve
from PIL import Image
ADJUSTMENT = 10
app = Flask(__name__)

filecounter = 1

detection_graph, sess = detector_utils.load_inference_graph()
cv2.namedWindow('Single-Threaded Detection', cv2.WINDOW_NORMAL)

def grab_hands(filename):
    if not os.path.exists('converted'):
        os.makedirs('converted')
    cv2.namedWindow('Single-Threaded Detection', cv2.WINDOW_NORMAL)
    img = cv2.imread(filename)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    boxes, scores = detector_utils.detect_objects(img, detection_graph, sess)
    #print(boxes, scores)
    num_hands_detect = 2
    im_width, im_height = (640, 360)
    points = detector_utils.draw_box_on_image(num_hands_detect, 0.27,
                                    scores, boxes, im_width, im_height,
                                    img)
    cv2.imshow('Single-Threaded Detection', cv2.cvtColor(img, cv2.COLOR_RGB2BGR))
    filename = filename.split("/")[-1]
    print(filename)
    print(len(points))
    if len(points) == 0:
        return
    for p1, p2 in points:
        w = p2[0] - p1[0]
        h = p2[1] - p1[1]
        img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
        cropped = img[(p1[1]-ADJUSTMENT):ADJUSTMENT+p1[1]+h, (p1[0]-ADJUSTMENT):ADJUSTMENT+p1[0]+w]
        #cv2.imshow("cropped", cropped)
        
        fname = f'converted/{filename}'
        print(fname)
        cv2.imwrite(fname, cropped)
        return fname
        #cv2.waitKey()


@app.route('/demo',methods=['POST','GET'])
def demo():
     global filecounter
     if request.method == 'POST':
         r = request.get_json()
        #  print()
         url = r['image']
         filename, m = urlretrieve(url, f"uploads/file_{filecounter}.png")
         img = Image.open(f"uploads/file_{filecounter}.png")
         new_img = img.resize((640,360))
         new_img.save(f"uploads/file_{filecounter}",'png')
         filecounter = filecounter + 1
        #  print(filename, guess_extension(m.get_content_type()))
        #  print(image_str[:10], type(image_str))
        #  with open(f"uploads/file_{filecounter}.png","wb") as f:
        #     f.write(base64.decodebytes(image_str.encode()))

        #  print(r)
        #  f = r.files['file']
        #  print(f)
        #  pathname = os.path.join(UPLOAD_FOLDER, f.filename)
        #  f.save(pathname)

         #image = base64.decodestring(data['image'])
        
         fname = grab_hands(filename)
         print(fname)
         if fname:
            return predict(fname)
         else:

            return "idle"

     return  '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    
    '''

#app.graph=load_graph('./frozen_inference_graph_141 14-51-46-798.pb')  
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int("5000"), debug=True, use_reloader=False)
