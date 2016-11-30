import base64
import json
from pprint import pprint
import os
import sys

if (len(sys.argv) !=3):
	print "ERROR: Please name both parse file and output file"
	quit()


with open(sys.argv[1]) as json_data:
  data = json.load(json_data)
  json_data.close()

f = open(sys.argv[2], 'a+')

# Total of objects in the JSON file
pr = len(data)
print 'Lenght %d' % pr
index = -1
c_hit = 0
c_err = 0
for res in data:
  index += 1

  if not res.get('error'):
    if data[index]['result'].get('answers')  and data[index]['timestamp']:
      c_hit += 1
      f.write('%s,%s,%s,%s,%s,%s,%s\n' % (data[index]['from'], data[index]['dst_addr'], data[index]['proto'], str(data[index]['result']['answers'][0]['RDATA'][0]), data[index]['result']['rt'], data[index]['prb_id'], data[index]['timestamp']))
    else:
      c_err += 1
  else:
    c_err += 1

f.close()

# Just print some stats
print 'total CHAOS %d' % index
print 'total hits  %d' % c_hit
print 'total error %d' % c_err

