#!/usr/bin/python3
"""Reads input from standard input and calculates metrics.

After every ten lines or a keyboard interruption (CTRL + C),
prints the following statistics:
    - Total file size up to that point.
    - Count of encountered status codes up to that point.
"""


def print_statistics(file_size, status_code_count):
    """Prints accumulated metrics.

    Args:
        file_size (int): The total accumulated file size.
        status_code_count (dict): The accumulated count of status codes.
    """
    print("Total file size: {}".format(file_size))
    for code in sorted(status_code_count):
        print("{}: {}".format(code, status_code_count[code]))


if __name__ == "__main__":
    import sys

    total_size = 0
    status_codes = {}
    valid_status_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    line_count = 0

    try:
        for line in sys.stdin:
            if line_count == 10:
                print_statistics(total_size, status_codes)
                line_count = 1
            else:
                line_count += 1

            tokens = line.split()
            try:
                total_size += int(tokens[-1])
            except (IndexError, ValueError):
                pass

            try:
                code = tokens[-2]
                if code in valid_status_codes:
                    status_codes[code] = status_codes.get(code, 0) + 1
            except IndexError:
                pass

        print_statistics(total_size, status_codes)

    except KeyboardInterrupt:
        print_statistics(total_size, status_codes)
        raise
