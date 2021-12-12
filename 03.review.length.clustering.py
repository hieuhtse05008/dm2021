import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
import json

documents = []
with open("./yelp_academic_dataset_review.json", "r") as f:
    for i,text in enumerate(f):
        #if(i==1000):
        #    break
        
        jsonText = json.loads(text)
        realText = jsonText['text']
        documents.append(realText)

data = [[len(doc.split())] for doc in documents]
kmeans = KMeans(3)
kmeans.fit(data)
clusters = kmeans.fit_predict(data)
print(len(clusters))
print(len(data)) 
plt.scatter(data,data,c=clusters,cmap='gist_rainbow')

plt.savefig("./03.review.length.clustering.png")