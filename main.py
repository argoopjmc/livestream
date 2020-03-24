import requests
import json
import time
from random import seed
from random import randint
from matplotlib import pyplot as plt

# these are IDs for the Sky News livestream please make sure you use the right ones for the event
API_KEY = "Obtain a key from the Google Cloud Platform and use it here"
dict_url = {
    "Guardian": "9Auq9mYxFEE",
    "Independent": "9Auq9mYxFEE",
    "Sun": "9Auq9mYxFEE",
    "ITV": "9Auq9mYxFEE",
    "Telegraph": "9Auq9mYxFEE",
}
dict_colors = {
    "Guardian": "m.",
    "Independent": "y.",
    "Sun": "k.",
    "ITV": "c.",
    "Telegraph": "r.",
    "Total_Views": "g.",
}

def create_url(stream_id):
    return "https://www.googleapis.com/youtube/v3/videos?part=liveStreamingDetails&id=" + stream_id + "&fields=items%2FliveStreamingDetails%2FconcurrentViewers&key=" + API_KEY

def get_views():
    dict_views = {
        "Guardian": 0,
        "Independent": 0,
        "Sun": 0,
        "ITV":0,
        "Telegraph": 0,
        "Total_Views": 0,
    }
    total_views = 0
    for x in dict_url.keys():
        r = requests.get(url=create_url(dict_url[x]))
        data = r.json()
        dict_views[x] = int(data['items'][0]['liveStreamingDetails']['concurrentViewers'])
        total_views += dict_views[x]
        dict_views['Total_Views'] = total_views
    return dict_views

def plot(max_time, start_time):
    seed(2)
    bojostats, ax = plt.subplots()
    time_taken = 0
    while time_taken < max_time:
        try:
          views = get_views()
          print(views)
        except IndexError:
          #as a precaution
          ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05), shadow=True, ncol= len(dict_colors))
          plt.show()
        current_time = time.time()
        for x in views:
            if(time_taken ==0):
              ax.plot(time_taken, views[x], dict_colors[x], label = x)
              ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05), shadow=True, ncol= len(dict_colors))
            else:
              ax.plot(time_taken, views[x], dict_colors[x])
            print(time_taken, " ", views[x])
        time.sleep(5 + randint(0,10))
        time_taken = round(current_time - start_time) / 60
        print(time_taken)

def main():
    plot(1, time.time())
    plt.show()

if __name__ == '__main__':
    main()
