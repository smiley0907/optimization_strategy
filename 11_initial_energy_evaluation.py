initial_energy_results = []

for depth in circuit_depths:

    energy = objective_function(
        initial_parameters[depth],
        depth
    )

    initial_energy_results.append({
        "Circuit Depth": depth,
        "Initial Energy": energy
    })

initial_energy_df = pd.DataFrame(
    initial_energy_results
)

initial_energy_df
