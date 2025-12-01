from functions import *
import re


values = read()

regex = r"mul\((\d{1,3}),\s*(\d{1,3})\)"
enable = r"do\(\)"
disable = r"don't\(\)"

enabled = True
total = 0
pos = 0

while pos < len(values):
    if re.match(enable, values[pos:]):
        enabled = True
        pos += len(enable.replace("\\", ""))
    elif re.match(disable, values[pos:]):
        enabled = False
        pos += len(disable.replace("\\", ""))
    else:
        numbers = re.match(regex, values[pos:])
        if numbers:
            if enabled:
                num1 = int(numbers.group(1))
                num2 = int(numbers.group(2))
                total += num1 * num2
            pos += len(numbers.group(0))
        else:
            pos += 1

print(total)  # 72948684
