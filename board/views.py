from math import ceil

from django.http import HttpResponseRedirect
from django.shortcuts import render
from board import models

LIST_COUNT = 10

def index(request):
    page = request.GET.get("p")
    page = 1 if page is None else int(page)

    print(page)

    # totalcount = models.count()
    # boardlist = models.findall(page, LIST_COUNT)

    # paging 정보를 계산
    # pagecount = ceil(totalcount / LIST_COUNT)

    # data = {
    #     "boardlist": boardlist,
    #     'pagecount': pagecount,
    #     'nextpage': 7,
    #     'prvpage': 5,
    #     'curpage': 2
    # }

    return render(request, 'board/index.html')

def view(request):
    return render(request, 'board/view.html')

def write(request):
    return render(request, 'board/write.html')

def updateform(request):
    # Access Control(접근 제어)
    authuser = request.session.get("authuser")
    if authuser is None:
        return HttpResponseRedirect('/')

    no = request.session['authuser']['no']

    # 1. 데이터를 가져오기
    result = models.findbyno(no)
    data = {'board': result}

    return render(request, 'board/updateform.html', data)


def update(request):
    no = request.session['authuser']['no']
    name = request.POST['name']
    password = request.POST['password']
    gender = request.POST['gender']

    models.update(no, name, password, gender)
    request.session['authuser'] = {'no': no, 'name': name}

    return HttpResponseRedirect('/board/updateform')

def deleteform(request):
    return render(request, 'board/deleteform.html')

def delete(request):
    no = request.POST['no']
    password = request.POST['password']

    models.deleteby_no_and_password(no, password)

    return HttpResponseRedirect('/board')