from sqlalchemy import create_engine
import pandas as pd
from sqlalchemy.exc import SQLAlchemyError
from decouple import config


class DataSaver:
    def __init__(self):
       user = config('DB_USER')
       password = config('DB_PASSWORD')
       host = config('DB_HOST')
       port = config('DB_PORT')
       database = config('DB_DATABASE')

       url = f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}"
       self.engine = create_engine(url)

    def save_dataframe(self, df, table_name):
        if df is None:
            print("NOT dataframe")

        if not isinstance(df,pd.DataFrame):
            print(f"Is not an instance of a {type(df)}")

        try:
            df.to_sql(table_name, con=self.engine, if_exists='replace', index=False)
            print(f"Data saved on table: {table_name}")

        except SQLAlchemyError as e:
            print("Error, dont save data")
