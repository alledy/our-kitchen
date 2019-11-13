from django.shortcuts import render
import urllib.request
import json
import requests
import pandas as pd
import numpy as np
import mathplot
from decouple import config
token = config('TOKEN')

def radius_analysis(request,lat_info,long_info):



