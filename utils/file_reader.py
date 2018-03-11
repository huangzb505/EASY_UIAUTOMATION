import yaml
import os
from xlrd import open_workbook


class YamlReader:
    def __init__(self, ymlf):
        if os.path.exists(ymlf):
            self.ymlf = ymlf
        else:
            raise FileNotFoundError("文件不存在")
        self._data = None

    @property
    def data(self):
        if not self._data:  # 如果是第一次调用data，读取yaml文档，否则返回之前保存的数据
            with open(self.ymlf, 'rb') as f:
                self._data = list(yaml.safe_load_all(f))
        return self._data


class SheetTypeError(Exception):
    pass


class ExcelReader:
    """
    读取excel文件中的内容。返回list。
    如：
    excel中内容为：
    | A  | B  | C  |
    | A1 | B1 | C1 |
    | A2 | B2 | C2 |
    如果 print(ExcelReader(excel, title_line=True).data)，输出结果：
    [{A: A1, B: B1, C:C1}, {A:A2, B:B2, C:C2}]
    如果 print(ExcelReader(excel, title_line=False).data)，输出结果：
    [[A,B,C], [A1,B1,C1], [A2,B2,C2]]
    可以指定sheet，通过index或者name：
    ExcelReader(excel, sheet=2)
    ExcelReader(excel, sheet='BaiDuTest')
    """
    def __init__(self, excel, sheet=0, title_line=True):
        if os.path.exists(excel):
            self.excel = excel
        else:
            raise FileNotFoundError('文件不存在')
        self._data = list()
        self.sheet = sheet
        self.title_line = title_line

    @property
    def data(self):
        if not self._data:  # 如果是第一次调用data，读取yaml文档，否则直接返回之前保存的数据
            book = open_workbook(self.excel)
            if type(self.sheet) not in [int, str]:
                raise SheetTypeError('please pass in <type int> or <type str>, not{0}'.format(type(self.sheet)))
            elif type(self.sheet) == int:
                s = book.sheet_by_index(self.sheet)
            else:
                s = book.sheet_by_name(self.sheet)

            if self.title_line:
                title = s.row_values(0)
                for col in range(1, s.nrows):
                    self._data.append(dict(zip(title, s.row_values(col))))   # 按行并行迭代以字典形式返回列数据
            else:
                for col in range(0, s.nrows):
                    self._data.append(s.row_values(col))
        return self._data


if __name__ == '__main__':
    y = 'E:\Test_Framework\config\config.yml'
    reader = YamlReader(y)
    print(reader.data)

    e = r'E:\Test_Framework\data\test_data.xlsx'
    excel = ExcelReader(e)
    print(excel.data)
