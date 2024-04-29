from pathlib import Path

def total_salary(path: str) -> tuple:
    
    total = 0
    count = 0
    try:
        with open(Path(__file__).parent / path, 'r', encoding='utf-8') as file:
            for line in file:
                try:
                    total += float(line.strip().split(',')[1])
                    count += 1
                except ValueError as e:
                    print(f'{e} with salary')
 
    except FileNotFoundError as e:
        print(f'{e} with file path: {path}')

    return round(total, 2), round(total/count, 2) if count else 0


def main():
    total, average = total_salary("salary_file.txt")
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")


if __name__ == '__main__':
    main()
