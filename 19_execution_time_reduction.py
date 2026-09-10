comparison_df["Time Reduction (%)"] = (
    (
        comparison_df["Execution Time (s)_Conventional"]
        -
        comparison_df["Execution Time (s)_Adaptive"]
    )
    /
    comparison_df["Execution Time (s)_Conventional"]
) * 100

display(
    comparison_df[
        [
            "Circuit Depth",
            "Time Reduction (%)"
        ]
    ]
)
