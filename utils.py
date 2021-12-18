import json
import statistics


def loadData(limit = 0):
    documents = []
    with open("./yelp_academic_dataset_review.json", "r") as f:
        for i, text in enumerate(f):
            if(limit > 0 and i == limit):
                break

            jsonText = json.loads(text)
            realText = jsonText['text']
            documents.append(realText)

    data = [len(doc.split()) for doc in documents]
    return data


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
                d = self.policy(d, p1.dist(p2))
        return d

    def merge(self, _c):
        self.points += _c.points

    def __repr__(self):
        return f"{[p.x for p in self.points]}"
    def getCentroid(self):
        return self.policy([p.x for p in self.points])
    

def getDist(p):
    return p['dist']
