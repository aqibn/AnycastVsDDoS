import matplotlib.pyplot as plt
import sys



startTime = 1466877600
letter = arg1 = sys.argv[1]
print letter
timeinterval = 10*60 #seconds
probe_dict = {}

timePeriod = [0 for x in range(10*3600/timeinterval)]
probeidToTimeStamp = []
x = 0
xAxis = [y for y in range(0,10*60,10)]
A = open(str(letter)+"reachability.csv", 'a+')
for x in range(1, 5):
	print x
	with open(str(letter)+"rootparsed"+str(x), "rt") as f:
		for line in f:
			x = line.split(',')
			probeidToTimeStamp.append([x[5],x[6]])

probeidToTimeStamp = sorted(probeidToTimeStamp, key=lambda x: x[1])


for x in probeidToTimeStamp:
	# print x
	if x[0] in probe_dict:
		lastProbe = probe_dict[x[0]]
		y = (int(x[1]) - startTime)/(10*60)
		if lastProbe == y:
			continue
		else: 
			probe_dict[x[0]] = y
	y = (int(x[1]) - startTime)/(10*60)
	probe_dict[x[0]] = y
	        # print "index %d" % y 

	timePeriod[y] = timePeriod[y]+1		

	        # print 'total  %s' % x[3]
	       
	        # print "count %d" %   timePeriod[y] 
                   
print timePeriod
index = 0
for v in timePeriod:  
	A.write('%s,%s\n'% (xAxis[index],v))
	index=index+1
A.close()
# print probeidToTimeStamp[:][10:100]

xAxis[:] = [x / 60 for x in xAxis]

# plt.plot(xAxis, timePeriod)
# plt.axis([0, 7.5, 0, 10000])
# plt.savefig(str(letter)+'root.png')
# plt.show()