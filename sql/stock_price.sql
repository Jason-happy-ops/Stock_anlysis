CREATE TABLE stock_price
(
    stock_code      VARCHAR(10),
    trade_date      DATE,
    open_price      DECIMAL(10, 2),
    close_price     DECIMAL(10, 2),      
    high_price      DECIMAL(10, 2),
    low_price       DECIMAL(10, 2),
    volume          INT(20),
    amount          DECIMAL(15, 2),       
    amplitude       DECIMAL(5, 2),
    pct_change      DECIMAL(5, 2),
    change_amount   DECIMAL(10, 2),
    turnover        DECIMAL(5, 2),

    PRIMARY KEY (stock_code, trade_date),
    FOREIGN KEY (stock_code) REFERENCES stock_info(stock_code)
        ON DELETE CASCADE ON UPDATE CASCADE
);