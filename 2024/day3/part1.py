from functions import *
import re


values = read()

regex = r"mul\((\d{1,3}),\s*(\d{1,3})\)"
numbers = re.findall(regex, values)

total = 0
for number in numbers:
    total += int(number[0]) * int(number[1])

print(total)  # 166905464
