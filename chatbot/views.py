from django.shortcuts import render
from django.http import HttpResponse, JsonResponse # 결과 확인
from django.views.decorators.csrf import csrf_exempt # 보안 토큰
from .models import Kitchen_info, Consulting
from django.contrib.auth import get_user_model
import json

def home(request):
    return render(request,'chatbot/home.html')

def chat(request):
    return render(request,'chatbot/chatbot.html')

# 웹훅의 default response
@csrf_exempt
def webhook(request):
    # build a request object
    req = json.loads(request.body)
    # get action from json
    action = req.get('queryResult').get('action')
    if action:
    # return a fulfillment message
        # 시간 확인하기
    #     if req.get('queryResult').get('action')=='get_time': 
    #        time = req['queryResult']['parameters']['date-time']
    #        fulfillmentText = {'fulfillmentText':f'요청하신 시간으로 상담 신청 해 드릴까요? 요청시간 :{time}'}
    #     # 예약 확인하기
    #     if req.get('queryResult').get('action')=='get_name.Consulting-custom-yes': 
    #        name = req['queryResult']['outputContexts'][0]['parameters']['KITCHEN_name']
    #        time = req['queryResult']['outputContexts'][0]['parameters']['date-time']
    #        fulfillmentText = {'fulfillmentText':f'[{name}]으로[{time}]에 상담이 신청되었습니다.\n라인에서 Our Kitchen을 친구 추가하시면 신청 결과를 챗봇이 알려드려요! \n https://qr-official.line.me/sid/L/079xpssr.png'}

    #        # DB에 저장
    #        #user = reqest.user
    #        Consulting.objects.create(kitchen=name,datetime=time)

    #     # 희망 입점 위치 물어보기
    #     if req.get('queryResult').get('action')=='Consulting.Consulting-custom-2':
    #         location =req['queryResult']['outputContexts'][0]['parameters']['KITCHEN_location']
    #         fulfillmentText = {'fulfillmentText':location}

    # return JsonResponse(fulfillmentText, safe=False)
    
    # 시간 확인하기
        if action=='Consulting2.Consulting2-custom-2.Consulting2-custom-2-custom': 
           time = req['queryResult']['parameters']['date-time']
           fulfillmentText = {'fulfillmentText':f'요청하신 시간으로 상담 신청 할까요? 요청시간 :{time}'}

        # 예약 확인하기
        if action=='Consulting2.Consulting2-custom-2.Consulting2-custom-2-custom.Consulting2-custom-2-custom-yes': 
           name = req['queryResult']['outputContexts'][1]['parameters']['KITCHEN_name']
           time = req['queryResult']['outputContexts'][1]['parameters']['date-time']
           fulfillmentText = {'fulfillmentText':f'[{name}]으로[{time}]에 상담이 신청되었습니다.\n라인에서 Our Kitchen을 친구 추가하시면 신청 결과를 챗봇이 알려드려요! \n https://qr-official.line.me/sid/L/079xpssr.png'}
           
           Consulting.objects.create(kitchen=name,datetime=time)

        # 주방 이름 모를 때
        if action=='Consulting2.Consulting2-custom.Consulting2-custom-custom': 
           location = req['queryResult']['parameters']['KITCHEN_location']
           
           kitchen_ob = Kitchen_info.objects.filter(kitchen_name__endswith=f'{location}점')
           kitchen_list = ''
           for i in kitchen_ob:
               #kitchen_list += "("+i+")"+kitchen_ob[i].kitchen_name
               kitchen_list += '"'+i.kitchen_name+'" '

           fulfillmentText = {'fulfillmentText':f'어느 주방에 상담을 신청해 드릴까요? [{location}]에는 {kitchen_list}이 있네요!'}

        if action=='Consulting2.Consulting2-custom.Consulting2-custom-custom.Consulting2-custom-custom-custom.Consulting2-custom-custom-custom-custom':
            name = req['queryResult']['outputContexts'][1]['parameters']['KITCHEN_name']
            time = req['queryResult']['outputContexts'][1]['parameters']['date-time']
            fulfillmentText = {'fulfillmentText':f'[{name}]으로[{time}]에 상담이 신청되었습니다.\n라인에서 Our Kitchen을 친구 추가하시면 신청 결과를 챗봇이 알려드려요! \n https://qr-official.line.me/sid/L/079xpssr.png'}

    return JsonResponse(fulfillmentText, safe=False)