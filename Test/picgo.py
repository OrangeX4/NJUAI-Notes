import os
import urllib.request

img_url = "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1516371301&di=d99af0828bb301fea27c2149a7070" \
    "d44&imgtype=jpg&er=1&src=http%3A%2F%2Fupload.qianhuaweb.com%2F2017%2F0718%2F1500369506683.jpg"
file_path = './images'
file_name = "picgo"

try:
    # 获得图片后缀
    file_suffix = os.path.splitext(img_url)[1]
    # 拼接图片名（包含路径）
    filename = '{}{}{}{}'.format(file_path, os.sep, file_name, file_suffix)
    # 下载图片，并保存到文件夹中
    urllib.request.urlretrieve(img_url, filename=filename)

    os.system("picgo upload " + filename)

except IOError as e:
    print("IOError")

except Exception as e:
    print("Exception")
