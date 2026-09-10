initial_parameters = {}

for depth in circuit_depths:

    rng = np.random.default_rng(RANDOM_SEED)

    initial_parameters[depth] = rng.uniform(
        -np.pi,
        np.pi,
        num_parameters[depth]
    )

print("Initial parameters generated using random seed 42.")
