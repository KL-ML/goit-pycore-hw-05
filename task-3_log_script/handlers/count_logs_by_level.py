"""Counting entries by login level"""

def count_logs_by_level(logs: list) -> dict:
    """Loops through all records and counts the number of records for each logging level.

    Args:
        logs (list): the list of log lines

    Returns:
        counts (dict): contains the number of records for each logging level
    """
    # Отримує список логів за кожним рівнем
    info = [l for l in logs if l['level'] == 'INFO']
    debag = [l for l in logs if l['level'] == 'DEBUG']
    warning = [l for l in logs if l['level'] == 'WARNING']
    error = [l for l in logs if l['level'] == 'ERROR']
    errr = [l for l in logs if l['level'] == 'ERRR']

    # Створює словник з кількістю логів кожного рівня
    counts = {'INFO': len(info), 'DEBUG': len(debag), 'WARNING': len(warning),
            'ERROR': len(error), 'ERRR': len(errr)}

    return counts
