import requests
import json
import time
from matplotlib import pyplot as plt

# these are IDs for random livestreams please make sure you use the right ones
API_KEY = "Put your own API Key here after obtaining it from the Google Cloud Platform"
dict_url = {
    "Guardian": "5qap5aO4i9A",
    "Independent": "_QNJA_wFn-o",
    "Sun": "Ino3ZmHhDLI",
    "Telegraph": "qgylp3Td1Bw",,
}
dict_views = {
    "Guardian": 0,
    "Independent": 0,
    "Sun": 0,
    "Telegraph": 0,
    "Total_Views": 0,
}
dict_colors = {
    "Guardian": "m.",
    "Independent": "y.",
    "Sun": "k.",
    "Telegraph": "r.",
    "Total_Views": "g.",
}

def create_url(stream_id):
    return "https://www.googleapis.com/youtube/v3/videos?part=liveStreamingDetails&id=" + stream_id + "&fields=items%2FliveStreamingDetails%2FconcurrentViewers&key=" + API_KEY

def get_views():
    total_views = 0
    for x in dict_url:
        r = requests.get(url=)
        data = r.json()
        dict_views[x] = int(data['items'][0]['liveStreamingDetails']['concurrentViewers'])
        total_views += dict_views[x]
        dict_views['Total_Views'] = total_views
    return dict_views

def plot(max_time, start_time):
    fig1, ax = plt.subplots()
    fig2, bx = plt.subplots()
    curr_time = 0
    while curr_time < max_time:
        try:
            print(get_views())
        except IndexError:
            plt.show()
        getviews = get_views()
        end_time = time.time()
        for x in getviews:
            ax.plot(curr_time, getviews[x], dict_colors[x])
            bx.plot(curr_time, getviews[x]/100, dict_colors[x])
            print(curr_time, " ", getviews[x])
        time.sleep(5)
        curr_time = round(end_time - start_time) / 60
        print(curr_time)

def showgrph():
    plt.show()

if __name__ == '__main__':
    start = time.time()
    plot(30)
    showgrph()
