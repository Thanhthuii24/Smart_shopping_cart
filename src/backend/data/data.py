import pandas as pd
import sqlite3

# Đọc file Excel
df = pd.read_excel('Danh_sach_gian_hang.xlsx.xlsx', engine='openpyxl')

# Kết nối hoặc tạo database SQLite
conn = sqlite3.connect('csdl.db')

df.to_sql('vi_tri_sp', conn, if_exists='replace', index=False)

# Đóng kết nối
conn.close()

print("Chuyển đổi thành công!")
