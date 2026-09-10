comparison_df["Final Energy Difference"] = (
    comparison_df["Final Energy_Conventional"]
    -
    comparison_df["Final Energy_Adaptive"]
).abs()

display(
    comparison_df[
        [
            "Circuit Depth",
            "Final Energy_Conventional",
            "Final Energy_Adaptive",
            "Final Energy Difference"
        ]
    ]
)
