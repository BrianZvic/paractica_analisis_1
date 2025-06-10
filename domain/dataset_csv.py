import pandas as pd
from domain.dataset import Dataset


class DatasetCsv(Dataset):
    def __init__(self, csv_file):
        super().__init__(csv_file)

    def upload_data(self):
        try:
            dataframe = pd.read_csv(self.get_fonts)
            self.set_dataset(dataframe)
            print("Dataset Almacenado")

        except Exception as e:
            print("Error al importar el el archivo")