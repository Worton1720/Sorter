from colorama import Fore, Style
import json
import os


# Остальной код folder_utils.py
# Функция для получения пути к файлу в директории, где находится текущий скрипт
def get_file_path(filename: str = None) -> str:
    """Возвращает путь к файлу"""
    from os.path import dirname, realpath, join

    dir_path = dirname(realpath(__file__))
    try:
        if filename == None:
            out_path = join(dir_path)
        else:
            out_path = join(dir_path, filename)
    except Exception as e:
        print(f"Ошибка: {e}")
        return 900  # Вернем 900 для обозначения ошибки
    return out_path


def get_extensions(extensions, main_path: str = None):
    """
    Получает расширения из файла или возвращает параметры по умолчанию.

    Args:
        main_path (str): Путь к папке.

    Returns:
        dict: Словарь расширений.
    """

    main_path = main_path or get_file_path()
    extensions_file_path = os.path.join(main_path, "extensions.json")
    # Загружает расширения из файла.
    try:
        with open(extensions_file_path, "r") as file:
            extensions = json.load(file)
        return extensions
    except (FileNotFoundError, json.JSONDecodeError) as e:
        # Сохраняет расширения в файл.
        with open(extensions_file_path, "w") as file:
            json.dump(extensions, file, indent=2)
        return extensions


def create_folder(path: str):
    """
    Создает папку по указанному пути, если она не существует.

    Args:
        path (str): Путь к папке.
    """
    try:
        if not os.path.exists(path):
            path = path.replace("/", "\\")
            os.mkdir(path)
    except OSError as e:
        print(f"{Fore.RED}Не удалось создать папку:{Style.RESET_ALL} {path}")
        print(f"{Fore.RED}Ошибка:{Style.RESET_ALL} {str(e)}")


def create_folders_from_list(folder_path: str, folder_names: str):
    """
    Создает папки из списка их названий в указанной папке.

    Args:
        folder_path (str): Путь к папке, в которой нужно создать папки.
        folder_names (str): Список названий папок.
    """
    for folder in folder_names:
        create_folder(os.path.join(folder_path, folder))


def get_subfolder_paths(folder_path: str):
    """
    Возвращает список путей к подпапкам в указанной папке.

    Args:
        folder_path (str): Путь к папке.

    Returns:
        list: Список путей к подпапкам.
    """
    try:
        return [f.path for f in os.scandir(folder_path) if f.is_dir()]
    except OSError as e:
        print(
            f"{Fore.RED}Не удалось получить список путей к подпапкам в папке:{Style.RESET_ALL} {folder_path}"
        )
        print(f"{Fore.RED}Ошибка:{Style.RESET_ALL} {str(e)}")
        return []


def get_file_paths(folder_path: str):
    """
    Возвращает список путей к файлам в указанной папке.

    Args:
        folder_path (str): Путь к папке.

    Returns:
        list: Список путей к файлам.
    """
    try:
        return [f.path for f in os.scandir(folder_path) if f.is_file()]
    except OSError as e:
        print(
            f"{Fore.RED}Не удалось получить список путей к файлам в папке:{Style.RESET_ALL} {folder_path}"
        )
        print(f"{Fore.RED}Ошибка:{Style.RESET_ALL} {str(e)}")
        return []


def remove_empty_folders(folder_path: str, extensions):
    """
    Удаляет пустые папки в указанной папке.

    Args:
        folder_path (str): Путь к папке.
    """
    try:
        for dirpath, dirnames, filenames in os.walk(folder_path, topdown=False):
            if not dirnames and not filenames:
                if not dirpath.endswith(tuple(extensions.keys())):
                    print(
                        f"{Fore.BLUE}Удаление пустой папки{Style.RESET_ALL}:",
                        os.path.basename(dirpath),
                        "\n",
                    )
                os.rmdir(dirpath)
    except OSError as e:
        print(
            f"{Fore.RED}Не удалось удалить пустые папки в папке:{Style.RESET_ALL} {folder_path}"
        )
        print(f"{Fore.RED}Ошибка:{Style.RESET_ALL} {str(e)}")
