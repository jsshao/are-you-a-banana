import os
import matplotlib.pyplot as pl
import numpy as np
import pandas as pd
from PIL import Image
from sklearn.neighbors import KNeighborsClassifier
from sklearn.decomposition import RandomizedPCA

STANDARD_SIZE = (300, 167)
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
    img_dir = "images/"
    images = [img_dir + f for f in os.listdir(img_dir)]
    labels = ["banana" if "banana" in f.split('/')[-1] else "human" for f in images]
    pca = RandomizedPCA(n_components=5)

    data = []
    for image in images:
        img = img_to_matrix(image)
        img = flatten_image(img)
        data.append(img)

    data = np.array(data)
    train = pca.fit_transform(data)
    test = pca.transform(test)
    knn = KNeighborsClassifier()
    knn.fit(train, labels)

def test(test=['david.jpg', 'banana_6.png']):
    for image in test:
        img = img_to_matrix(image)
        img = flatten_image(img)
        test.append(img)
    test = np.array(test)
    print knn.predict(test)
