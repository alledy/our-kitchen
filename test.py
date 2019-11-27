from django.shortcuts import render
from .models import Kitchen_info, Reservation_time
import urllib.request
import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# import mathplot
import folium
from folium import plugins
from decouple import config
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required

def radius(request,lng,lat):
    token = config('TOKEN')
    url = f'http://apis.data.go.kr/B553077/api/open/sdsc/storeListInRadius?radius=2000&cy={lng}&cx={lat}&ServiceKey={token}'
    response = requests.post(url).json()["indsSclsNm"]
    info = response.get()
    plt.pie(info)