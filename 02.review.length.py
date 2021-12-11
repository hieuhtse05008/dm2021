import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
import json

documents = []
with open("./yelp_academic_dataset_review.json", "r") as f:
    i = 0
    for text in f:
        #if(i==1000):
        #    break
        i+=1
        jsonText = json.loads(text)
        realText = jsonText['text']
        documents.append(realText)

doc_lengths = [len(doc.split()) for doc in documents]
#print(doc_lengths)
density = stats.gaussian_kde(doc_lengths)
n, x, _ = plt.hist(doc_lengths)  
plt.plot(x, density(x))
plt.savefig("./02.review.length.png")