# -*- coding: utf-8 -*-
"""RecommendationCourseUSE.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1OUvRRJu7L8Tz98uLpLUfOp2zl3kMMEiU
"""

import tensorflow as tf
import tensorflow_hub as hub
import matplotlib.pyplot as plt
import os
import re
import numpy as np
import pandas as pd

from sklearn.metrics.pairwise import cosine_similarity
from sklearn.neighbors import NearestNeighbors
from sklearn.decomposition import PCA

model_url = "https://tfhub.dev/google/universal-sentence-encoder/4"
model = hub.load(model_url)
print('Model Loaded')

def embed(texts):
    return model(texts)
embed(['Hinterland & Infrastructure Management'])

df = pd.read_csv("DatasetCourse.csv", engine="python")
df.head()

df = df[["Name", "Power Summary", "Platform"]]
df.head()

titles = list(df['Power Summary'])
titles[:1]

embeddings = embed(titles)
print('The embedding shape is:', embeddings.shape)

pca = PCA(n_components=2)
emb_2d = pca.fit_transform(embeddings)
plt.figure(figsize=(11, 6))
plt.title('Embedding space')
plt.scatter(emb_2d[:, 0], emb_2d[:, 1])
plt.show()

nn = NearestNeighbors(n_neighbors=10)
nn.fit(embeddings)

def recommend(text):
    emb = embed([text])
    neighbors = nn.kneighbors(emb, return_distance=False)[0]
    return df[['Name', 'Platform']].iloc[neighbors].values.tolist()

print('Recommended Course:')
recommend("Hinterland")