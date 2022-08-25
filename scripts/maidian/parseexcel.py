class ParseExcel(object):
    def __init__(self, sheet_name):
        try:
            self.filename = DownloadFile().m_file_path
            self.sheet_name = sheet_name
            self.df = pd.read_excel(self.filename, self.sheet_name)
        except Exception as e:
            raise e

    def get_row_num(self):
        """获取行号组成的列表, 从0开始的"""
        row_num_list = self.df.index.values
        return row_num_list

    def get_cell_value(self, row, column):
        """获取某一个单元格的数据"""
        try:
            if isinstance(row, int) and isinstance(column, int):
                cell_value = self.df.iloc[row - 2, column - 1]  # iloc的行参数是按照有效数据行，且从0开始
                return cell_value
            else:
                raise TypeError('row and column must be type int')
        except Exception as e:
            raise e

    def get_table_title(self):
        """获取表头， 返回列表"""
        table_title = self.df.columns.values
        return table_title

    def get_row_value(self, row):
        """获取某一行的数据， 行号从1开始"""
        try:
            if isinstance(row, int):
                row_data = self.df.iloc[row - 2].values
                return row_data
            else:
                raise TypeError('row must be type int')
        except Exception as e:
            raise e

    def get_column_value(self, col_name):
        """获取某一列数据"""
        try:
            if isinstance(col_name, str):
                col_data = self.df[col_name].values
                return col_data
            else:
                raise TypeError('col_name must be type str')
        except Exception as e:
            raise e

    def get_all_value(self):
        """获取所有的数据，不包括表头, 返回嵌套字典的列表"""
        rows_num = self.get_row_num()
        table_title = self.get_table_title()
        values_list = []
        for i in rows_num:
            row_data = self.df.loc[i, table_title].to_dict()
            values_list.append(row_data)
        return values_list