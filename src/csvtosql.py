import os
import glob
from sqlite3 import OperationalError
import pandas as pd
from sqlalchemy import create_engine, false
from insert_fun import update_sql

# 数据库配置
DB_config = {'user': 'root', 'password': '', 'host': 'localhost',
             'port': 3306, 'database': 'stock'}

engine = create_engine(
    "mysql+pymysql://{user}:{password}@{host}:{port}/{database}?charset=utf8mb4".format(**DB_config))

# 检查是否成功与数据库连接
try:
    with engine.connect() as conn:
        print("successfully connected to the database")

    current_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(current_dir, '..', 'data')

    Column_map = {'open': 'open_price',
                  'close': 'close_price',
                  'high': 'high_price',
                  'low': 'low_price'}

    for csv_path in glob.glob(os.path.join(data_dir, '*.csv')):
        print(f"Processing: {os.path.basename(csv_path)}")
        df = pd.read_csv(csv_path,dtype={'stock_code':str})
        df = df.rename(columns=Column_map)
        df['trade_date'] = pd.to_datetime(df['trade_date'])
        df.to_sql(name='stock_price', con=engine, if_exists='append', index=false, method=update_sql)

except  OperationalError as e:
    print("check XAMPP connection")


