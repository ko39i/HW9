from contextlib import contextmanager
from openpyxl import Workbook

@contextmanager
def create_workbook(filepath):
    workbook = Workbook()
    try:
        yield workbook
    finally:
        workbook.save(filepath)

with create_workbook('workbook_name.xlsx') as workbook:
    worksheet = workbook.active
    worksheet.cell(row=1, column=1, value="1")
