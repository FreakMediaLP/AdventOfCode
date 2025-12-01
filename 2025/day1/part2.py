from functions import *

cur_lock = 50
zero_count = 0

for line in read_lines():
    operation = line[0]
    turns = int(line[1:])
    print(f"{operation}{turns}")

    match operation:
        case "L":
            while turns > 0:
                cur_lock = cur_lock - 1
                turns = turns - 1

                if cur_lock < 0:
                    cur_lock = cur_lock + 100
                if cur_lock == 0:
                    zero_count += 1
        case "R":
            while turns > 0:
                cur_lock = cur_lock + 1
                turns = turns - 1

                if cur_lock > 99:
                    cur_lock = cur_lock - 100
                if cur_lock == 0:
                    zero_count += 1

    start = cur_lock
    print(f"-> {cur_lock}\n")

print(zero_count)  # 6819
