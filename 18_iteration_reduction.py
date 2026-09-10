comparison_df["Iteration Reduction (%)"] = (
    (
        comparison_df["Iterations_Conventional"]
        -
        comparison_df["Iterations_Adaptive"]
    )
    /
    comparison_df["Iterations_Conventional"]
) * 100

display(
    comparison_df[
        [
            "Circuit Depth",
            "Iterations_Conventional",
            "Iterations_Adaptive",
            "Iteration Reduction (%)"
        ]
    ]
)
