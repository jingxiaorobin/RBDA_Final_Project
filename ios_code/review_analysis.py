import requests
import json
import os
import datetime
import sys

fileObject = open('ios_review.txt', 'w')

count = 0
for row in sys.stdin:
    count +=1
    try:
        row = eval(row)
        
        for i in range(100): # each day top 100 app
            appname = row[i]["trackCensoredName"]
            try:
                topicnumber = row[i]["review_analysis"]["number_topics"]
                for j in range(topicnumber):
                    topic = row[i]["review_analysis"]["topics"][j]
                    for a,x in enumerate(topic.keys()):
                        name='v'+str(a)
                        locals()['v'+str(a)]=topic[x]
                    fileObject.write("%s,%s,%s,%s,%s,%s,%s,%s"%(appname,v0,v1,v2,v3,v4,v5,v6))   
                    fileObject.write("\n")
            except KeyError:
                pass
    except SyntaxError:
        pass
       
    print(count)
  
fileObject.close()

#cat ios_test.txt | python review_analysis.py