import json
import re
import nltk
from nltk.corpus import stopwords

stop_words = set(nltk.corpus.stopwords.words('english'))

# f = open("yelp_academic_dataset_review.json", "r")
f = open("dataset.json", "r")

Lines = f.readlines()
counts = dict()


for line in Lines:    
    j_data = json.loads(line)
    # print(j_data['text'])
    sentence = j_data['text']
    words = sentence.split()
    for word in words:
        word = re.sub('[^a-zA-Z]+', '', word)
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1


filtered = dict()
for word in counts:
    if not word in stop_words:
        filtered[word] = counts[word]


print('Original', len(counts))
print('Filtered', len(filtered))
