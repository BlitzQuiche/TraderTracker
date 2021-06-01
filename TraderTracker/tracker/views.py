from django.shortcuts import render, redirect
from django.http import HttpResponse
from .bots import binanceBot

def index(request):
    return render(request, 'index.html')

def crypto(request):
    b = binanceBot()
    BTCGBP = b.get_price("BTCGBP")
    btc_all = b.get_trades("BTCGBP")
    btc_all_buys = [x for x in btc_all if x['isBuyer']]
    btc_bal = b.get_asset_bal('BTC')
    btc_val = float(BTCGBP['price']) * float(btc_bal['free'])
    total_spent = sum([float(x['quoteQty']) for x in btc_all_buys ])
    btc_av_open = round(total_spent / float(btc_bal['free']), 2)

    context = {
        'BTCGBP': BTCGBP,
        'BTC_trades': btc_all_buys,
        'BTC_bal': btc_bal,
        'BTC_val': btc_val,
        'BTC_av_open': btc_av_open
    }
    return render(request, 'crypto.html', context)
