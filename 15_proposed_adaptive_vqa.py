adaptive_results = []
adaptive_histories = {}

for depth in circuit_depths:

    params = initial_parameters[depth].copy()
    history = []

    def adaptive_objective(x):
        energy = objective_function(x, depth)
        history.append(energy)
        return energy

    start_time = time.perf_counter()

    result = minimize(
        adaptive_objective,
        params,
        method="COBYLA",
        options={
            "maxiter": MAX_EVALUATIONS,
            "rhobeg": 0.5,
            "tol": 1e-6,
            "f_target": E_TARGET
        }
    )

    execution_time = (
        time.perf_counter() - start_time
    )

    final_energy = objective_function(
        result.x,
        depth
    )

    adaptive_histories[depth] = history

    adaptive_results.append({
        "Circuit Depth": depth,
        "Final Energy": final_energy,
        "Iterations": result.nfev,
        "Execution Time (s)": execution_time,
        "Termination": "Adaptive target reached"
    })

adaptive_df = pd.DataFrame(
    adaptive_results
)

adaptive_df
