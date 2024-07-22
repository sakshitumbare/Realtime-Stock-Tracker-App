from django.shortcuts import render
from yahoo_fin.stock_info import *
# Create your views here.

def stockpicker(request):
    stock_picker = tickers_nifty50()
    print(stock_picker)
    return render(request,"myapp/stocktracker.html",context=stock_picker)