#cat ios_review_final.txt | python ios_result3_review_ana.py
import requests
import json
import os
import datetime
import sys

total_attitude = {}
total_rating = {}
total_weight = {}
topics = []
count = 0

for row in sys.stdin:
    (genre,name,positive,topicname,negative,reviewnum,rating,topicid,weight) = row.split(',')
    
    if genre =="Puzzle": # "Adventure" or "Puzzle"
        
        
        if topicid not in topics:
            topics.append(topicid)
            total_attitude[topicid] = {}
            total_rating[topicid] ={}
            total_weight[topicid] ={}
            
            total_attitude[topicid]['score']= float(positive)
            total_attitude[topicid]['count']= 1
            total_rating[topicid]['score']= float(rating)
            total_weight[topicid]['score']= float(weight)
            
        else:
            total_attitude[topicid]['score'] += float(positive)
            total_attitude[topicid]['count'] += 1
            total_rating[topicid]['score'] += float(rating)
            total_weight[topicid]['score'] += float(weight)
        
for t in topics:
    print("weight: %s, Topic: %s, Avg Positive attitude:%s, Avg Rating: %s, "%(total_weight[t]['score'],t, total_attitude[t]['score']/total_attitude[t]['count'],total_rating[t]['score']/total_attitude[t]['count']) )  
        
   
