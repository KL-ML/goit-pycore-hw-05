"""opens the file, reads each line and applies the parse_log_line function to it"""

import re
from handlers import parse_log_line

def load_logs(file_path: str) -> list:
    """opens the file, reads each line and applies the parse_log_line function to it

    Args:
        file_path (str): the path string to the log file

    Returns:
        list: list of logs

    Rises:
        IsADirectoryError: If the path points to a directory instead of a file
        FileNotFoundError: If the file path is incorrect or corrupted
    """

    lines = []
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            while True:
                line = file.readline()
                if not line:
                    break

                pattern = r"\d{4}\-\d{2}\-\w{2}\s\d{2}\:\d{2}\:\d{2}\s\w+\s\w+"
                # 2024-01-22 08:30:01 INFO User logged in successfully.
                match = re.search(pattern, line, re.IGNORECASE)
                if match:
                    lines.append(parse_log_line(line))

            return lines

    except IsADirectoryError: # Якщо шлях вказує на директрію а не файл
        print("Не вдалося знайти файл.\n")
        return None

    except FileNotFoundError: # Якщо шлях до файлу невірний або пошкоджений
        print("Не вдалося знайти файл.\n")
        return None
