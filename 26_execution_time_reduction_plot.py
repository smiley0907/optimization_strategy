plt.figure(figsize=(8, 5))

plt.bar(
    circuit_depths,
    comparison_df[
        "Time Reduction (%)"
    ]
)

plt.xlabel("Circuit Depth")
plt.ylabel("Execution-Time Reduction (%)")
plt.title(
    "Execution-Time Reduction "
    "Across Circuit Depths"
)

plt.grid(axis="y")
plt.show()
