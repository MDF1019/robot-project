import datetime

import requests
from django.http import JsonResponse
from django.shortcuts import render

from django.views import View

all_ = []


def index(request):
    info = {}
    if request.method == "POST":
        msg = request.POST.get('word')
        res = requests.post("http://api.qingyunke.com/api.php?key=free&appid=0&msg=" + msg)
        res = res.json()
        # anwer = "{}  ({})".format(res["content"], datetime.datetime.now())
        anwer = "{}".format(res["content"])
        info['梦'] = msg
        info['答案'] = anwer
        all_.append(info)
        return render(request, 'index.html', {'dialog': all_})
    else:
        return render(request, "index.html", {"dialog": all_})
