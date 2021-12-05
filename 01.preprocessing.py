import json
import re
import nltk
from nltk.corpus import stopwords
import math

# stopwords
stop_words = set(nltk.corpus.stopwords.words('english'))

# read file
# f = open("yelp_academic_dataset_review.json", "r")
f = open("dataset.json", "r")
documents = f.readlines()

# get words
counts = dict()

for line in documents:    
    j_data = json.loads(line)
    # print(j_data['text'])
    sentence = j_data['text']
    words = list(set(sentence.split()))
    for word in words:        
        word = re.sub('[^a-zA-Z\']+', '', word)
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

# remove stopwords
filtered = dict()
for word in counts:
    if not word in stop_words:
        filtered[word] = counts[word]
# for word in counts:
    # print(word)
print('Original', len(counts))
print('Filtered', len(filtered))

# compute tf - idf
tfs = dict()
idfs = dict()
tf_idfs = dict()
for word in filtered:
    tfs[word] = filtered[word]/len(documents)

for word in filtered:    
    idfs[word] = math.log(1/tfs[word])
    
for word in filtered:    
    tf_idfs[word] = tfs[word]*idfs[word]


sorted = sorted(tf_idfs.items(), key=lambda x: x[1])

for word in tf_idfs:    
    print(word, tf_idfs[word])