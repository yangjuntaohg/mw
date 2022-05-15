
import xlrd

def getcollist(path):

    #打开
    workbook = xlrd.open_workbook(filename=str(path))
    #获取sheet
    table = workbook.sheets()[0]
    # table_row = table.row_values(rowx=0, start_colx=0, end_colx=None)
    # print(table_row)
    #获取表格列生成list
    table_col = table.col_values(colx=0, start_rowx=0, end_rowx=None)
    return table_col

if __name__ == '__main__':
    path='/Users/edy/Desktop/xls.xls'
    print(getcollist(path))