###### Part 1 ######
commands = input_data.splitlines()
cycles = []
x = 1
for command in commands:
    if command == "noop":
        cycles.append(x)
    elif command.startswith(""):
        add = int(command.split(" ")[-1])
        cycles.append(x)
        cycles.append(x)
        x += add

signal_strength = 0
for num in [20, 60, 100, 140, 180, 220]:
    signal_strength += cycles[num - 1] * num
    
print(signal_strength)

###### Part 2 ######
draw_matrix = [["." for _ in range(40)] for __ in range(6)]
for row in range(6):
    for col in range(40):
        abs_pos = row * 40 + col
        sprite_loc = [cycles[abs_pos] - 1, cycles[abs_pos], cycles[abs_pos] + 1]
        if col in sprite_loc:
            draw_matrix[row][col] = "#"
           
 for r in draw_matrix:
    print("".join(r))
