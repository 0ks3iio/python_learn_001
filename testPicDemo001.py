"""
使用百度API识别图片文字并保存
"""
import base64

from aip import AipOcr

# 获取access_token
APP_ID = "16973541"
API_KEY = "qqY04psvCa3EN75tfhcc9Rsx"
SECRET_KEY = "FyskZIlZzbIhpTgIGrfqX96CC7mbH6Bf"

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)


# 读取图片路径
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


filePath = "E:\\jpg\\GDP1-100.jpg"
image = get_file_content(filePath)

result = client.accurate(image)

print(result)
