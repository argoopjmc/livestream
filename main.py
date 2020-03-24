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
    dict_views = {
        "Guardian": 0,
        "Independent": 0,
        "Sun": 0,
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
    fig1, ax = plt.subplots()
    fig2, bx = plt.subplots()
    time_taken = 0
    while time_taken < max_time:
        views = get_views()
        try:
            print(views)
        except IndexError:
            plt.show()
        current_time = time.time()
        for x in views:
            ax.plot(time_taken, views[x], dict_colors[x])
            bx.plot(time_taken, views[x]/100, dict_colors[x])
            print(time_taken, " ", views[x])
        time.sleep(5)
        time_taken = round(current_time - start_time) / 60
        print(time_taken)

def main():
    plot(30, time.time())
    plt.show()

if __name__ == '__main__':
    main()
