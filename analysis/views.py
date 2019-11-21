from django.shortcuts import render
from .models import Kitchen_info, Reservation_time
import urllib.request
import requests
import pandas as pd
import numpy as np
# import mathplot
import folium
from decouple import config

token = config('TOKEN')

def kitchen_map(request,lat,lng):
    map = folium.Map(location=[37.5502, 126.982], zoom_start=11)

#     for n in location_raw.index:
#         folium.Marker([location_raw['lat'][n], 
#         location_raw['lng'][n]], popup= location_raw['kitchen_name'][n]], icon = folium.icon(color ='red')).add_to(map)

def radius(request,lat_info,lng_info):
    token = config('TOKEN') 
    url = f'http://apis.data.go.kr/B553077/api/open/sdsc/storeListInRadius?radius={choosen_radius}&cy={long_info}&cx={lat_info}&ServiceKey={token}'
    response = requests.post(url).json()
    response.get()

# def Rectangle_analysis(request,lat,lng)
