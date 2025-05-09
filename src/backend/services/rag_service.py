import sqlite3
from utils.excel_to_sql import sync_excel_to_sql

class RAGService:
    def __init__(self):
        # Đồng bộ dữ liệu khi khởi tạo
        sync_excel_to_sql(
            excel_path="data/Danh_sach_gian_hang.xlsx",
            db_path="data/database.db",
            table_name="gian_hang"
        )
        self.db_path = "data/database.db"

    def query_item_location(self, item_name: str) -> str:
        """Truy vấn vị trí món đồ từ database"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        query = """
        SELECT * FROM gian_hang
        WHERE ten_san_pham LIKE ?
        LIMIT 1
        """
        cursor.execute(query, (f"%{item_name}%",))
        row = cursor.fetchone()

        conn.close()

        if row:
            return f"Món '{item_name}' nằm ở gian hàng số {row[1]}, khu vực {row[2]}"
        return f"Không tìm thấy vị trí của món '{item_name}'."
