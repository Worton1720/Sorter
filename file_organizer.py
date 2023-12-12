import os
from colorama import init, Fore, Style
from folder_utils import (
    create_folders_from_list,
    get_file_paths,
    remove_empty_folders,
    get_extensions
)

# Инициализация colorama
init()



# Остальной код extensions
def sort_files(main_path: str, extensions):
    """
    Сортирует файлы в указанной папке по категориям.

    Args:
        main_path (str): Путь к папке.
    """
    try:
        extensions = get_extensions(extensions)
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
                        new_file_name = f"{os.path.splitext(file_name)[0]}({suffix})"
                        dest_file_path = os.path.join(dest_folder, f"{new_file_name}{os.path.splitext(file_name)[1]}")
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

        remove_empty_folders(main_path, extensions)
        print(f"{Fore.GREEN}Сортировка завершена!{Style.RESET_ALL}")

    except Exception as e:
        print(
            f"{Fore.RED}Произошла ошибка при сортировке файлов:{Style.RESET_ALL} {str(e)}"
        )
