import requests
import json
import os
from pandas.io.json import json_normalize
import datetime
import pandas as pd

API_key1 = 'd0fbd94503166e7d63c5bbb48fb3ee7da6b72318'
API_key2 = '10092e1cf5c2e2373954f90c5972e0fd9ee4913b'
API_key3 = 'f1a4314631d9806db00eb4e72430d2413f3f9160'

def time(beginday = 19,beginmon = 7,endday = 20,endmon = 7):
    day_list = []
    begin = datetime.date(2019,beginmon,beginday)
    end = datetime.date(2019,endmon,endday)
    for i in range((end - begin).days+1):
        day = begin + datetime.timedelta(days=i)
        new_day = datetime.datetime.strptime(str(day), "%Y-%m-%d").strftime("%d-%m-%Y")
        day_list.append(str(new_day))
    return day_list

def json_extract_line(api,list_name = 'topselling_paid',date = '20-07-2019'):
    toplink = 'https://data.42matters.com/api/v2.0/ios/apps/top_appstore_charts.json?\
list_name=' + list_name + '&\
primaryGenreId=6014&\
device_type=iphone&\
country=US&\
limit=100&\
date=' + date +'&\
access_token='+api
    
    temp = requests.get(toplink)
    df = temp.json()['app_list']
    df['list_name'] = list_name
    df['date'] = date
    
    return df



#take default para: 20190701-0720
daylist = time()

#take top 10 app for free game/paid game/general game
#list_names = ['topselling_free','topselling_paid','topgrossing']
list_name = 'topgrossing'
fileObject = open('ios_game.txt', 'w')
count = 0
api = API_key1

for date in daylist:
    
    top_table = json_extract(api, list_name = list_name, date = date)
    count += 1
    if count <190: #each api have only 200 request per day
        fileObject.write(str(top_table))
    fileObject.write('\n')
    elif count <380:
        api = API_key2
    elif:
        api = 570
    else:
        break
    print(date)
fileObject.close()

#write to txt file, each line is one top10
#method 1: run local and copy to HDFS
# $scp ios_game_07.json xj655@dumbo.es.its.nyu.edu:/home/xj655

# $hdfs dfs -mkdir /user/xj655/project
# $hdfs dfs -put ios_game_07.json project

#method 2: run script on Dumbo
