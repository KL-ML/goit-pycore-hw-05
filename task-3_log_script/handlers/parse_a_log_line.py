"""Function for parsing log lines."""

def parse_log_line(log_line: str) -> dict:
    """Function for parsing log lines.

    Args:
        line (str): log line in the form of a string

    Returns:
        dict: a dictionary with parsed components: date, time, level, message.
    """
    date, time, level, *args = log_line.split(' ')
    message = ' '.join(args).removesuffix('\n')
    line_dict = {'date': date, 'time': time, 'level': level, 'message': message}

    return line_dict
