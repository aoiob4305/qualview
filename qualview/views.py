from django.shortcuts import render
from datetime import datetime

from . import parse

def mainview(request):
    lists = parse.parse('20170715.txt')
    amounts = parse.getFailAmounts(lists)
    today = datetime.now().strftime('%Y-%m-%d')
    return render(request, 'qualview/main.html', {'lists': lists, 'amounts': amounts, 'today': today})

def monthlyview(request):
    return render(request, 'qualview/monthly.html', {})