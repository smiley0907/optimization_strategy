plt.figure(figsize=(8, 5))

plt.bar(
    circuit_depths,
    comparison_df[
        "Iteration Reduction (%)"
    ]
)

plt.xlabel("Circuit Depth")
plt.ylabel("Iteration Reduction (%)")
plt.title(
    "Optimization Iteration Reduction "
    "Across Circuit Depths"
)

plt.grid(axis="y")
plt.show()
