
import os
import datetime
import sys

def count_lines(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return len(f.readlines())

def count_code_lines(folder_path):
    total_lines = 0
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            # change .* to the type that u want/ 直接改写下面文件后缀类型来指定你想要探测的文件类型
            # the showcase already include four types with .py, .html, .css, .txt/ 已经写了四种文件类型
            if file.endswith('.py') or file.endswith('.html') or file.endswith('.css') or file.endswith('txt'):
                file_path = os.path.join(root, file)
                total_lines += count_lines(file_path)
                print(file_path)
    print("该文件夹内所含有的代码行数为：")
    return total_lines

if __name__ == '__main__':
    if len(sys.argv) > 1:
        folder_path = sys.argv[1]
        print("你选择的文件夹：")
        print(folder_path)
    else:
        # default filepath
        folder_path = r'E:\Project\Rrawl\monkey'
    print("涉及文件：")
    result = count_code_lines(folder_path)
    print(result)
    with open('result.txt', 'w', encoding='utf-8') as f:
        f.write(f"生成时间：{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}: ")
        f.write(f"该文件夹内所含有的代码行数为：{result}\n")
    print("文件已成功保存到 result.txt")
