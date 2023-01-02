from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("한국어 학습자 발음 평가 시스템")
