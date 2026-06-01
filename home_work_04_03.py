import sys
from pathlib import Path
from colorama import Fore, Style, init

# Инициализация colorama
init(autoreset=True)


def print_directory_structure(path, indent=""):

    for item in path.iterdir():

        if item.is_dir():

            print(f"{indent}{Fore.BLUE}📁 {item.name}")

            print_directory_structure(item, indent + "    ")

        else:

            print(f"{indent}{Fore.GREEN}📄 {item.name}")


def main():

    if len(sys.argv) < 2:
        print(Fore.RED + "Не указан путь к директории")
        return

    path = Path(sys.argv[1])

    if not path.exists():
        print(Fore.RED + "Путь не существует")
        return

    if not path.is_dir():
        print(Fore.RED + "Это не дериктория")
        return

    print(f"{Fore.YELLOW}Структура дериктории: {path}\n")

    print_directory_structure(path)

if __name__ == "__main__":
    main()