from django.shortcuts import render
from django.http import HttpResponse, JsonResponse # 결과 확인
from django.views.decorators.csrf import csrf_exempt # 보안 토큰
#from library.df_response_lib import * # import df_library
import json

def home(request):
    return HttpResponse('Hello world')

def chat(request):
    return render(request,'chatbot/chatbot.html')

# 웹훅의 default response
@csrf_exempt
def webhook(request):
    # build a request object
    req = json.loads(request.body)
    # get action from json
    action = req.get('queryResult').get('action')
    # return a fulfillment message
    if action == 'get_consulting':
        #if req.get('queryResult').get('parameters').get('KITCHEN_name') :
        fulfillmentText = {'fulfillmentText': "키친명이있네요"}

   # if action == 'get_kitchen':
    #    fulfillmentText = {'fulfillmentText': req.get('queryResult').get('parameters').get('KITCHEN_name')}
    # return response
    return JsonResponse(fulfillmentText, safe=False)

# @csrf_exempt
# def webhook(request):
# # build request object
#     req = json.loads(request.body)
#     #get action from json
#     action = req.get('queryResult').get('action')   
#     # prepare response for suggestion chips
#     if action == 'get_suggestion_chips':
#         # set fulfillment text
#         fulfillmentText = 'Suggestion chips Response from webhook'
#         aog = actions_on_google_response()
#         aog_sr = aog.simple_response([
#             [fulfillmentText, fulfillmentText, False]
#         ])
#         #create suggestion chips
#         aog_sc = aog.suggestion_chips(["suggestion1", "suggestion2"])
#         ff_response = fulfillment_response()
#         ff_text = ff_response.fulfillment_text(fulfillmentText)
#         ff_messages = ff_response.fulfillment_messages([aog_sr, aog_sc])
#         reply = ff_response.main_response(ff_text, ff_messages)
#     # return generated response
#     return JsonResponse(reply, safe=False)