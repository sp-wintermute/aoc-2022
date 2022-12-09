# 1_1
calories_per_elf = ([sum([int(x) for x in chunk.split("\n")]) for chunk in input_data.split("\n\n")])
print(max(calories_per_elf))

# 1_2
import numpy as np
top_3 = np.array(calories_per_elf)[np.argsort(calories_per_elf)][::-1][:3]
print(sum(top_3))

#2_1
score_mapping = {"X" : 1, "Y" : 2, "Z" : 3} #1 for Rock, 2 for Paper, and 3 for Scissors
# Each of the inputs has: one counterplay that wins, one that draws, one that loses
win_mapping = {"A" : {"Y" : 6, "X" : 3, "Z" : 0}, 
               "B" : {"Z" : 6, "Y" : 3, "X" : 0}, 
               "C" : {"X" : 6, "Z" : 3, "Y" : 0}}
scores = [score_mapping[line.split(" ")[1]] + win_mapping[line.split(" ")[0]][line.split(" ")[1]] for line in input_data.split("\n")]
print(sum(scores))

#2_2
score_mapping = {"rock" : 1, "paper" : 2, "scissors" : 3}
win_mapping = {"A" : {"paper" : 6, "rock" : 3, "scissors" : 0}, 
               "B" : {"scissors" : 6, "paper" : 3, "rock" : 0}, 
               "C" : {"rock" : 6, "scissors" : 3, "paper" : 0}}
win_to_move_mapping = {"X" : 2, "Y" : 1, "Z" : 0} # X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win
scores = [win_mapping[line.split(" ")[0]]
          [list(win_mapping[line.split(" ")[0]].keys())[win_to_move_mapping[line.split(" ")[1]]]] +
          score_mapping[list(win_mapping[line.split(" ")[0]].keys())[win_to_move_mapping[line.split(" ")[1]]]]
          for line in input_data.split("\n")]
print(sum(scores))

#3_1
items =          [ord(char) - 96 if char.islower()
                  else ord(char) - 38
                  for char in 
                [list(set([s
                  for s in rucksack[:int(len(rucksack)/2)]
                  if s in rucksack[int(len(rucksack)/2):] ]) )[0]
                  for rucksack in input_data.split("\n")]
    ]
print(sum(items))

#3_2
groups = [ord(char) - 96 if char.islower()
                  else ord(char) - 38
                  for char in 
                [list(set(s for s in group[0] if (s in group[1] and s in group[2])))[0]
                for group in np.reshape(np.array(input_data.split("\n")), 
                [int(len(input_data.split("\n"))/3), 3]) 
                ]
         ]
print(sum(groups))

#4_1
ranges = [[ True if (int(pair.split(",")[0].split("-")[0]) >= int(pair.split(",")[1].split("-")[0] )
                    and int(pair.split(",")[0].split("-")[1]) <= int(pair.split(",")[1].split("-")[1] ))
                    or (int(pair.split(",")[1].split("-")[0]) >= int(pair.split(",")[0].split("-")[0] )
                    and int(pair.split(",")[1].split("-")[1]) <= int(pair.split(",")[0].split("-")[1] )) 
           else False]
          [0]
          for pair in input_data.split("\n")
]
print(sum(ranges))

#4_2
ranges = [[ True if 
           any([x 
                in range(int(pair.split(",")[1].split("-")[0]), int(pair.split(",")[1].split("-")[1]) + 1)
                for x in range(int(pair.split(",")[0].split("-")[0]), int(pair.split(",")[0].split("-")[1]) + 1)
               ])  
            else False]
          [0]
          for pair in input_data.split("\n")]
print(sum(ranges))

#5_1
stacks = [['R', 'G', 'J', 'B', 'T', 'V', 'Z'],
          ['J', 'R', 'V', 'L'],
          ['S', 'Q', 'F'],
          ['Z', 'N', 'H', 'L', 'F', 'V', 'Q', 'G'],
          ['R', 'Q', 'T', 'J', 'C', 'S', 'M', 'W'],
          ['S', 'W', 'T', 'C', 'H', 'F'],
          ['D', 'Z', 'C', 'V', 'F', 'N', 'J'],
          ['L', 'G', 'Z', 'D', 'W', 'R', 'F', 'Q'],
          ['J', 'B', 'W', 'V', 'P']]
import re
instructions = [line for line in input_data.split("\n") if line.startswith("move")]
for instruction in instructions:
    matches = re.search("move ([\d]+) from ([\d]+) to ([\d]+)", instruction)
    for _ in range(int(matches[1])):
        stacks[int(matches[3]) - 1].append(stacks[int(matches[2]) - 1].pop())
print ("".join([s[-1] for s in stacks]))
 
#5_2
for instruction in instructions:
    matches = re.search("move ([\d]+) from ([\d]+) to ([\d]+)", instruction)
    for ix in range(1, int(matches[1]) + 1):
        ix = ix - int(matches[1]) - 1
        stacks[int(matches[3]) - 1].append(stacks[int(matches[2]) - 1][ix])
        del stacks[int(matches[2]) - 1][ix]
print ("".join([s[-1] for s in stacks]))


#6_1
block = ""
for i, s in enumerate(input_data):
    block += s
    block = block[-4:]
    if not any([block.count(x) > 1 for x in block]) and len(block) == 4:
        print(block, i + 1)
        break

#6_2
block = ""
for i, s in enumerate(input_data):
    block += s
    block = block[-14:]
    if not any([block.count(x) > 1 for x in block]) and len(block) == 14:
        print(block, nums, i + 1)
        break
          
  
