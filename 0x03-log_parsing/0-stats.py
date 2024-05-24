#!/usr/bin/python3
"""Write a script that reads stdin line by line and computes metrics"""
import re
import sys
import signal

counter = 0
file_size = 0
try:

    for line in sys.stdin:
        line_pattern = r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{6}\] \"GET /projects/260 HTTP/1.1\" (\d{3}) (\d+)"
        if re.search(line_pattern, line) is None:
            pass

        IP_pattern = r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"
        status_code_pattern = "(\d{3})"
        file_size_pattern = " \d+$"
        date_pattern = "\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{6}\]"

        IP = re.search(IP_pattern, line)
        file_size = re.search(file_size_pattern, line)
        status_code = re.search(status_code_pattern, line).group(1)

        counter += 1
        print(status_code)

        print(status_code)

except KeyboardInterrupt:
    pass

# 214.131.33.145 - [2024-05-18 02:59:50.755591] "GET /projects/260 HTTP/1.1" 400 105
# <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
# f"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{6}\] GET /projects/260 HTTP/1.1 (\d{3}) (\d+)"
