import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
import json

documents = []
with open("./yelp_academic_dataset_review.json", "r") as f:
    for i, text in enumerate(f):
        if(i == 10):
            break

        jsonText = json.loads(text)
        realText = jsonText['text']
        documents.append(realText)

data = [len(doc.split()) for doc in documents]
#kmeans = KMeans(3)
# kmeans.fit(data)
#clusters = kmeans.fit_predict(data)
# print(len(clusters))
# print(len(data))
# plt.scatter(data,data,c=clusters,cmap='gist_rainbow')

# plt.savefig("./03.review.length.clustering.png")


class Point:
    def __init__(self, x) -> None:
        self.x = x

    def dist(self, _p):
        return abs(self.x - _p.x)


class Cluster:
    def __init__(self, policy=min):
        self.points = []
        self.policy = policy

    def addPoint(self, p):
        self.points.append(p)

    def dist(self, _c):
        d = 0
        if(self.policy == min):
            d = float('inf')
        else:
            d = -1
        for p1 in self.points:
            for p2 in _c.points:
                d = self.policy(d,p1.dist(p2))
        return d
    def merge(self, _c):
        self.points += _c.points
    def __repr__(self):
        return f"{[p.x for p in self.points]}"
        
def getDist(p):
    return p['dist']     

clusters = []
for doc_len in data:
    c = Cluster()
    p = Point(doc_len)
    c.addPoint(p) 
    clusters.append(c)
idx=0
while True:
    distances = []
    for c1 in clusters:
        for c2 in clusters:
            if(c1 != c2):
                dist=c1.dist(c2)
                distances.append({
                    'c1':c1,
                    'c2':c2,
                    'dist':dist
                })    
    minDist = min(distances, key= getDist)
    minDist['c1'].merge(minDist['c2'])            
    clusters.remove(minDist['c2'])
    idx+=1
    print(f"Iteration {idx} ({len(clusters)}) {clusters}")
    if(len(clusters) == 3): break



#plt.scatter(data, data, c=idx_clusters, cmap='gist_rainbow')
#plt.savefig("./03.review.length.clustering.png")
