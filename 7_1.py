with open("7_input.txt") as f:
    input_data = f.read()
    
states = []
ls = {}

ls_mode = False
for line in input_data.split("\n"):
    if ls_mode:
        if not line.startswith("$ cd"):
            ls["/".join(states)].append(line)
        else:
            ls_mode = False
    if not ls_mode:
        if line.startswith("$ cd"):
            target = line.split("cd ")[-1]
            if target != "..":
                states.append(target)
            else:
                states.pop()
        if line.startswith("$ ls"):
            ls["/".join(states)] = []
            ls_mode = True

def recursive_sum(di):
    return sum([
        int(x.split(" ")[0]) 
        if "dir" not in x
        else recursive_sum(di + "/" + x.split(" ")[-1])
        for x in ls[di]
    ])
    
sizes = {}
for di in ls:
    if recursive_sum(di) <= 100000:
        sizes[di] = recursive_sum(di)

print(sum(sizes.values()))
