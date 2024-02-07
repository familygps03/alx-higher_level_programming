#!/usr/bin/python3
"""Module containing a script that reads stdin line by line and computes metrics.
Every 10 lines and after a keyboard interruption (CTRL + C), it prints the statistics since the beginning:
Total file size: <total size>, where <total size> is the sum of all previous sizes (see input format above).
Number of lines by status code:
Possible status codes: 200, 301, 400, 401, 403, 404, 405, and 500.
If a status code doesn’t appear, nothing is printed for that status code.
Format: <status code>: <number>. Status codes are printed in ascending order.
"""

import sys

file_size = 0
status_tally = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0, "404": 0, "405": 0, "500": 0}
line_count = 0

try:
    for line in sys.stdin:
        tokens = line.split()
        if len(tokens) >= 2:
            status_code = tokens[-2]
            if status_code in status_tally:
                status_tally[status_code] += 1
                line_count += 1
            try:
                file_size += int(tokens[-1])
            except ValueError:
                pass
        if line_count % 10 == 0:
            print("File size: {:d}".format(file_size))
            for key, value in sorted(status_tally.items()):
                if value:
                    print("{:s}: {:d}".format(key, value))
    print("File size: {:d}".format(file_size))
    for key, value in sorted(status_tally.items()):
        if value:
            print("{:s}: {:d}".format(key, value))

except KeyboardInterrupt:
    print("File size: {:d}".format(file_size))
    for key, value in sorted(status_tally.items()):
        if value:
            print("{:s}: {:d}".format(key, value))
