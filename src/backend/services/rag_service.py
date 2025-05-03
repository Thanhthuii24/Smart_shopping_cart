import pandas as pd
import os

class RAGService:
    def __init__(self):
        path = os.path.join("data", "Danh_sach_gian_hang.xlsx")
        self.df = pd.read_excel(path)

    def search_item(self, query: str) -> str:
        matches = self.df[self.df["Tên sản phẩm"].str.contains(query, case=False, na=False)]
        if matches.empty:
            return "Không tìm thấy thông tin trong hệ thống RAG."
        results = []
        for _, row in matches.iterrows():
            results.append(f"Sản phẩm: {row['Tên sản phẩm']} - Vị trí: {row['Gian hàng']}")
        return "\n".join(results)
