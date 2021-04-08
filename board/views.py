from math import ceil

from django.shortcuts import render
from board import models

LIST_COUNT = 10

def index(request):
    page = request.GET["p"]

    totalcount = models.count()
    boardlist = models.findall(page, LIST_COUNT)

    # paging 정보를 계산
    pagecount = ceil(totalcount / LIST_COUNT)

    data = {
        "boardlist": boardlist,
        'pagecount': pagecount,
        'nextpage': 7,
        'prvpage': 5,
        'curpage': 2
    }

    return render(request, 'board/index.html')


def view(request):
    return render(request, 'board/view.html')