import osmnx as ox
import requests
from bs4 import BeautifulSoup as bs
import json

from geopy.distance import geodesic

CKAD_distance = 60



url = None

def pars_time_and_path(url):
    url = url
    response = requests.get(url)
    response_json =json.loads(response.text)
    paths = response_json["paths"]
    km_path = round(paths[0]['distance'] / 1000)
    time = paths[0]['time'] // (60)
    return km_path, time


def calculetion_of_price(client_K, finish_K):

    distance1  = geodesic(55.755799, 37.617617, client_K).kilometers
    distance2  = geodesic(55.755799, 37.617617, finish_K).kilometers

    final_price = None

    with open('russia_graph2.gpkg', 'r') as file:
        G = file.read()
    with open('Moscow_city.txt', 'r') as file:
        Moscow_MCAD = file.read()
    with open('Moscow_oblast.txt', 'r') as file:
        Moscow_oblast = file.read()
    klient_node = ox.nearest_nodes(G, client_K[0], client_K[1])
    finish_node = ox.nearest_nodes(G, finish_K[0], finish_K[1])

    if CKAD_distance - distance1 < 0 and finish_node in Moscow_MCAD:
        pass

    elif CKAD_distance - distance2 < 0 and klient_node in Moscow_MCAD:
        pass

    elif klient_node and finish_node in Moscow_MCAD:
        km_path, time = pars_time_and_path(url)
        final_price = 1500
        if time // 60 > 1:
            min_price = (time - 60) * 15
            final_price += min_price
            return final_price
        
    elif klient_node in Moscow_MCAD and finish_node in Moscow_oblast:
        pass
    
    elif finish_node in Moscow_MCAD and klient_node in Moscow_oblast:
        pass
    

