import os

def dir_size(path):
    size = 0
    for name in os.listdir(path):
        full_path = os.path.join(path, name)
        if os.path.isfile(full_path):  # если файл
            size += os.path.getsize(full_path)  # добавляем размер
        elif os.path.isdir(full_path):  # если папка
            size += dir_size(full_path)  # рекурсивно суммируем размер
    return size

path = input("Введите путь к папке: ")
size = dir_size(path)
print(f"Общий размер папки '{path}': {size}")
