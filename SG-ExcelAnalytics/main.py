import Month_Day_Separation as mds
from DB_Connector import DBConnector as dbc
import openpyxl
import pandas as pd

# If the program is running in the main file, then:
if __name__ == "__main__":
    df = pd.DataFrame(columns=["DBName", "MaxTemp",
                      "TimeMaxTemp", "NumDetections"])
    connector = dbc(df)
    connector.load_databases()  # fills df and writes data.csv
    connector.save_csv('data.csv')
    connector.save_excel('data.xlsx')  # saves data.csv and data.xlsx
    df
