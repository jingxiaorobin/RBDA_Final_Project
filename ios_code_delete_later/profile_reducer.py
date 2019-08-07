import json
import sys
from collections import Counter

name_l = []
genres_l = []
age_l = []
price_l = []

topic_l = []
average_rating_l = []
review_percentage_l = []
positive_l = []

for line in sys.stdin:
    a = line.strip()
    
    name, b = a.split('[')
    genres,  c= b.split(']')
    age, price,  topic, average_rating, review_percentage, positive= c.strip().split(' ')
    
    name_l.append(name)
    genres_l.append(genres)
    age_l.append(age)
    price_l.append(float(price))
    
    topic_l.append(topic)
    average_rating_l.append(float(average_rating))
    review_percentage_l.append(float(review_percentage))
    positive_l.append(positive)
    print(name)
#print(len(list(set(name_l))))#print(name_l)
print('The total game number is %s, genres includes %s, the highest price is %s, the topic number is %s, max average rating about one topic is %s, max positive attitude towards one topic is %s'%(len(list(set(name_l))),  len(list(set(genres_l))), len(price_l), len(list(set(topic_l))),max(average_rating_l), max(positive_l)))
