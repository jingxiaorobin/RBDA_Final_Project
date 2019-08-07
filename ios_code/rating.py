import requests
import json
import os
#from pandas.io.json import json_normalize
import datetime
#import pandas as pd
import sys

fileObject = open('ios_avg_rating.txt', 'w')

count = 0
for row in sys.stdin:
    count +=1
    print(count)
    try:
        row = eval(row)
        
        for i in range(100):
            appname = row[i]["trackCensoredName"]

            rating = row[i]["averageUserRating"]
           
            fileObject.write("%s,%s"%(appname,rating))
            fileObject.write("\n")
    except SyntaxError:
        pass
       
    
  
fileObject.close()
