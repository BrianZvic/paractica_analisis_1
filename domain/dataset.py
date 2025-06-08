from abc import ABC,abstractmethod
import pandas as pd

class Dataset(ABC):
    def __init__(self,font):
        self.__dataset = None
        self.__font = font
        self.__raw_data = None
        
    
    @property
    def get_raw_data(self):
        return self.__raw_data
    
    @property
    def get_dataset(self):
        return self.__dataset

    
    def set_dataset(self,value):
        self.__dataset = value

    @property
    def get_fonts(self):
        return self.__font


    def set_raw_data(self,value):
        self.__raw_data = value

    @abstractmethod
    def upload_data(self):
        pass
    
    @property
    def get_description(self):
        if self.validate_data():
            return print(self.__dataset.describe())
        else:
            return print("Dataset is not present")

    @property
    def get_info(self):
        if self.validate_data():
            return print(self.__dataset.info())
        else:
            return print("Dataset is not present")


    def validate_data(self):
        if isinstance(self.get_dataset,pd.DataFrame):
            return True
        else:
            return False

    def drop_duplicates(self):
        if self.validate_data():
            self.get_dataset = self.get_dataset.drop_duplicates()
            print("Dataset has been eliminated duplicated")
        else:
            print("Dataset has been NOT eliminated duplicated")

    def delete_nan(self):
       try:
           if self.validate_data():
               self.get_dataset.dropna(inplace=True)
               return print("Dataset has been eliminated NaN data")
           else:
               print("Dataset has been NOT eliminated NaN data")
       except Exception as e:
           print("it occurred an error")

    def nan_replace(self):
        try:
            if self.validate_data():
                df_copy = self.__dataset.copy()
                list_colums = df_copy.columns.tolist()
                col_index = 0
                row_index = 0
                for col in df_copy:
                    for row in df_copy[col]:
                        if type(row) is float:
                            df_copy.iloc[row_index, col_index] = df_copy[list_colums[col_index]].mode().iloc[0]
                        row_index = + 1
                    col_index = + 1
                self.get_dataset = df_copy
                print("Dataset has been replaced the NAN data")
            else:
                print("Dataset has been NOT replaced the NAN data")
        except Exception as e:
            print("It was not possible to replace the NAN data, it occurred an error")

    def nan_replace_with_value(self, column_name, value):
        try:
            if self.validate_data():
                self.get_dataset[column_name] = self.get_dataset[column_name].fillna(value)
                return print("Dataset has been replaced the NAN data")
            else:
                print("Dataset has been NOT replaced the NAN data")
        except Exception as e:
            print("It was not possible to replace the NAN data, it occurred an error")


    def convert_to_lowercase(self):
        if self.validate_data():
            self.get_dataset = self.get_dataset.str.lower()
            self.get_dataset = self.get_dataset.applymap(lambda x: x.lower() if isinstance(x, str) else x)

    def see_NaNvalues(self):
        if self.validate_data():
            print(self.get_dataset.isnull().sum())
        else:
            print("Dataset is not present")

    def see_duplicatesvalues(self):
        if self.validate_data():
            print(self.get_dataset.duplicated().sum())
        else:
            print("Dataset is not present")

    def set_datatype(self,column_name,type_name):
        try:
            if self.validate_data():
                self.get_dataset[column_name] = self.get_dataset[column_name].astype(type_name)
                print("Dataset has been set datatype")
            else:
                print("Dataset is not present")
        except Exception as e:
            print("It was not possible to set the datatype of the dataset")


