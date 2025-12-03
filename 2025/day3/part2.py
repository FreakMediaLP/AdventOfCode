from functions import *

lines = read_lines()
banks = []
rage_length = 12

for line in lines:
    banks.append(list(line.strip()))

count = 0
for bank in banks:
    battery_order = ""
    big_num = {"num": 0, "pos": 0}

    for battery in range(rage_length):
        pos = big_num["pos"]

        limit = -rage_length + battery + 1
        if limit == 0:  # thanks for that Python _-_
            limit = None

        bank_slice = bank[big_num["pos"]:limit]
        for number in bank_slice:
            if int(number) > big_num["num"]:
                big_num["num"] = int(number)
                big_num["pos"] = pos + 1

            pos += 1
        battery_order += str(big_num["num"])
        big_num["num"] = 0

    count += int(battery_order)

print(count)  # 168617068915447