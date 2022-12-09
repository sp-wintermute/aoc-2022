forest = np.array([[int(x) for x in line] for line in input_data.split("\n")])

visibility = np.ones(forest.shape)
for i in range(forest.shape[0]):
    for j in range(forest.shape[1]):
        for sli in [forest[i, j + 1:], 
                    np.flip(forest[i, :j]), 
                    forest[i + 1:, j], 
                    np.flip(forest[:i, j])]:
            try:
                if not any(sli >= forest[i, j]):
                    visibility[i, j] *= len(sli)
                else:
                    visibility[i, j] *= np.argmax(sli >= forest[i, j]) + 1
            except:
                visibility[i, j] *= 0
print(visibility.max())
