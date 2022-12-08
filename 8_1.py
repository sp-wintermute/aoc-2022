import numpy as np
forest = np.array([[int(x) for x in line] for line in input_data.split("\n")])

def build_incremental_array(line):
    indices = []
    current_max = -1
    for i, tree in enumerate(line):
        if tree > current_max:
            indices.append(i)
            current_max = tree
    return indices

def find_visible_trees(forest, axis=1):
    col_ix_of_visible_trees = [build_incremental_array(line) for line in forest]
    row_ix_of_visible_trees = np.array([[i] * len(row) for i, row in enumerate(col_ix_of_visible_trees)])
    col_ix_of_visible_trees, row_ix_of_visible_trees = (np.hstack(col_ix_of_visible_trees), 
                                                        np.hstack(row_ix_of_visible_trees))
    return row_ix_of_visible_trees, col_ix_of_visible_trees

def count_visible_trees(forest, row_ix_of_visible_trees, col_ix_of_visible_trees, count_matrix):
    chosen_trees = forest[row_ix_of_visible_trees, col_ix_of_visible_trees]
    chosen_counts = count_matrix[row_ix_of_visible_trees, col_ix_of_visible_trees]
    chosen_trees = chosen_trees[chosen_counts != 1]
    return len(chosen_trees)

tree_counts = []
count_matrix = np.zeros(forest.shape)
for i in range(4):
    row_ix_of_visible_trees, col_ix_of_visible_trees = find_visible_trees(forest)
    tree_counts.append(count_visible_trees(forest, 
                                           row_ix_of_visible_trees, 
                                           col_ix_of_visible_trees,
                                           count_matrix))
    count_matrix[row_ix_of_visible_trees, col_ix_of_visible_trees] = 1
    forest, count_matrix = np.rot90(forest), np.rot90(count_matrix)
print(tree_counts)
 
