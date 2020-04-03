import xlrd
import xlwt


def read_excel():
    # 打开文件
    _data = xlrd.open_workbook('D:\\桌面\\健康告知\\重疾险.xlsx')
    table = _data.sheet_by_index(0)
    rows = table.nrows
    for i in range(1, rows):
        _par = list(table.row_values(i))
        para = _par[2].split('\n')
        for _param in para:
            # print(_param)
            data = list()
            data.append(_par[0])
            data.append(_par[1])
            data.append(_param)
            write_excel_file(data)
    # print(rows, table.row_values(2))
    # s_data = xlrd_json(table, rows)


import openpyxl as xl
import os


def write_excel_file(data, folder_path='D:\\桌面\\健康告知\\'):
    result_path = os.path.join(folder_path, "zhongji.xlsx")
    print('***** 开始写入excel文件 ' + result_path + ' ***** \n')
    if os.path.exists(result_path):
        print('***** excel已存在，在表后添加数据 ' + result_path + ' ***** \n')
        workbook = xl.load_workbook(result_path)
        sheet = workbook.active
    else:
        print('***** excel不存在，创建excel ' + result_path + ' ***** \n')
        workbook = xl.Workbook()
        workbook.save(result_path)
        sheet = workbook.active
        headers = ["公司名称", "保险名称", "健康告知"]
        sheet.append(headers)
    sheet.append(data)
    print(data)
    workbook.save(result_path)
    print('***** 生成Excel文件 ' + result_path + ' ***** \n')


if __name__ == '__main__':
    read_excel()

