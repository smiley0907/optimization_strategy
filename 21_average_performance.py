average_iteration_reduction = (
    comparison_df[
        "Iteration Reduction (%)"
    ].mean()
)

average_time_reduction = (
    comparison_df[
        "Time Reduction (%)"
    ].mean()
)

maximum_energy_difference = (
    comparison_df[
        "Final Energy Difference"
    ].max()
)

average_energy_difference = (
    comparison_df[
        "Final Energy Difference"
    ].mean()
)

print(
    f"Average Iteration Reduction: "
    f"{average_iteration_reduction:.2f}%"
)

print(
    f"Average Execution-Time Reduction: "
    f"{average_time_reduction:.2f}%"
)

print(
    f"Maximum Final Energy Difference: "
    f"{maximum_energy_difference:.8f}"
)

print(
    f"Average Final Energy Difference: "
    f"{average_energy_difference:.8f}"
)
