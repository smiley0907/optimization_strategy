conventional_results = []
conventional_histories = {}

for depth in circuit_depths:

    params = initial_parameters[depth].copy()
    history = []

    def conventional_objective(x):
        energy = objective_function(x, depth)
        history.append(energy)
        return energy

    start_time = time.perf_counter()

    result = minimize(
        conventional_objective,
        params,
        method="COBYLA",
        options={
            "maxiter": MAX_EVALUATIONS,
            "rhobeg": 0.5,
            "tol": 1e-6
        }
    )

    execution_time = (
        time.perf_counter() - start_time
    )

    final_energy = objective_function(
        result.x,
        depth
    )

    conventional_histories[depth] = history

    conventional_results.append({
        "Circuit Depth": depth,
        "Initial Energy": objective_function(
            params, depth
        ),
        "Final Energy": final_energy,
        "Iterations": result.nfev,
        "Execution Time (s)": execution_time
    })

conventional_df = pd.DataFrame(
    conventional_results
)

conventional_df
