import re
from collections import defaultdict
import matplotlib.pyplot as plt
import numpy as np
# import statistics


f = open('probesList','rt')
count = 0
astoProbeID = defaultdict(list)


for line in f:
	str = re.sub( '\s+', ' ', line ).strip()
	string_split = str.split(' ')
	if len(string_split) >= 4 and string_split[2] != "Never":
		# print str
		count = count + 1
		# print string_split[0],string_split[1]
		astoProbeID[string_split[1]].append(string_split[0])




# print astoProbeID.items()
numVPsPerAS = []
countNumVPsPerAS = [0 for x in range(100)]
xAxis = [y for y in range(0,100)]
for key, value in astoProbeID.items():
	count = len(value)
	print key,count
	numVPsPerAS.append(count)
	if count >= 100:
		count = 99
	countNumVPsPerAS[count] = countNumVPsPerAS[count] + 1 

print numVPsPerAS
sortedNumVpsPerAS = sorted(numVPsPerAS,reverse=True)
print sortedNumVpsPerAS
# hist, bins = np.histogram(numVPsPerAS, bins=100)
# plt.hist(numVPsPerAS,1000)
# plt.plot(hist)
plt.axis([0, 100, 0, 10])
# plt.xlabel("Number of VPs",fontsize="18")
# plt.ylabel("Frequency of AS per X VPS",fontsize="18")
# plt.title("Distribution of VPs across ASes", fontsize="18")
print "Max: %d" % max(numVPsPerAS)
print "Median: %d" % np.median(numVPsPerAS) 


fig = plt.figure(1, figsize=(9, 6))

# Create an axes instance
ax = fig.add_subplot(111)

# Create the boxplot
bp = ax.boxplot(numVPsPerAS)
# width = 0.7 * (bins[1] - bins[0])
# center = (bins[:-1] + bins[1:]) / 2
# plt.bar(center, hist, align='center', width=width)
plt.show()
print count		