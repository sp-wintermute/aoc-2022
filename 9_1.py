commands = input_data.split("\n")
trace = np.zeros([500, 500])
head_pos = [250, 250]
tail_pos = [250, 250]
trace[tail_pos[0], tail_pos[1]] = 1

def parse_command(command):
    direc = command.split(" ")[0]
    steps = int(command.split(" ")[1])
    if direc in ("L", "R"):
        axis = 0
    else:
        axis = 1
    if direc in ("U", "R"):
        vec = + 1
    else:
        vec = -1
    return axis, vec, steps

def move_tail(head_pos, tail_pos, diagonally=False):
    axes = [0, 1]
    for axis in axes:
        distance = head_pos[axis] - tail_pos[axis]
        if abs(distance) <= 1 and not diagonally:
            #adjasent, do nothing
            pass
        else:
            # increment in the same direction
            tail_pos[axis] += int(distance / abs(distance))
            if not diagonally:
                break
    return tail_pos

def follow(head_pos, tail_pos):
    # are they in the same row/col?
    axes = [0, 1]
    if any([head_pos[axis] == tail_pos[axis] for axis in axes]):
        tail_pos = move_tail(head_pos, tail_pos, diagonally=False)
    else:
        if not all([abs(head_pos[axis] - tail_pos[axis]) <= 1 for axis in axes]):
            tail_pos = move_tail(head_pos, tail_pos, diagonally=True)
    return tail_pos

for command in commands:
    axis, vec, steps = parse_command(command)
    for move in range(1, steps + 1):
        head_pos[axis] += vec
        tail_pos = follow(head_pos, tail_pos)
        trace[tail_pos[0], tail_pos[1]] = 1
        
print(trace.sum())
