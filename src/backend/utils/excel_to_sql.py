import pandas as pd
import sqlite3  

def sync_excel_to_sql(excel_path: str, db_path: str, table_name: str):
    # Đọc file Excel
    df = pd.read_excel(excel_path, engine='openpyxl')

    conn = sqlite3.connect(db_path)

    df.to_sql(table_name, conn, if_exists='replace', index=False)

    conn.close()
    print(f"Đồng bộ xong bảng `{table_name}` từ Excel vào DB `{db_path}`")
