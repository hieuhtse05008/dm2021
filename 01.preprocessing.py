import json


# f = open("yelp_academic_dataset_review.json", "r")
f = open("dataset.json", "r")

Lines = f.readlines()
counts = dict()
count = 0
# Strips the newline character
for line in Lines:
    count += 1
    if count > 10:
        break
    j_data = json.loads(line)
    print(j_data['text'])
    sentence = j_data['text']
    words = sentence.split()
    for word in words:
        
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

print(count)