from manageexcel import readExcel

CASE_NUMBER = 0 #用例编号
CASE_NAME = 1   #用例名称
CASE_METHOD = 2 #请求类型
CASE_URL = 3    #请求地址
CASE_DATA = 4   #用例数据
CASE_STATUS = 5 #用例状态
CASE_KEY = 6    #验证关键字

file_path = "/Users/anderson/PycharmProjects/restfulapi/api_data.xlsx"
host = "http://localhost:5000"

row_num = readExcel(file_path).getRows

class CASE:
    number = readExcel(file_path).getName(CASE_NUMBER)
    name = readExcel(file_path).getName(CASE_NAME)
    method = readExcel(file_path).getName(CASE_METHOD)
    url = readExcel(file_path).getName(CASE_URL)
    data = readExcel(file_path).getName(CASE_DATA)
    status = readExcel(file_path).getName(CASE_STATUS)
    key = readExcel(file_path).getName(CASE_KEY)