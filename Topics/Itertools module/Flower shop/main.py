import itertools

for n_flowers in range(1, 4):
    for bouquet in itertools.combinations(flower_names, n_flowers):
        print(bouquet)
