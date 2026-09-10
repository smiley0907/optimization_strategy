comparison_df["Target Satisfied"] = (
    comparison_df[
        "Final Energy_Adaptive"
    ] <= E_TARGET
)

display(
    comparison_df[
        [
            "Circuit Depth",
            "Final Energy_Adaptive",
            "Target Satisfied"
        ]
    ]
)
