"""Script for analysing a log files
    """

from pathlib import Path
import sys
from handlers import display_log_counts, load_logs, count_logs_by_level, filter_logs_by_level

def main():
    """The main function of the script
    Exeption (IndexError): Error when there are no arguments in the command line
    """
    try:
        file_path = Path(sys.argv[1])
        logs = load_logs(file_path)

        if logs:
            counts = count_logs_by_level(logs)
            display_log_counts(counts)

        if len(sys.argv) >= 3:
            level = sys.argv[2].upper()
            filter_logs_by_level(logs, level)

    except IndexError:
        print('\nНапишіть адресу лог-файлу в якості аргументу в командному рядку\n')

if __name__ == '__main__':
    main()
