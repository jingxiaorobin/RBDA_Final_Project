import json
import sys
import datetime
count  = -1
def time(beginday = 1,beginmon = 7,endday = 20,endmon = 7):
    day_list = []
    begin = datetime.date(2019,beginmon,beginday)
    end = datetime.date(2019,endmon,endday)
    for i in range((end - begin).days+1):
        day = begin + datetime.timedelta(days=i)
        new_day = datetime.datetime.strptime(str(day), "%Y-%m-%d").strftime("%d-%m-%Y")
        day_list.append(str(new_day))
    return day_list
datelist = time()

for line in sys.stdin:
    a = line.strip()
    dic = eval(a)
    count+=1
    
    date = datelist[count//3]
    for i in range(len(dic)):
        genres = dic[i]['genres']
        review_analysis = dic[i]['review_analysis']['topics']
        price = dic[i]['price']
        name = dic[i]['trackCensoredName']
        age = dic[i]['trackContentRating']
        for j in range(len(review_analysis)):
            print(name, \
                  genres,  \
                  age,\
                  price,\
                  review_analysis[j]['topic_id'],\
                  review_analysis[j]['average_rating'],\
                  review_analysis[j]['reviews_percentage'],\
                  review_analysis[j]['positive'])
            

     #   The output of the  mapper is 
    #Game name(pokemon go), 
    #genres([Health%fitness, role-playing],  
    #age ( for 4+, 12+)
    #price(0=free),
    
    #review analysis:
        #topic: update/stability
        #average_rating: rating towards the topic review
        #review_percentage
        #positive towards review topic
    
