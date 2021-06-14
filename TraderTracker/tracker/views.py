from django.shortcuts import render, redirect
from django.http import HttpResponse
from .bots import binanceBot

def index(request):
    return render(request, 'index.html')

def crypto(request):
    """
    Crypto home page controller.
    Displays balance, holdings, market price and average open
    for each main holding in binance account - BTC, ADA
    """
    b = binanceBot()

    ## BTC ##
    # Get current price of token 
    BTCGBP = b.get_price("BTCGBP")

    # Get all of my buy trades of token 
    btc_all = b.get_trades("BTCGBP")
    btc_all_buys = [x for x in btc_all if x['isBuyer']]

    # Get volume of current token in account
    btc_bal = b.get_asset_bal('BTC')

    # Calculate average open of token 
    btc_val = float(BTCGBP['price']) * float(btc_bal['free'])
    btc_total_spent = sum([float(x['quoteQty']) for x in btc_all_buys ])
    btc_av_open = round(btc_total_spent / float(btc_bal['free']), 2)

    ## ADA ##
    ADAGBP = b.get_price("ADAGBP")
    ada_all = b.get_trades("ADAGBP")
    ada_all_buys = [x for x in ada_all if x['isBuyer']]
    ada_bal = b.get_asset_bal('ADA')
    ada_val = float(ADAGBP['price']) * float(ada_bal['free'])
    ada_total_spent = sum([float(x['quoteQty']) for x in ada_all_buys ])
    print(ada_total_spent)
    print(ada_bal)
    if float(ada_bal['free']) != 0:
        ada_av_open = round(ada_total_spent / float(ada_bal['free']), 2)
    else:
        ada_av_open = 0
    context = {
        'BTCGBP': BTCGBP,
        'BTC_trades': btc_all_buys,
        'BTC_bal': btc_bal,
        'BTC_val': round(btc_val, 2),
        'BTC_total_spend': btc_total_spent,
        'BTC_av_open': btc_av_open,

        'ADAGBP': ADAGBP,
        'ADA_trades': ada_all_buys,
        'ADA_bal': ada_bal,
        'ADA_val': round(ada_val, 2),
        'ADA_total_spend': ada_total_spent,
        'ADA_av_open': ada_av_open
    }
    return render(request, 'crypto.html', context)


