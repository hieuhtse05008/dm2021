import random
import utils
from utils import Point, Cluster

wc = utils.loadData()

points = [Point(x) for x in wc]

K = 3

centroids = [random.choice(points) for i in range(0, K)]

while True:
    clusters = [Cluster() for i in range(0, K)]
    for p in points:
        distances = [p.dist(centroid) for centroid in centroids]
        argMin = distances.index(min(distances))
        clusters[argMin].addPoint(p)

    #print(clusters)
    newCentroids = [Point(c.getCentroid()) for c in clusters]
    #print(f"Centroids: {[c.getCentroid for c in clusters]}")
    centroidsDiffs = []
    for c1, c2 in zip(centroids, newCentroids):
        centroidsDiffs.append(c1.dist(c2))

    sse = 0
    for dif in centroidsDiffs:
        sse += dif ** 2
    centroids.clear()
    centroids = newCentroids
    if sse < 1:
        print("Stop")
        print(f"{[len(c.points) for c in clusters]}")
        break
    
