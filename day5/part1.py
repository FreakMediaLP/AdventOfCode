from functions import *
import math


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

print(f"{data}\n")

total = 0
for line in lines:
    if check_rules(line, data):
        total += int(line[math.floor(len(line) / 2)])  # get middle number from list

print(total)  # 4578
