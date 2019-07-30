import requests
import json
import os
from pandas.io.json import json_normalize
import datetime
import pandas as pd
import sys

fileObject = open('ios_genre.txt', 'w')


for row in sys.stdin:
    for i in range(100):
        
        appname = json.loads(row)['app_list'][i]['bundleId'].split('.')[-1]
        genrelist = json.loads(row)['app_list'][i]['genre'][-1]
        review = json.loads(row)['app_list'][i]['review analysis']
        
        fileObject.write("%s,%s,%s\n"%(appname,genrelist,str(review))
        #break  
    #break
fileObject.close()