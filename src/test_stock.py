import requests
import pandas as pd
import json

def get_stock_data(code, market=1):
    """
    直接从东方财富获取A股数据
    market: 1=上海, 0=深圳
    """
    secid = f"{market}.{code}"
    
    url = "https://push2his.eastmoney.com/api/qt/stock/kline/get"
    params = {
        "secid": secid,
        "fields1": "f1,f2,f3,f4,f5,f6",
        "fields2": "f51,f52,f53,f54,f55,f56,f57,f58,f59,f60,f61",
        "klt": "101",        # 101=日K
        "fqt": "1",          # 1=前复权
        "beg": "20240101",
        "end": "20251231",
        "lmt": "1000"        # 最多1000条
    }
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }
    
    r = requests.get(url, params=params, headers=headers, timeout=30)
    data = r.json()
    
    if data["data"] is None or data["data"]["klines"] is None:
        return pd.DataFrame()
    
    # 解析 klines 数据
    klines = data["data"]["klines"]
    
    rows = []
    for line in klines:
        parts = line.split(",")
        rows.append({
            "trade_date": parts[0],
            "open": float(parts[1]),
            "close": float(parts[2]),
            "high": float(parts[3]),
            "low": float(parts[4]),
            "volume": int(float(parts[5])),      # 成交量（手）
            "amount": float(parts[6]),            # 成交额
            "amplitude": float(parts[7]),         # 振幅%
            "pct_change": float(parts[8]),        # 涨跌幅%
            "change_amount": float(parts[9]),     # 涨跌额
            "turnover": float(parts[10]) if parts[10] != "-" else 0  # 换手率
        })
    
    df = pd.DataFrame(rows)
    df.insert(0, "stock_code", code)
    return df

# 获取三只股票
stocks = [
    {"name": "农业银行", "code": "601288", "market": 1},
    {"name": "国电南瑞", "code": "600406", "market": 1},
    {"name": "半导体ETF", "code": "512480", "market": 1},
]

for stock in stocks:
    print(f"获取: {stock['name']} ({stock['code']})")
    
    df = get_stock_data(stock["code"], stock["market"])
    
    if df.empty:
        print(f"无数据")
        continue
    
    filename = f"data/{stock['name']}_{stock['code']}.csv"
    df.to_csv(filename, index=False, encoding="utf-8-sig")
    print(f"{filename} ({len(df)}行)")

print("\n全部完成")