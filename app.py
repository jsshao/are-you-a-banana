import os
import uuid
import matplotlib.pyplot as pl
import numpy as np
import pandas as pd
from flask import Flask
from flask import redirect
from flask import render_template
from flask import request
from flask import send_from_directory
from flask import url_for
from PIL import Image
from sklearn.decomposition import RandomizedPCA
from sklearn.neighbors import KNeighborsClassifier

app = Flask(__name__)
STANDARD_SIZE = (300, 167)
IMG_DIR = "static/images/"
UPLOAD_DIR = "uploads"
ACCEPTED_EXTENSIONS = (".png", ".jpg", ".jpeg")
pca = RandomizedPCA(n_components=5)
knn = KNeighborsClassifier()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/uploads/<filename>')
def showImg(filename):
    return send_from_directory(UPLOAD_DIR, filename)

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['input-img']
    if file and file.filename.endswith(ACCEPTED_EXTENSIONS):
        unique_filename = str(uuid.uuid4())
        unique_path = os.path.join(UPLOAD_DIR, unique_filename)
        try:
            file.save(unique_path)
            predictions = test([unique_path])
            return render_template("result.html", uploaded_img=unique_filename)
        finally:
            pass
            #os.remove(unique_filename)

def img_to_matrix(filename):
    img = Image.open(filename)
    img = img.resize(STANDARD_SIZE)
    img = list(img.getdata())
    img = map(list, img)
    img = np.array(img)
    return img

def flatten_image(img):
    s = img.shape[0] * img.shape[1]
    img_wide = img.reshape(1, s)
    return img_wide[0]

def visualize():
    pca = RandomizedPCA(n_components=2)
    X = pca.fit_transform(data)
    df = pd.DataFrame({"x": X[:, 0], "y": X[:, 1], "label":labels})
    colors = ["red", "yellow"]
    for label, color in zip(df['label'].unique(), colors):
        mask = df['label']==label
        pl.scatter(df[mask]['x'], df[mask]['y'], c=color, label=label)
    pl.legend()
    pl.show()

def train():
    images = [IMG_DIR + f for f in os.listdir(IMG_DIR) if f.endswith(ACCEPTED_EXTENSIONS)]
    labels = ["banana" if "banana" in f.split('/')[-1] else "human" for f in images]
    data = []
    for image in images:
        img = img_to_matrix(image)
        img = flatten_image(img)
        data.append(img)
    data = np.array(data)
    train = pca.fit_transform(data)
    knn.fit(train, labels)

def test(images=['static/images/banana_6.png']):
    test = []
    for image in images:
        img = img_to_matrix(image)
        img = flatten_image(img)
        test.append(img)
    test = np.array(test)
    test = pca.transform(test)
    return knn.predict(test)

if __name__ == '__main__':
    train()
    app.run(debug=True)
