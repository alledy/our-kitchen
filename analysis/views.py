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

token = config('TOKEN')

def kitchen_map(request):
    kitchens = Kitchen_info.objects.all()
    map = folium.Map(location=[37.5502, 126.982], zoom_start=11)   
    for kitchen in kitchens:
        name = kitchen.kitchen_name
        folium.Marker([kitchen.lat, kitchen.lng], popup=name).add_to(map)
    map.save(outfile='analysis/templates/analysis/icon.html') 
    return render(request, 'analysis/test.html', {'map':map})

# def create_info(request):
#     if request.method == 'POST':
#         Form = Kitchen_infoForm(request.POST, request.FILES)
#         if Form.is_valid():
#             kitchen = form.save(commit=False)
#             kitchen.save()
#             return redirect('analysis:detail', Kitchen_info.id)

def radius(request,lng,lat):
    token = config('TOKEN')
    url = f'http://apis.data.go.kr/B553077/api/open/sdsc/storeListInRadius?radius=2000&cy={lng}&cx={lat}&ServiceKey={token}'
    response = requests.post(url).json()["indsSclsNm"]
    info = response.get()
    plt.pie(info)
    
    
    
# def Rectangle_analysis(request,lat,lng)
