SELECT trade_date,close_price,pct_change FROM `stock_price` WHERE stock_code = '300750'
ORDER BY trade_date  DESC
LIMIT 10