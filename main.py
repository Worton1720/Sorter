from os.path import expanduser, isabs
from colorama import init, Fore, Style
from file_organizer import sort_files

# Инициализация colorama
init()

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
}


def main():
    # Путь к папке по умолчанию
    link_path_def = expanduser("~\\Downloads")

    print(f"\n{Fore.YELLOW}------- Начало работы -------{Style.RESET_ALL}")
    """
    Основная функция программы.
    """
    print("1) Введите путь к папке.")
    print("2) Нажмите enter, чтобы оставить путь к папке Download.")
    main_path = ""

    while not main_path:
        main_path = input("Путь к папке: ").strip().replace("'", "").replace('"', "")
        if not main_path:
            main_path = link_path_def
            print(f"{Fore.GREEN}Выбрана папка Download!{Style.RESET_ALL} \n")

        else:
            if not isabs(main_path):
                print(
                    f"{Fore.RED}Введенный путь не является действительным. Попробуйте снова.{Style.RESET_ALL}"
                )
                main_path = ""

    sort_files(main_path, extensions)
    print(f"{Fore.YELLOW}------- Конец работы -------{Style.RESET_ALL}")


if __name__ == "__main__":
    while True:
        main()

        choice = input("\n Желаете продолжить? (y/n): ")
        if choice.lower() not in ["y", "н"]:
            break
