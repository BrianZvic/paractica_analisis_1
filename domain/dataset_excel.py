import pandas as pd
from domain.dataset import Dataset

class DatasetExcel(Dataset):
    def __init__(self, excel_file):
        super().__init__(excel_file)


    def upload_data(self):
        try:
            df = pd.read_excel(self.get_fonts)
            self.set_dataset(df)
            print("Dataset Almacenado")

        except Exception as e:
            print(e)