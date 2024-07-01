"""gets and outputs all log entries for a given logging level
    """

def filter_logs_by_level(logs: list, level: str):
    """gets and outputs all log entries for a given logging level

    Args:
        logs (list): a list of log entries for a specific logging level
        level (str): the name of the logging level
    """

    if level in ('INFO', 'DEBUG', 'ERROR', 'WARNING', 'ERRR'):

        filtered_by_level = [l for l in logs if l['level'] == level]
        print(f"Деталі логів для рівня '{level}':")

        for log in filtered_by_level:
            log_sting = f"{log['date']} {log['time']} - {log['message']}"
            print(log_sting)

    else:
        print("Напишіть корректну назву рівня логування для відображення деталей логів.\n")
