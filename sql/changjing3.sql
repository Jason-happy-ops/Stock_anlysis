SELECT a.stock_code, a.avg_volume, b.trade_date, b.volume, b.pct_change
FROM ( SELECT stock_code, AVG(volume) AS avg_volume
       FROM stock_price
       WHERE trade_date >= DATE_SUB((SELECT MAX(trade_date) FROM stock_price), INTERVAL 20 DAY)
       GROUP BY stock_code
) AS a
JOIN ( SELECT stock_code, trade_date, volume, pct_change
      FROM stock_price
      WHERE (trade_date) = (SELECT MAX(trade_date) FROM stock_price)
    GROUP BY stock_code
) AS b
ON a.stock_code = b.stock_code 
WHERE  b.volume >= a.avg_volume*1.5
    AND b.pct_change > 0
GROUP BY b.stock_code
ORDER BY b.volume / a.avg_volume DESC;
