import requests
import json
import os
#from pandas.io.json import json_normalize
import datetime
#import pandas as pd
import sys

fileObject = open('ios_genre.txt', 'w')

count = 0
for row in sys.stdin:
    count +=1
    try:
        row = eval(row)
        
        for i in range(100):

            #print(row[i].keys())

            appname = row[i]["trackCensoredName"]

            genrelist = row[i]['genres'][-1]
            if  genrelist != 'Game':
            #review = row[i]['review_analysis']
                fileObject.write("%s,%s"%(appname,genrelist))
            #fileObject.write("%s,%s,%s"%(appname,genrelist,str(review)))
                fileObject.write("\n")

            try:
                genrelist = row[i]['genres'][-2]
            except IndexError:
                pass
            if  genrelist != 'Game':
                fileObject.write("%s,%s"%(appname,genrelist))
                fileObject.write("\n")
    except SyntaxError:
        pass
       
    print(count)
  
fileObject.close()
