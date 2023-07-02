import os
from os.path import splitext, expanduser
from colorama import init, Fore, Style
from urllib.parse import urlparse

# Инициализация colorama
init()

# Путь к папке по умолчанию
link_path_def = expanduser("~\\Downloads")

# Расширения файлов для каждой категории
extensions = {
    "video": [
        "mp4",
        "mov",
        "avi",
        "mkv",
        "wmv",
        "3gp",
        "3g2",
        "mpg",
        "mpeg",
        "m4v",
        "h264",
        "flv",
        "rm",
        "swf",
        "vob",
    ],
    "code": ["py", "js", "html", "jar", "json", "java", "cpp", "css", "php"],
    "data": [
        "sql",
        "sqlite",
        "sqlite3",
        "csv",
        "dat",
        "db",
        "log",
        "mdb",
        "sav",
        "tar",
        "xml",
        "xlsx",
        "xls",
        "xlsm",
        "ods",
    ],
    "audio": [
        "mp3",
        "wav",
        "ogg",
        "flac",
        "aif",
        "mid",
        "midi",
        "mpa",
        "wma",
        "wpl",
        "cda",
        "aac",
        "m4a",
    ],
    "image": [
        "jpg",
        "png",
        "bmp",
        "ai",
        "psd",
        "ico",
        "jpeg",
        "ps",
        "svg",
        "tif",
        "tiff",
        "gif",
        "eps",
    ],
    "archive": [
        "zip",
        "rar",
        "7z",
        "z",
        "gz",
        "rpm",
        "arj",
        "pkg",
        "deb",
        "tar.gz",
        "tar.bz2",
    ],
    "text": ["pdf", "txt", "doc", "docx", "rtf", "tex", "wpd", "odt"],
    "presentation": ["pptx", "ppt", "pps", "key", "odp"],
    "font": ["otf", "ttf", "fon", "fnt"],
    "installer": ["torrent", "msi", "exe"],
    "mobile": ["apk", "obb"],
    "different": ["mcaddon", "mcpack", "ct"],
    "backup": ["bak", "bak2"],
    "other": [],
}


def create_folder(path: str):
    """
    Создает папку по указанному пути, если она не существует.

    Args:
        path (str): Путь к папке.
    """
    try:
        if not os.path.exists(path):
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


def remove_empty_folders(folder_path: str):
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


def sort_files(main_path: str):
    """
    Сортирует файлы в указанной папке по категориям.

    Args:
        main_path (str): Путь к папке.
    """
    try:
        create_folders_from_list(main_path, extensions)

        file_paths = get_file_paths(main_path)
        ext_list = list(extensions.items())
        for file_path in file_paths:
            try:
                extension = os.path.splitext(file_path)[-1].lower()[1:]
                file_name = os.path.basename(file_path)
                categorized = False
                for folder, exts in ext_list:
                    if extension in exts:
                        dest_folder = os.path.join(main_path, folder)
                        dest_file_path = os.path.join(dest_folder, file_name)
                        suffix = 1
                        while os.path.exists(dest_file_path):
                            new_file_name = f"{os.path.splitext(file_name)[0]}_{suffix}{os.path.splitext(file_name)[1]}"
                            dest_file_path = os.path.join(dest_folder, new_file_name)
                            suffix += 1
                        print(
                            f"{Fore.BLUE}Перемещение{Style.RESET_ALL}: {file_name} в {os.path.basename(dest_file_path)} в папке {folder}\n"
                        )
                        os.rename(file_path, dest_file_path)
                        categorized = True
                        break

                if not categorized:
                    dest_folder = os.path.join(main_path, "other")
                    dest_file_path = os.path.join(dest_folder, file_name)
                    suffix = 1
                    while os.path.exists(dest_file_path):
                        new_file_name = f"{os.path.splitext(file_name)[0]}_{suffix}{os.path.splitext(file_name)[1]}"
                        dest_file_path = os.path.join(dest_folder, new_file_name)
                        suffix += 1
                    print(
                        f"{Fore.BLUE}Перемещение{Style.RESET_ALL}: {file_name} в {os.path.basename(dest_file_path)} в папке other\n"
                    )
                    os.rename(file_path, dest_file_path)

            except Exception as e:
                print(
                    f"{Fore.RED}Произошла ошибка при обработке файла:{Style.RESET_ALL} {str(e)}"
                )
                continue

        remove_empty_folders(main_path)
        print(f"{Fore.GREEN}Сортировка завершена!{Style.RESET_ALL}")

    except Exception as e:
        print(
            f"{Fore.RED}Произошла ошибка при сортировке файлов:{Style.RESET_ALL} {str(e)}"
        )


def main():
    print(f"\n{Fore.YELLOW}------- Начало работы -------{Style.RESET_ALL}")
    """
    Основная функция программы.
    """
    print("1) Введите путь к папке.")
    print("2) Нажмите enter, чтобы оставить путь к папке Download.")
    main_path = ""

    while not main_path:
        main_path = input("Путь к папке: ").strip()
        if not main_path:
            main_path = link_path_def
            print(f"{Fore.GREEN}Выбрана папка Download!{Style.RESET_ALL} \n")
        else:
            parsed = urlparse(main_path)
            if not parsed.scheme or not parsed.netloc:
                print(
                    f"{Fore.RED}Введенный путь не является ссылкой. Попробуйте снова.{Style.RESET_ALL}"
                )
                main_path = ""

    sort_files(main_path)
    print(f"{Fore.YELLOW}------- Конец работы -------{Style.RESET_ALL}")


if __name__ == "__main__":
    while True:
        main()

        choice = input("\n Желаете продолжить? (y/n): ")
        if choice.lower() not in ["y", "н"]:
            break
