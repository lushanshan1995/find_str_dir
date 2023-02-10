# 查询目录下所有文件
import os
import sys


def find_str(path, text):
    for file_name in os.listdir(path):
        child = os.path.join('%s/%s' % (path, file_name))
        if os.path.isfile(child):
            # 文件 打开读取
            f = open(child, "r", encoding='ISO-8859-1')
            # 在文件中找到要查到的字符串后进行打印
            if text in f.read():
                print(text + " found in " + child)
        else:
            # 文件夹
            find_str(child, text)


find_str(sys.argv[1], sys.argv[2])

