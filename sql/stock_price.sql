Create TABLE stock_price
(	stock_code VARCHAR(10),
 	trade_date date,
 	open_price DECIMAL(3,2),
 	cloese_price DECIMAL(3,2),
 	high_price DECIMAL(3,2),
 	low_price DECIMAL(3,2),
 	volume INT(20),
	amount BIGINT,
 	amplitude DECIMAL(3,2),
 	pct_change DECIMAL(3,2),
 	change_amount DECIMAL(3,2),
 	
 	PRIMARY KEY (stock_code,trade_date),
	FOREIGN KEY (stock_code) REFERENCES stock_info(stock_code)
 	ON DELETE CASCADE ON UPDATE CASCADE
);