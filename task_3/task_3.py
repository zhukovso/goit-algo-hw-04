import sys
from pathlib import Path
import colorama


def print_element(colour, text, level):
    print(colorama.Style.RESET_ALL + f"{'┃ ' * level}┣ " + colour + f"{text}")


def parse_folder(path, i=0):
    try:
        for element in path.iterdir():
            if element.is_dir():
                print_element(colorama.Fore.YELLOW, element.name, i)
                i += 1
                parse_folder(element, i)
            if element.is_file():
                print_element(colorama.Fore.GREEN, element.name, i)
    except FileNotFoundError as e:
        print(f'{e} with file path')
    finally:
        print(colorama.Style.RESET_ALL, end="")


def main():
    if len(sys.argv) > 1:
        parent_folder_path = Path(sys.argv[1])
        print(f"{parent_folder_path}")
        parse_folder(parent_folder_path)


if __name__ == '__main__':
    main()
