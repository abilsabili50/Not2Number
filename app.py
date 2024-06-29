import os
import numpy as np
import cv2 as cv
import tensorflow as tf

from flask import Flask, render_template, request, Response
app = Flask(__name__)

detect = tf.saved_model.load("./model/saved_model")
print("sukses load model")

class_mapping = {1:"1",2:"1'",3:"1''",4:"2",5:"2'",6:"3",7:"3'",8:"4",9:"4'",10:"5",11:"5'",12:"5,",13:"6",14:"6'",15:"6,",16:"7",17:"7'",18:"7,",19:"0"}

#Allow files with extension png, jpg and jpeg
ALLOWED_EXT = set(['jpg' , 'jpeg' , 'png'])
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXT

def read_image(filename):
    image = cv.imread(filename)
    image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
    return image

def convert_image_into_input(image):
    ret, thresholded_image = cv.threshold(image, 235, 255, cv.THRESH_BINARY_INV)
    x = np.expand_dims(thresholded_image, axis=0)
    return x

def draw_boxes(image, boxes, scores, labels, score_threshold=0.5):
  for box, score, label in zip(boxes, scores, labels):
    if score < score_threshold:
      continue

    ymin, xmin, ymax, xmax = box

    im_height, im_width = image.shape[:2]
    xmin = int(xmin * im_width)
    ymin = int(ymin * im_height)
    xmax = int(xmax * im_width)
    ymax = int(ymax * im_height)

    center = int((xmax - xmin)/2)

    new_label = class_mapping[label]
    label_text = f"{new_label}"
    cv.putText(image, label_text, (xmin + center, ymin), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)

def transform(filepath):
    image = read_image(filepath)
    input_image = convert_image_into_input(image)
    detected = detect(input_image)

    boxes = detected["detection_boxes"][0].numpy()
    scores = detected["detection_scores"][0].numpy()
    labels = detected["detection_classes"][0].numpy().astype(np.int32)
    
    draw_boxes(image, boxes, scores, labels)
    [filename, ext] = filepath.split('.')
    new_filepath = filename + "_transformed." + ext
    cv.imwrite(new_filepath, image)
    return os.path.basename(new_filepath)
    

@app.route('/', methods=['GET', 'POST'])
def home():
    output_image = "image/card_image.png"
    error = ""
    disabled = "disableClick"
    
    # transformasi dilakukan
    if request.method == 'POST':
        file = request.files['input_image']
        if file and allowed_file(file.filename):
            filename = file.filename
            
            saved_filepath = os.path.join("static", "temp", filename)
            file.save(saved_filepath)
            
            new_filepath = transform(saved_filepath)
            output_image = "temp/" + new_filepath
            
            error = "hidden"
            disabled = ""
            return render_template('index.html', output_image=output_image, error=error, disabled=disabled)
        else :
            return render_template('index.html', output_image=output_image, error=error, disabled=disabled)

    error = "hidden"
    return render_template('index.html', output_image=output_image, error=error, disabled=disabled)

if __name__ == '__main__':
    app.run(debug=True)