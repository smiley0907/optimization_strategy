final_results = comparison_df[
    [
        "Circuit Depth",
        "Iterations_Conventional",
        "Iterations_Adaptive",
        "Iteration Reduction (%)",
        "Execution Time (s)_Conventional",
        "Execution Time (s)_Adaptive",
        "Time Reduction (%)",
        "Final Energy_Conventional",
        "Final Energy_Adaptive",
        "Final Energy Difference"
    ]
].copy()

display(final_results)
