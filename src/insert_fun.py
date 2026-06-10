from sqlalchemy import text

def update_sql(table, conn, keys, data_iter):
    # 核心逻辑：联合主键对应的列有新值，变化，否则不变
    columns_str = ', '.join(keys)
    placeholders = ', '.join(['%s'] * len(keys))
    
    update_cols = [k for k in keys if k not in ['stock_code', 'trade_date']]
    duplicate_clause = ', '.join([f"{col} = VALUES({col})" for col in update_cols])
    
    sql = f"""
        INSERT INTO stock_price (
{columns_str}
)
        VALUES (
{placeholders}
)
        ON DUPLICATE KEY UPDATE 
{duplicate_clause}
    """
    
    for row in data_iter:
        try:
            conn.exec_driver_sql(sql, tuple(row))
        except Exception as e:
            print(f" SQL执行失败: {e}")
            print(f"  SQL: {sql}")
            print(f"  数据: {tuple(row)}")
            raise  
        conn.exec_driver_sql((sql), tuple(row))
    
    return 0  