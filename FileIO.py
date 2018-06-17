# coding:utf8
# !/bin/python
# 对文件的IO封装工具
import os

import xlrd, xlwt
from xlutils.copy import copy


class OpenExcel(object):
    # 打开Excel进行读写操作
    def __init__(self, path, sname=None, row=0, col=0, heads=[]):
        self.path = path
        self.sname = sname
        self.row = row
        self.col = col
        self.heads = heads

        self.rexcel = self.openExcel()
        self.wexcel = copy(self.rexcel)
        self.sheet = self.initRSheet()
        self.sheets = self.getSheetNames()

    def openExcel(self):
        # 打开EXCEL文件，没有则创建
        if not os.path.exists(self.path):
            excel = xlwt.Workbook(encoding='utf-8')
            sheet = excel.add_sheet('sheet1', cell_overwrite_ok=True)
            for i, value in enumerate(self.heads):
                sheet.write(0, i, value)
            excel.save(self.path)
        rexcel = xlrd.open_workbook(self.path)
        return rexcel

    def getSheetNames(self):
        # 获取目标EXCEL文件所有sheet名
        sheets = self.rexcel.sheet_names()
        return sheets

    def initRSheet(self):
        # 初始化sheet对象
        sname = self.sname
        if not sname:
            sname = 0
        sheet = RWSheet(self.rexcel, self.wexcel, sname, self.row, self.col)
        return sheet

    def getSheet(self, sname=None, row=0, col=0):
        # 获取sheet对象
        sheet = self.sheet
        if sname:
            sheet = RWSheet(self.rexcel, self.wexcel, sname, row, col)
        return sheet

    def save(self, path=None):
        # 保存写入的数据
        if not path:
            path = self.path
        self.wexcel.save(path)


class RWSheet(object):
    # 生成sheet对象对表进行读写操作
    (
        XL_CELL_EMPTY,
        XL_CELL_TEXT,
        XL_CELL_NUMBER,
        XL_CELL_DATE,
        XL_CELL_BOOLEAN,
        XL_CELL_ERROR,
        XL_CELL_BLANK,
    ) = range(7)
    ctype_text = {
        XL_CELL_EMPTY: 'empty',
        XL_CELL_TEXT: 'text',
        XL_CELL_NUMBER: 'number',
        XL_CELL_DATE: 'xldate',
        XL_CELL_BOOLEAN: 'bool',
        XL_CELL_ERROR: 'error',
        XL_CELL_BLANK: 'blank',
    }

    def __init__(self, rexcel, wexcel, sname, row=0, col=0):
        self.rexcel = rexcel
        self.wexcel = wexcel
        self.sname = sname
        self.row = row
        self.col = col

        if isinstance(sname, str):
            rsheet = self.rexcel.sheet_by_name(sname)
        elif isinstance(sname, int):
            rsheet = self.rexcel.sheet_by_index(sname)
        else:
            rsheet = self.rexcel.sheet_by_index(0)
            print "Please enter the correct sheet name"
        self.rsheet = rsheet
        if not sname:
            sname = 0
        self.wsheet = self.wexcel.get_sheet(sname)
        self.sheetname, self.nrows, self.ncols = self.getSheetInfo()

    def getSheetInfo(self):
        # 获取sheet的名称，行数，列数
        sheet = self.rsheet
        sheetname = sheet.name
        nrows = sheet.nrows
        ncols = sheet.ncols
        return sheetname, nrows, ncols

    def getRowValue(self, row=None):
        # 获取整行的值
        sheet = self.rsheet
        if not row:
            row = self.row
        if row > self.nrows:
            row = self.nrows - 1
        rows = sheet.row_values(row)
        return rows

    def getColValue(self, col=None):
        # 获取整列的值
        sheet = self.rsheet
        if not col:
            col = self.col
        if col > self.ncols:
            col = self.ncols - 1
        cols = sheet.col_values(col)
        return cols

    def getCellValue(self, row=None, col=None):
        # 获取单元格内容
        sheet = self.rsheet
        if not row and not col:
            row = self.row
            col = self.col
        if row >= self.nrows:
            row = self.nrows - 1
        if col >= self.ncols:
            col = self.ncols - 1
        # value = sheet.cell_value(row, col)
        ctype = RWSheet.ctype_text[sheet.cell(row, col).ctype]
        value = sheet.cell(row, col).value
        return ctype, value

    def getAllData(self):
        # 获取所有的数据
        datas = []
        for r in range(self.nrows):
            datas.append(self.getRowValue(r))
        return datas

    def getRangeData(self, rows=0, rowe=None, cols=0, cole=None):
        # 获取rows行到rowe行，cols列到cole列之间的数据
        if rowe is None:
            rowe = self.nrows
        if cole is None:
            cole = self.ncols
        datas = []
        for r in range(rows, rowe):
            rdata = []
            for c in range(cols, cole):
                rdata.append(self.getCellValue(r, c)[1])
            datas.append(rdata)
        return datas

    def writeRowValue(self, values=[], row=None):
        # 写入整行的值
        sheet = self.wsheet
        if not row:
            row = self.nrows
        for i, v in enumerate(values):
            sheet.write(row, i, v)
        return True

    def writeColValue(self, values=[], col=None):
        # 写入整列的值
        sheet = self.wsheet
        if not col:
            col = self.ncols
        for i, v in enumerate(values):
            sheet.write(i, col, v)
        return True

    def writeCellValue(self, value="", row=None, col=None):
        # 写入单元格的值
        sheet = self.wsheet
        if not row:
            row = self.nrows
        if not col:
            col = 0
        sheet.write(row, col, value)
        return True

    def writeAllData(self, datas=[[]], row=None, col=None):
        # 写入所有的值
        sheet = self.wsheet
        if not row:
            row = self.nrows
        if not col:
            col = 0
        for i, values in enumerate(datas):
            for j, value in enumerate(values):
                sheet.write(row + i, col + j, value)
        return True


class WriteSQL(object):
    def __init__(self, path, table=None, field=[], datas=[[]]):
        self.path = path
        self.table = table
        self.field = field
        self.datas = datas
        self.initwrite = self.runWrite()

    def runWrite(self):
        for d in self.datas:
            if d:
                sql = self.insertSql(self.table, self.field, d)
                self.writeSql(sql + '\n')

    def writeSql(self, sql):
        with open(self.path, "a") as f:
            f.write(sql)

    def insertSql(self, table, field=[], data=[]):
        if field:
            fieldstr = ("%s," * len(field))[0:-1]
            # fieldstr = ",".join(field)
            if fieldstr:
                fieldstr = ("(" + fieldstr + ")") % tuple(field)
        if data:
            datastr = ("%s," * len(data))[0:-1]
            if datastr:
                datastr = ("(" + datastr + ")") % tuple(data)
        sql = "INSERT INTO %s " % table + fieldstr + " VALUES " + datastr
        return sql


if __name__ == '__main__':
    path = "property.xlsx"
    # e = OpenExcel(path)
    # print e.getSheetNames()
    # sheet1 = e.sheet
    # print sheet1.getSheetInfo()
    # print sheet1.getRowValue()
    # print sheet1.getColValue()
    # print sheet1.getCellValue()
    # print sheet1.getAllData()
    # print sheet1.getRangeData(5, 10, 3, 6)
    # print sheet1.nrows, sheet1.ncols

    # e = OpenExcel("cs.xls")
    # print e.sheet.writeRowValue([1, 2, 3, 4, 5])
    # print e.sheet.writeColValue(values=[1, 2, 3, 4, 5])
    # print e.sheet.writeCellValue(value=6)
    # print e.sheet.writeAllData(datas=[[7, 8, 9], [4, 5, 6], [1, 2, 3]])
    # e.save()
