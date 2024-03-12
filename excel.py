from openpyxl import Workbook, load_workbook

class ExcelHandler:
    def __init__(self, file_name):
        self.file_name = file_name
        self.workbook = None
        self.sheet = None

    def create_workbook(self):
        self.workbook = Workbook()

    def load_workbook(self):
        if 'xlsm' in self.file_name:
            self.workbook = load_workbook(filename=self.file_name, keep_vba=True)
        else:
            self.workbook = load_workbook(filename=self.file_name)

    def create_sheet(self, sheet_name):
        self.sheet = self.workbook.create_sheet(title=sheet_name)

    def select_sheet(self, sheet_name):
        self.sheet = self.workbook[sheet_name]

    def write_cell(self, row, column, value):
        self.sheet.cell(row=row, column=column, value=value)

    def get_cell(self, row, column):
        return self.sheet.cell(row,column).value

    def save_workbook(self):
        self.workbook.save(self.file_name)

    def close_workbook(self):
        self.workbook.close()