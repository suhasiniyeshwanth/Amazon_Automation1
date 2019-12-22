import pandas as pd
from source.utilities import globals


def get_sheet(sheet):
    data = pd.read_excel(globals.EXCEL_PATH, sheet_name=sheet)
    return data


def get_value(sheet, row_name, col_name):
    data = pd.read_excel(globals.EXCEL_PATH, sheet_name=sheet, index_col="TestCaseID")
    value = data.loc[row_name, col_name]
    return value


def get_total_number_rows(sheet):
    data = get_sheet(globals.EXCEL_PATH, sheet)
    total_row = data.shape[0]
    return total_row


def write_to_excel(sheet, row_number, column_name, value_to_write):
    data = get_sheet(globals.EXCEL_PATH, sheet)
    data.loc[row_number, column_name] = value_to_write
    write = pd.ExcelWriter(globals.EXCEL_PATH)
    data.to_excel(write, sheet_name=sheet)
    write.save()