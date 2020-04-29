from django.shortcuts import render
import json
import requests

def index(request):
    api = requests.get("https://api.covid19api.com/summary")
    data = json.loads(api.content)
    return render(request,'covid_app/index.html',{'data':data})

def search(request):
    
    
    return render(request,'covid_app/search.html',{'data':data})    