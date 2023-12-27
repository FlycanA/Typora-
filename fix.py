import os
import shutil
import re

# 设置源目录和目标目录
src_dir = r'C:\Users\Lenovo\Documents\笔记\vuln4'
dst_dir = os.path.join(src_dir, "img")

# 检查目标文件夹是否存在，如果不存在则创建
if not os.path.exists(dst_dir):
    os.makedirs(dst_dir)

# 遍历源目录下的所有文件
for root, dirs, files in os.walk(src_dir):
    for file in files:
        if file.endswith('.md'):
            # 打开文件并读取内容
            file_path = os.path.join(root, file)
            print(file_path)
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # 查找并移动图片文件
            pattern = re.compile(r'C:\\Users\\Lenovo\\AppData\\Roaming\\Typora\\typora-user-images\\(.+?\.(?:png|jpg|jpeg|gif))')
            matches = pattern.findall(content)
            for match in matches:
                image_path = os.path.join('C:\\Users\\Lenovo\\AppData\\Roaming\\Typora\\typora-user-images\\', match)
                dst_path = os.path.join(dst_dir, match)
                shutil.move(image_path, dst_path)
                content = content.replace(image_path, dst_path)

            # 保存文件并输出日志
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f'Moved {len(matches)} images in {file_path}')
