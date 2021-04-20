import os

def alter(file, old_str, new_str):
    """
    替换文件中的字符串
    :param file:文件名
    :param old_str:就字符串
    :param new_str:新字符串
    :return:

    """
    file_data = ""
    with open(file, "r", encoding="utf-8") as f:
        for line in f:
            if old_str in line:
                line = line.replace(old_str, new_str, -1)
            file_data += line
    with open(file, "w", encoding="utf-8") as f:
        f.write(file_data)


def file_name_walk(file_dir):
    for root, dirs, files in os.walk(file_dir):
        if '.git' in root or 'image' in root:
            continue
        print("root", root)  # 当前目录路径
        # print("dirs", dirs)  # 当前路径下所有子目录
        # print("files", files)  # 当前路径下所有非目录子文件
        for file in files:
            if file[-3:] == '.md':
                alter(file, '![](image', '![](images')
                print(file, end=' ')
        print('\n')


file_name_walk(".\\")
