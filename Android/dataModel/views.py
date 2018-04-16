import simplejson
from django.shortcuts import render

# Create your views here.
#coding=utf-8
from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from django import forms
from .models import User

def regist(request):
    if request.method == 'POST':
        userinfo = simplejson.load(request.raw_post_data)
        if userinfo:
            username = userinfo['username']
            password = userinfo['password']
            email = userinfo['email']

            User.objects.create(username=username,password=password)
            User.save()

            return HttpResponse('regist success!!!')



def login(request):
    if request.method == 'POST':
        userinfo = simplejson.load(request.raw_post_data)
        if userinfo:
            username = userinfo['username']
            password = userinfo['password']

            user = User.objects.filter(username__exact=username,password__exact=password)

            if user:
                return HttpResponse('登陆成功')
            else:
                return HttpResponse('用户名或密码错误,请重新登录')