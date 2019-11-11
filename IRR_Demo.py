import twstock as ts
import pandas as pd
import numpy as np
from datetime import date
from datetime import datetime
import time
import msvcrt
import function_irr
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)

stock_list = ['2881A','2881B','2882A','2882B','2891B','2887E','2838A']
df1 = pd.DataFrame(index=stock_list,columns=['名稱','成交價','成交量','IRR'])

while True:
    print('【 時間 : '+datetime.now().strftime('%H:%M:%S')+' 】')
    time.sleep(1)

    for i in stock_list: #產生變數載入個股資訊
        locals()['X'+str(i)]=pd.DataFrame(ts.realtime.get(i))
        # print('X'+str(i)+'='+ str(locals()['X'+str(i)]))
        locals()['X'+str(i)+'name'] = locals()['X'+str(i)].loc['name','info']  
        locals()['X'+str(i)+'_LP'] = locals()['X'+str(i)].loc['latest_trade_price','realtime'] #收盤價
        locals()['X'+str(i)+'_volume'] = locals()['X'+str(i)].loc['accumulate_trade_volume','realtime']
        df1.loc[str(i),'名稱'] = locals()['X'+str(i)+'name']
        df1.loc[str(i),'成交價'] = float(locals()['X'+str(i)+'_LP'])
        df1.loc[str(i),'成交量'] = locals()['X'+str(i)+'_volume']


    #富邦甲
    irr_2881A = [ (date.today(), (df1.loc['2881A','成交價'])*(-1)),
        (date(2020, 6, 30), 2.46),
        (date(2021, 6, 30), 2.46),
        (date(2022, 6, 30), 2.46),
        (date(2023, 4, 30), 2.46),
        (date(2023, 4, 30), 0.8),
        (date(2023, 4, 30), 60)]
    df1.loc['2881A','IRR'] = function_irr.xirr(irr_2881A)
    #富邦乙
    irr_2881B = [ (date.today(), (df1.loc['2881B','成交價'])*(-1)),
        (date(2020, 6, 30), 2.16),
        (date(2021, 6, 30), 2.16),
        (date(2022, 6, 30), 2.16),
        (date(2023, 6, 30), 2.16),
        (date(2024, 6, 30), 2.16),
        (date(2025, 3, 31), 2.16),
        (date(2025, 3, 31), 0.53),
        (date(2025, 3, 31), 60)]
    df1.loc['2881B','IRR'] = function_irr.xirr(irr_2881B)
    #國泰甲
    irr_2882A = [ (date.today(), (df1.loc['2882A','成交價'])*(-1)),
        (date(2020, 6, 30), 2.28),
        (date(2021, 6, 30), 2.28),
        (date(2022, 6, 30), 2.28),
        (date(2023, 12, 31), 2.28),
        (date(2023, 12, 31), 60),]
    df1.loc['2882A','IRR'] = function_irr.xirr(irr_2882A)
    #國泰乙
    irr_2882B = [ (date.today(), (df1.loc['2882B','成交價'])*(-1)),
        (date(2020, 6, 30), 2.13),
        (date(2021, 6, 30), 2.13),
        (date(2022, 6, 30), 2.13),
        (date(2023, 6, 30), 2.13),
        (date(2024, 6, 30), 2.13),
        (date(2025, 6, 30), 2.13),
        (date(2025, 6, 30), 1.05),
        (date(2025, 6, 30), 60)]
    df1.loc['2882B','IRR'] = function_irr.xirr(irr_2882B)
    #中信乙
    irr_2891B = [ (date.today(), (df1.loc['2891B','成交價'])*(-1)),
        (date(2020, 6, 30), 2.25),
        (date(2021, 6, 30), 2.25),
        (date(2022, 6, 30), 2.25),
        (date(2023, 6, 30), 2.25),
        (date(2024, 6, 30), 2.25),
        (date(2024, 12, 31), 2.25),
        (date(2024, 12, 31), 60)]
    df1.loc['2891B','IRR'] = function_irr.xirr(irr_2891B)
    #台新戊
    irr_2887E = [ (date.today(), (df1.loc['2887E','成交價'])*(-1)),
        (date(2020, 6, 30), 2.375),
        (date(2021, 6, 30), 2.375),
        (date(2022, 6, 30), 2.375),
        (date(2023, 6, 30), 2.375),
        (date(2023, 12, 31), 2.375),
        (date(2023, 12, 31), 50)]
    df1.loc['2887E','IRR'] = function_irr.xirr(irr_2887E)
    #聯邦銀甲
    irr_2838A = [ (date.today(), (df1.loc['2838A','成交價'])*(-1)),
        (date(2020, 6, 30), 2.4),
        (date(2021, 6, 30), 2.4),
        (date(2022, 6, 30), 2.4),
        (date(2023, 4, 30), 2.4),
        (date(2023, 4, 30), 0.78),
        (date(2023, 4, 30), 50)]
    df1.loc['2838A','IRR'] = function_irr.xirr(irr_2838A)
    df1['IRR'] = df1['IRR']*100
    # df1['IRR'] = df1['IRR'].astype('object')

    print(df1)
    
    
