#!/usr/bin/env python

from _pybgpstream import BGPStream, BGPRecord, BGPElem
import sys
# Create a new bgpstream instance and a reusable bgprecord instance

letter = sys.argv[1]
prefix = sys.argv[2]
startTime = int(sys.argv[3])
endTime = int(sys.argv[4])

print letter, prefix, startTime, endTime

stream = BGPStream()
rec = BGPRecord()


# startTime = 1448841600
timeinterval = 10*60 #seconds
timePeriod = [0 for x in range(48*3600/timeinterval)]
probeidToTimeStamp = []
x = 0
xAxis = [y for y in range(0,48*60,10)]



# Consider RIPE RRC 10 only
stream.add_filter('collector','route-views2')
stream.add_filter('record-type','updates')

stream.add_filter('prefix',prefix)
# Consider this time interval:

# Sat Aug  1 08:20:11 UTC 2015
stream.add_interval_filter(startTime,endTime)
# stream.add_interval_filter(1448841600,1448841600)

# Start the stream
stream.start()

# Get next record
while(stream.get_next_record(rec)):
    # Print the record information only if it is not a valid record
    if rec.status != "valid":
        print rec.project, rec.collector, rec.type, rec.time, rec.status
    else:
        elem = rec.get_next_elem()
        while(elem):
            # Print record and elem information
            print rec.project, rec.collector, rec.type, rec.time, rec.status, elem.type, elem.fields
            y = (int(elem.time) - startTime)/(10*60)
       

            timePeriod[y] = timePeriod[y]+1     

            elem = rec.get_next_elem()


print timePeriod
A = open(str(letter)+"_bgpupdates_route-views2_June25th.csv", 'a+')
index = 0
for v in timePeriod:  
    A.write('%s,%s\n'% (xAxis[index],v))
    index=index+1

