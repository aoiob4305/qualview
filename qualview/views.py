from django.shortcuts import render

from . import parse

def mainview(request):
    lists = parse.parse('20170715.txt')
    lines = [x['등록라인'] for x in lists[:-1]]
    amounts = [int(x['불량수량']) for x in lists[:-1]]
    return render(request, 'qualview/main.html', {'lists': lists, 'lines': lines, 'amounts': amounts})

def monthlyview(request):
    return render(request, 'qualview/monthly.html', {})