import matplotlib.pyplot as plt
import json
import statistics
import math

# read input, parse linecound words
wc=[]
with open("yelp-1000.json", "r") as fp:
    while True:
        line = fp.readline()
        if not line:
            break
        review = json.loads(line)
        text = review["text"]
        wc.append(len(text.split(" ")))
        lenwc = len(wc)
        if lenwc % 10 == 0:
            print(f"read {lenwc} lines")

#print(wc)

wcmax = max(wc)
wcmin = min(wc)
wcmean = statistics.mean(wc)

# find variance
wcvar = 0
for w in wc:
    wcvar += (w - wcmean) ** 2
wcvar = wcvar / len(wc)
wcstddev = math.sqrt(wcvar)

print(wcmax, wcmin, wcmean, wcvar, wcstddev)


# generate gaussian distribution
dist=[]
wcmiddle = (wcmax - wcmin) / 2
for i in range(wcmin, wcmax):
    normval = 1 / (wcstddev * math.sqrt(2*math.pi)) * math.exp(-1/2 * (((i - wcmean)/wcstddev)**2))
    dist.append(normval)

normmax = max(dist)
print(normmax)
dist = [normval * (600 / normmax) for normval in dist]
plt.plot(range(wcmin, wcmax), dist)

n, x, _ = plt.hist(wc)  
#plt.savefig('foo.png')
plt.show()