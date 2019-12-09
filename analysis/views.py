from django.shortcuts import render, redirect
from .models import Kitchen_info, Start_up, move_pop, stay_pop
import urllib.request
import requests
import pandas as pd
import numpy as np
from pandas import DataFrame
import matplotlib.pyplot as plt
# import mpld3
from matplotlib import rcParams
import folium
from folium import plugins
from decouple import config
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from collections import Counter
import json
import sqlite3


token = config('TOKEN')
# 소상공인 API


def kitchen_map(request):
    kitchens = Kitchen_info.objects.all()
    name = list()
    lng = list()
    lat = list()
    for kitchen in kitchens:
        name.append(kitchen.kitchen_name)
        lng.append(kitchen.lng)
        lat.append(kitchen.lat)
    return render(request, 'analysis/test.html', {'name': name, "lng": lng, "lat": lat})


def kitchen_map2(request):
    kitchens = Kitchen_info.objects.all()
    name = list()
    lng = list()
    lat = list()
    for kitchen in kitchens:
        name.append(kitchen.kitchen_name)
        lng.append(kitchen.lng)
        lat.append(kitchen.lat)
    return render(request, 'analysis/test1.html', {'name': name, "lng": lng, "lat": lat})

# 맵 생성


def radius(request, lat, lng):
    token = config('TOKEN')
    store_id = list()
    store_code = list()
    store_lon = list()
    store_lat = list()
    street_name = list()
    map = folium.Map(location=[lat,lng], zoom_start=14)
    for j in range(1, 30):
        url = f'http://apis.data.go.kr/B553077/api/open/sdsc/storeListInRadius?radius=500&cx={lng}&cy={lat}&ServiceKey={token}&type=json&indsLclsCd=Q&pageNo={j}'
        # url = f'http://apis.data.go.kr/B553077/api/open/sdsc/storeListInRadius?radius=500&cx={lng}&cy={lat}&ServiceKey={token}&type=json&indsLclsCd=Q&pageNo=2'
        res = requests.get(url).json()
        if res["header"]["resultCode"] != '00':
            break
        # map_list = list()
        times = len(res["body"]["items"])
        for i in range(times):
            store_id.append(res["body"]["items"][i]["bizesId"])
            store_code.append(res["body"]["items"][i]["indsMclsNm"])
            store_lon.append(res["body"]["items"][i]["lon"])
            store_lat.append(res["body"]["items"][i]["lat"])

######################################################################
        if Start_up:
            #area = res["body"]["items"][0]["signguCd"]
            area_name = res["body"]["items"][0]["signguNm"]
            # area_name2 = area_name.split(' ')[2]
            # start_up = Start_up.objects.all()
            # start_up = Start_up.objects.filter(signgunm = area_name)
            start_up = Start_up.objects.get(signgunm = area_name)
            close = start_up.close
            remain_term = start_up.remain_term 
            plma = start_up.plma
            danger = start_up.danger
        # 구별 창업지수를 필터하기 위한 식
            street_name = res["body"]["items"][i]["rdnm"]
            street_name1 = area_name.split(' ')[2]
            if street_name1 in stay_pop:
                break
            print(street_name1)
            move_info = move_pop.objects.get(rdnm = street_name1)
            move_info
                
        # 도로명에 따른 상주인구와 유동인구 정보를 분류

    #가게별 코드별 유니크 이름으로 분류하고, 해당 빈도 값을 만드는 식  
    store_code_unique = pd.unique(store_code)
    piechart_value = Counter(store_code)
    pie_keys = list(piechart_value.keys())
    print(pie_keys)
    pie_values = piechart_value.values()
    print(pie_values)
    return render(request, 'analysis/radius.html',{'move_info':move_info,'pie_keys':pie_keys,'pie_values':pie_values,'danger':danger,'lat':lat,'lng':lng,'store_id':store_id,'store_code':store_code,'store_lon':store_lon,'store_lat':store_lat, 'close':close, 'remain_term':remain_term, 'plma':plma })
   

#     #상주인구의 지역코드와 info3가 같다면
#         label = ['총상주인구', '남성_total', '여성_total', '20대_total', '30대_total', '40대_total', '50대_total', '60대_total', '남성_20', '남성_30', '남성_40', '남성_50', '남성_60', '여성_20', '여성_30', '여성_40', '여성_50', '여성_60']
#         plt.rcParams["font.family"] = 'Malgun Gothic'
#         plt.rcParams["font.size"] = 12
#         plt.rcParams["figure.figsize"] = (12, 8)

#         plt.figure()

#         x = numpy.arange(len(label))
#         worker_value = numpy.array()
#         #해당 row의 인덱스를 찾자.

#         plt.bar(x-0.0, live_avg, width=0.2, color='blue')
#         plt.bar(x+0.2, live[n], color='red')
#         plt.xticks(x, label)

#         plt.legend()
#         plt.ylabel('인원')
#         plt.title(info3+'직장인구 현황')
#         return
#     else
#         result = '해당 지역 정보가 없습니다.'
#         return(request,보낼 곳, {'result':result})


# def pyechart(request):
#         if __name__=='__main__':


#             labels = ['20대_total', '30대_total', '40대_total', '50대_total', '60대_total']
#             titles = ['연령별 상주인구', '연령별 이동인구']
#             data   = [live[n,3:7],worker[n,3:7] # 상주와 이동 각각의

#             #### 2. matplotlib의 figure 및 axis 설정
#             rcParams.update({'font.size': 10})
#             fig, axes = plt.subplots(1,2,figsize=(10,5))
#             plt.subplots_adjust(wspace=0.5) # subplot간의 너비 간격 조절

#             #### 3. 각 subplot에 pie plot 그리기
#             explode = (0, 0.1, 0, 0, 0, 0, 0) # 퍼짐 정도 조절
#             for i in range(2):
#                 ax = axes[i] # subplot 선택
#                 wedges, texts, autotexts = ax.pie(data[i], explode=explode, labels=labels,
#                                                 autopct='%1.1f%%', pctdistance=0.85,
#                                                 shadow=False, startangle=90)
#                 for w in wedges: # 조각 설정
#                     w.set_linewidth(0)
#                     w.set_edgecolor('w')

#                 for t in texts: # label 설정
#                     t.set_color('k')
#                     t.set_fontsize(10)

#                 for a in autotexts: # 퍼센티지 설정
#                     a.set_color('w')
#                     a.set_fontsize(12)
#                 '''
#                 NOTE. 아래의 2줄은 파이차트를 도넛차트로 보이게끔 하는 trick임
#                 '''
#             #### 4. 그래프 저장하고 출력하기
#             plt.savefig('ex_pieplot.png', format='png', dpi=300)
#             plt.show()
