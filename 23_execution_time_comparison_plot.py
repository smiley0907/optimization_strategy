plt.figure(figsize=(8, 5))

plt.plot(
    circuit_depths,
    comparison_df[
        "Execution Time (s)_Conventional"
    ],
    marker="o",
    label="Conventional VQA"
)

plt.plot(
    circuit_depths,
    comparison_df[
        "Execution Time (s)_Adaptive"
    ],
    marker="s",
    label="Proposed Adaptive VQA"
)

plt.xlabel("Circuit Depth")
plt.ylabel("Execution Time (s)")
plt.title(
    "Execution-Time Comparison "
    "Across Circuit Depths"
)

plt.legend()
plt.grid(True)
plt.show()
