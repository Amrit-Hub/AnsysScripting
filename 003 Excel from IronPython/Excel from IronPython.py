from __future__ import print_function
import clr
# https://learn.microsoft.com/en-us/dotnet/api/microsoft.office.interop.excel?view=excel-pia
clr.AddReference("Microsoft.Office.Interop.Excel")

# import Application
import Microsoft.Office.Interop.Excel as Excel

# Create excel object
excel = Excel.ApplicationClass()

# Make the excel application visible
excel.Visible = True

# Read the workbook
workbook = excel.Workbooks.Open(r"D:\AnsysScripting\0_3 Excel from IronPython\excel.xlsx")

# Read the worksheet (Excel index starts with 1, unlike 0 in python)
worksheet = workbook.Worksheets['Sheet1']  # Name based
worksheet = workbook.Sheets[1] # Index based
print(worksheet.Name)

# Store worksheet used range
worksheetRange = worksheet.UsedRange
rowCount = worksheetRange.Rows.Count
colCount = worksheetRange.Columns.Count
# print(rowCount, colCount)

# print worksheet values
for row in range(1, rowCount+1):
    for col in range(1, colCount+1):
        print(worksheetRange.Cells[row, col].Value2, end="\t")
    print("\n")

workbook.Close()