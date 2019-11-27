from django.shortcuts import render, redirect
from reservation.models import Kitchen_info
from .models import Start_up, move_pop, stay_pop
import urllib.request
import requests
import pandas as pd
import numpy
import matplotlib.pyplot as plt
import mpld3
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
    url = f'http://apis.data.go.kr/B553077/api/open/sdsc/storeListInRadius?radius=500&cx={lng}&cy={lat}&ServiceKey={token}&type=json&indsLclsCd=Q'
    res = requests.get(url).json()
    print(res)
    times = len(res["body"]["items"])
    print(times)
    store_id = list()
    store_code = list()
    store_lon = list()
    store_lat = list()
    #map = folium.Map(location=[lat,lng], zoom_start=14)
    map_list = list()
    for i in range(times):
        store_id.append(res["body"]["items"][i]["bizesId"])
        store_code.append(res["body"]["items"][i]["indsSclsNm"])
        store_lon.append(res["body"]["items"][i]["lon"])
        store_lat.append(res["body"]["items"][i]["lat"])

######################################################################
    #area = res["body"]["items"][0]["signguCd"]
    # area_name = res["body"]["items"][0]["signguNm"]
    # # area_name2 = area_name.split(' ')[2]
    # # start_up = Start_up.objects.all()
    # # start_up = Start_up.objects.filter(signgunm = area_name)
    # start_up = Start_up.objects.get(signgunm = area_name)
    # print(start_up)
    # if start_up:
    #    #start_info = cur.execute(f"select * from analysis_start_up where signgunm='{area_name}';")
    #     start_info = start_up
    #     print(start_up.close)
    #     #막대그래프(서울 평균과 지역 데이터 비교)
    #     label = ['위험도', '평균 폐업기간(년)', '점포 유지기간']

    #     plt.rcParams["font.family"] = 'Malgun Gothic'
    #     plt.rcParams["font.size"] = 12
    #     plt.rcParams["figure.figsize"] = (12, 8)

    #     x = numpy.arange(len(label))

    #     plt.bar(x-0.0, start_info.close, label='폐업신고율(%)', width=0.2, color='blue')
    #     plt.bar(x+0.2, start_info.remain_term, label='평균 폐업기간(년)', width=0.2, color='red')
    #     plt.bar(x+0.2, start_info.plma, label='평균 매장 증감율(년)', width=0.2, color='red')
    #     plt.xticks(x, label)
    #     plt.legend()
    #     plt.ylim(0, 5)
    #     plt.title(f'{area_name} + {Start_up.danger}')
    #     plt.savefig('analysis/ex_barhplot.png', format='png', dpi=300)
    #     fig = plt.figure()
    #     mpld3.save_html(fig,"analysis/bar.html")
    # else:
    #     result = '해당 지역 정보가 없습니다.'
    #     return redirect('analysis:kitchen_map')
    # return render(request, 'analysis/radius.html', {'lat': lat, 'lng': lng, 'store_id': store_id, 'store_code': store_code, 'store_lon': store_lon, 'store_lat': store_lat, 'start_info.close': start_info.close, 'start_info.remain_term': start_info.remain_term, 'start_info.plma': start_info.plma})
    return render(request, 'analysis/radius.html', {'lat': lat, 'lng': lng, 'store_id': store_id, 'store_code': store_code, 'store_lon': store_lon, 'store_lat': store_lat})

# def stick(request, lat, lng):
#     token = config('TOKEN')
#     url = f'http://apis.data.go.kr/B553077/api/open/sdsc/storeListInRadius?radius=500&cx={lng}&cy={lat}&ServiceKey={token}&type=json&indsLclsCd=Q'
#     res = requests.get(url).json()


# def pie(request):
#     token = config('TOKEN')
#     url = f'http://apis.data.go.kr/B553077/api/open/sdsc/storeListInRadius?radius=500&cx={lng}&cy={lat}&ServiceKey={token}&type=json&indsLclsCd=Q'
#     res = requests.get(url).json()

#     if worker.code = info3
#         #직장인구의 지역코드와 info3가 같다면

#         #서울 평균과 지역 데이터 비교
#         label = ['총직장인구수', '남성_total', '여성_total', '20대_total', '30대_total', '40대_total', '50대_total', '60대_total', '남성_20', '남성_30', '남성_40', '남성_50', '남성_60', '여성_20', '여성_30', '여성_40', '여성_50', '여성_60']
#         plt.rcParams["font.family"] = 'Malgun Gothic'
#         plt.rcParams["font.size"] = 12
#         plt.rcParams["figure.figsize"] = (12, 8)

#         plt.figure()

#         x = numpy.arange(len(label))
#         worker_value = numpy.array()
#         #해당 row의 인덱스를 찾자.

#         plt.bar(x-0.0, worker_avg, width=0.2, color='blue')
#         plt.bar(x+0.2, worker[n], color='red')
#         plt.xticks(x, label)

#         plt.legend()
#         plt.ylabel('인원')
#         plt.title(info3+'직장인구 현황')
#         return
#     else
#         result = '해당 지역 정보가 없습니다.'
#         return(request,보낼 곳, {'result':result})

#     if live.code = info3
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
