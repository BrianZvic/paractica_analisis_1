from datetime import date

from database.datasaver import DataSaver
from domain.dataset_excel import DatasetExcel

import pandas as pd


from domain.dataset_csv import dataset_csv
from os import path

path_csv = path.join(path.dirname(__file__),"files/ElectricSalesHistoricalCars.csv")
path_excel = path.join(path.dirname(__file__),"files/precios_res1_2018.xlsx")

dsaver = DataSaver()

datasetcsv = dataset_csv(path_csv)
datasetcsv.upload_data()

#datasetexcel = DatasetExcel(path_excel)
#datasetexcel.upload_data()


#dsaver.save_dataframe(datasetcsv.get_dataset,"csv")

#print(datasetcsv.convert_to_lowercase())
#print(datasetcsv.get_dataset)

#dsaver.save_dataframe(datasetexcel.get_dataset,"excel")

#print(datasetcsv.get_dataset.info())
#datasetcsv.delete_nan()
datasetcsv.see_NaNvalues()
#datasetcsv.set_datatype("region","string")

#print(datasetcsv.get_dataset.info())
#print(datasetcsv.get_dataset["region"].mode())

datasetcsv.nan_replace_with_value("region",datasetcsv.get_dataset["region"].mode().iloc[0])
datasetcsv.see_NaNvalues()



