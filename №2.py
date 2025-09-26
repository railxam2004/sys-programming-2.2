from pathlib import Path

def dir_size(path):
    total_size = 0
    base_path = Path(path)

    for item in base_path.rglob('*'):  # рекурсивно ищем
        if item.is_file():  # если это файл
            total_size += item.stat().st_size  # добавляем размер

    return total_size

path = input("Введите путь к папке: ")
size = dir_size(path)

print(f"Общий размер папки '{path}': {size}")
