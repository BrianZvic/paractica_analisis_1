
from database.datasaver import DataSaver
from domain.dataset_excel import DatasetExcel




from domain.dataset_csv import DatasetCsv
from os import path


path_csv = path.join(path.dirname(__file__),"files/ElectricSalesHistoricalCars.csv")
path_excel = path.join(path.dirname(__file__),"files/precios_res1_2018.xlsx")

dataset_csv = DatasetCsv(path_csv)
dataset_excel = DatasetExcel(path_excel)

#--Cargar datos de archivos--
#dataset_excel.upload_data()
dataset_csv.upload_data()

#--Metodos de transformacion--

#--Cambia el tipo de dato en una columna solictada
#dataset_csv.set_datatype("Precio","float")

#-Muestra los valores NaN de un data set
#dataset_csv.see_NaNvalues()

#-Reemplaza el valor de las columnas vacias con el valor que indiques
#dataset_csv.nan_replace_with_value("Precio",3.2)


#-Reemplaza los valores NaN de una columna con valores que mas se repiten en la columna en cuenstion
#dataset_csv.nan_replace()

#-Borra las filas que contengan valores Nulos
#dataset_csv.delete_nan()

#-Muestra la cantidad de datos duplicados que tiene el dataset.
#dataset_csv.see_duplicatesvalues()

#-Elimina los valores duplicados de un dataset
#dataset_csv.drop_duplicates()

datasaver = DataSaver()

#-Guarda los datos en una Base de datos
#datasaver.save_dataframe(dataset_csv.get_dataset,"Precios")


