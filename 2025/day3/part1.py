from functions import *


lines = read_lines()
banks = []

for line in lines:
    banks.append(list(line.strip()))

count = 0
for bank in banks:
    big_num = {
        "num": "0", "pos": 0,
        "num2": "0", "pos2": 0
    }
    pos = 0
    for number in bank[:-1]:
        if int(number) > int(big_num["num"]):
            big_num["num"] = number
            big_num["pos"] = pos

        pos += 1

    pos = 0
    for number in bank[(big_num["pos"] + 1):]:
        if int(number) > int(big_num["num2"]):
            big_num["num2"] = int(number)
            big_num["pos2"] = pos

        pos += 1

    count += int(f"{big_num['num']}{big_num['num2']}")

print(count)  # 16993