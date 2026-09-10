plt.figure(figsize=(8, 5))

plt.plot(
    circuit_depths,
    comparison_df["Iterations_Conventional"],
    marker="o",
    label="Conventional VQA"
)

plt.plot(
    circuit_depths,
    comparison_df["Iterations_Adaptive"],
    marker="s",
    label="Proposed Adaptive VQA"
)

plt.xlabel("Circuit Depth")
plt.ylabel("Optimization Iterations")
plt.title(
    "Optimization Iteration Comparison "
    "Across Circuit Depths"
)

plt.legend()
plt.grid(True)
plt.show()
