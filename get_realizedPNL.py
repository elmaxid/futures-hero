check_how_many_trades = 30

import time
import config
import binance_futures
from termcolor import colored

i, overall_PNL = 0, 0
trades_list    = binance_futures.account_trades(check_how_many_trades)
position_info  = binance_futures.position_information()[0]
markPrice      = float(position_info.get('markPrice'))
positionAmt    = abs(float(position_info.get('positionAmt')))
fees_in_USDT   = round(((markPrice * positionAmt * 0.08) / 100), 2)

for trade in trades_list:
    overall_PNL = overall_PNL + float(trade.get('realizedPnl')) - fees_in_USDT
    if (float(trade.get('realizedPnl'))) > 0 :
        i = i + 1
        print(str(i) + ".  " + trade.get('realizedPnl'))
    elif (float(trade.get('realizedPnl'))) < 0 :
        i = i + 1
        print(str(i) + ". " + trade.get('realizedPnl') + " LOSER TRADE")
    else: continue

if overall_PNL > 0 : print(colored("\nOverall PNL over the last " + str(check_how_many_trades) + " trades: " + str(round(overall_PNL, 2)) + " USDT", "green"))
elif overall_PNL < 0 : print(colored("\nOverall PNL over the last " + str(check_how_many_trades) + " trades: " + str(round(overall_PNL, 2)) + " USDT", "red"))
else: print("\nOverall PNL over the last " + str(check_how_many_trades) + " trades: " + str(round(overall_PNL, 2)) + " USDT")
