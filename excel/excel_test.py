#!/usr/bin/python
# -*- coding: utf-8 -*-

"""

"""
import xlrd, xlwt
from xlutils.copy import copy

EXCELFILE = u"e:/routines/submit-on-Friday/通院.xls"

def open_excel(file, sheet_index=0):
    try:
        workbook = xlrd.open_workbook(file)
        sheet = workbook.sheet_by_index(sheet_index)
        return sheet
    except Exception, e:
        print str(e)

def read_excel(sheet):
    nrows = sheet.nrows
    ncols = sheet.ncols
    header_list = sheet.row_values(0)

    print nrows
    print ncols
    for field in header_list:
        print field.encode('gbk')

def write_excel(file, sheet_index=0, row=0, col=0):
	ro_workbook = xlrd.open_workbook(file)

	wo_workbook = copy(ro_workbook)
	wo_workbook.get_sheet(sheet_index).write(row, col, u"黄士傑")
	wo_workbook.save(file)

ctype_list = [
    'empty',
    'string',
    'number',
    'date',
    'boolean',
    'error'
] # seqence critical

def print_cell_type(s, row=0, col=0):
    ctype_value = s.cell(row, col).ctype
    if ctype_value >= 0 and ctype_value <= 5:
        print "cell(%d, %d): \"%s\" data type is %s" % (row, col, 
					s.cell(row, col).value.encode('gbk'), ctype_list[ctype_value])

if __name__ == "__main__":
    write_excel(EXCELFILE)
    sheet0 = open_excel(EXCELFILE)
    read_excel(sheet0)
    print_cell_type(sheet0, 0, 0)
