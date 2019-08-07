#Find the topic mentioned with the most frequency for each app game
import json
import sys

app_list = {}
avg_rating = 0
for line in sys.stdin:
    a = line.strip()
    
    name, b = a.split('[')
    genres,  c= b.split(']')
    age, price, date, topic, average_rating, review_percentage, positive= c.strip().split(' ')
    
    if name not in app_list.keys() and topic != 'general_feedback':
        app_list[name] = topic
        app_list[name+'_rate'] = float(average_rating)
    else:
        if float(average_rating) > app_list[name+'_rate'] and topic != 'general_feedback':
            app_list[name] = topic
            app_list[name+'_rate'] = float(average_rating)
        else:
            continue
for key in app_list.keys():
    if key.endswith('te') == False:
        print key, app_list[key]
 