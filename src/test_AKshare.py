import akshare as ak
import pandas as pd
import time

stock_dict = [{"name":"平安银行" , "code":"000001"},
{"name":"比亚迪" , "code":"002594"},
{"name":"宁德时代" , "code":"300750"},
{"name":"贵州茅台" , "code":"600519"},]

def stock_list(stock):
    time.sleep(5)
    df = ak.stock_zh_a_hist(symbol = stock['code'] , start_date = '20240101', period = 'daily' ,
    adjust = 'qfq')
    
    filename = f"data/{stock['name']}_{stock['code']}.csv"
    df.to_csv(filename, index=False, encoding='utf-8-sig')


for stock in stock_dict:
    print(f"正在获取: {stock['name']} ({stock['code']})")
    try:
        stock_list(stock)
    except Exception as e:
        print(f"获取 {stock['name']} 失败: {e}")
        continue  
