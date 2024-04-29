from pathlib import Path

def get_cats_info(path: str) -> list[dict]:
    cats_list = list()
    try:
        with open(Path(__file__).parent / path, 'r', encoding='utf-8') as file:
            for line in file:
                try:
                    id, name, age = line.strip().split(',')
                    if not id or not name or not age :
                        raise ValueError("some values are empty")
                    cats_list.append({"id": id, "name": name, "age": age}) 
                except ValueError as e:
                    print(f'{e} with cat_line: {line}')
 
    except FileNotFoundError as e:
        print(f'{e} with file path: {path}')

    return cats_list


def main():
    cats_info = get_cats_info("cats_file.txt")
    print(cats_info)


if __name__ == '__main__':
    main()