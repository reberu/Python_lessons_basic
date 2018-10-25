import os
import sys
import shutil
# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

# Создание папок
for i in range(1, 9):
    dirname = 'dir_' + str(i)
    if not os.path.exists(dirname):
        os.mkdir(dirname)

# Удаление папок
path = os.getcwd()
dirs = os.listdir(path)
for i in dirs:
    if "dir_" in i:
        os.rmdir(i)

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
path = os.getcwd()
subfolders = [f.name for f in os.scandir(path) if f.is_dir()]
for i in subfolders:
    print(i)

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
path = os.getcwd()
dst = str(path) + r'\thisiscopy.py'
shutil.copyfile(sys.argv[0], dst)
print(dst)
