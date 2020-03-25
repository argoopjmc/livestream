import requests
import json
import time
from datetime import datetime
from random import seed,randint
from matplotlib import pyplot as plt

file_name = datetime.now().strftime("%d-%m-%Y@%H.%M.%S") + "_LiveStreamStats.json"
print(file_name)


# these are IDs for the Sky News livestream please make sure you use the right ones for the event
API_KEY = "Put your own key here"
dict_url = {
    "Guardian": "9Auq9mYxFEE",
    "Independent": "",
    "Sun": "9Auq9mYxFEE",
    "ITV": "9Auq9mYxFEE",
    "Telegraph": "9Auq9mYxFEE",
    "Sky News":"9Auq9mYxFEE",
}
clean_url_dict = {key: value for (key, value) in dict_url.items() if value != "" }
dict_colors = {
    "Guardian": "m.",
    "Independent": "y.",
    "Sun": "k.",
    "ITV": "c.",
    "Telegraph": "r.",
    "Sky News": "b." ,
    "Total_Views": "g.",
}

def create_url(stream_id):
    return "https://www.googleapis.com/youtube/v3/videos?part=liveStreamingDetails&id=" + stream_id + "&fields=items%2FliveStreamingDetails%2FconcurrentViewers&key=" + API_KEY

def get_views():
    dict_views = {
        'Guardian': 0,
        'Independent': 0,
        'Sun': 0,
        'ITV':0,
        'Telegraph': 0,
        'Sky News' : 0,
        'Total_Views': 0,
    }
    total_views = 0
    for x in clean_url_dict.keys():
        r = requests.get(url=create_url(clean_url_dict[x]))
        data = r.json()
        print(data)
        dict_views[x] = int(data['items'][0]['liveStreamingDetails']['concurrentViewers'])
        total_views += dict_views[x]
        dict_views['Total_Views'] = total_views
    return dict_views

def plot(max_time, start_time):
    seed(2)
    bojostats, ax = plt.subplots()
    plt.xlabel("Time in minutes from " + datetime.now().strftime("%d/%m/%Y@%H:%M:%S"))
    plt.ylabel("Viewers")
    time_taken = 0
    dump = open(file_name,'w')
    data_dump = {}
    get_id = 1
    while time_taken < max_time:
        try:
          curr_datetime = datetime.now().strftime("%d/%m/%Y-%H:%M:%S")
          views = get_views()
          print(curr_datetime," ",get_id ," ",views)
          get_id +=1
          views_datetime_dict = {curr_datetime:views}
          data_dump.update(views_datetime_dict)
        except IndexError:
          #as a precaution
          print("At least one event has ended")
          ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05), shadow=True, ncol= len(clean_url_dict) + 1)
          plt.show()
        current_time = time.time()
        for x in views:
            if(views[x] !=0):
              if (time_taken == 0):
                ax.plot(time_taken, views[x], dict_colors[x], label = x)
                ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05), shadow=True, ncol= len(clean_url_dict) + 1)
              else:
                ax.plot(time_taken, views[x], dict_colors[x])
        time.sleep(5 + randint(0,10))
        time_taken = round(current_time - start_time) / 60
    print(len(data_dump))
    json.dump(data_dump,dump)
    dump.close()

def main():
    plot(2, time.time())
    plt.show()

if __name__ == '__main__':
    main()
