SELECT stock_code, trade_date, close_price, 
pct_change
FROM
 stock_price
WHERE (stock_code, trade_date) IN (
    SELECT stock_code, MAX(trade_date)
    FROM
 stock_price
    GROUP BY
 stock_code
)
ORDER BY pct_change DESC;


SELECT a.stock_code, a.trade_date, a.close_price, a.pct_change 
FROM stock_price a
JOIN(
    SELECT stock_code, MAX(trade_date) AS max_trade_date
    FROM stock_price
    GROUP BY stock_code
)  AS b
ON a.stock_code = b.stock_code AND a.trade_date = b.max_trade_date
ORDER BY a.pct_change DESC;