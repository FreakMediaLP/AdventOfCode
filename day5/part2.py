from functions import *
import math


def apply_rules(line, data):
    sorted_line = []








    if check_rules(sorted_line, data):
        return sorted_line


def check_rules(line, data):
    for number in line:
        position = line.index(number)
        for before in data[number]["before"]:
            if before in line and line.index(before) > position:
                return False
        for after in data[number]["after"]:
            if after in line and line.index(after) < position:
                return False
    return True


rules, lines = [], []
for line in read_lines():
    line = line.strip()

    if len(line) == 5:
        rules.append(line.split("|"))
    elif len(line) > 5:
        lines.append(line.split(","))
print(rules)
print(f"{lines}\n")

data = {}
for rule in rules:
    data[rule[0]] = {"before": [], "after": []}
    data[rule[1]] = {"before": [], "after": []}

for entry in data.keys():
    for rule in rules:
        if entry == rule[0]:
            data[entry]["after"].append(rule[1])
        elif entry == rule[1]:
            data[entry]["before"].append(rule[0])
print(data)

invalid_lines = []
for line in lines:
    if not check_rules(line, data):
        invalid_lines.append(line)
print(f"{invalid_lines}\n")

total = 0
for line in invalid_lines:
    total += math.factorial(len(line))

total = 0
for line in invalid_lines:
    sorted_line = apply_rules(line, data)
    total += int(sorted_line[math.floor(len(sorted_line) / 2)])  # get middle number from list

print(total)  #
