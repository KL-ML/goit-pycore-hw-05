"""formats and outputs calculation results in a readable form."""

def display_log_counts(counts: dict):
    """ formats and outputs calculation results in a readable form.
        Args:
            counts (dict): a dictionary with the number of logs of each level
        Returns:
            display_log (str): formated calculation results
    """

    info, debag, warning, error, errr = counts

    display_log = f"""Pівень логування | Кількість
-----------------|----------
INFO             | {counts[info]}
DEBUG            | {counts[debag]}
ERROR            | {counts[warning]}
WARNING          | {counts[error]}
ERRR             | {counts[errr]}
"""

    print(display_log)
