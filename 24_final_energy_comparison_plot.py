plt.figure(figsize=(8, 5))

plt.plot(
    circuit_depths,
    comparison_df[
        "Final Energy_Conventional"
    ],
    marker="o",
    label="Conventional VQA"
)

plt.plot(
    circuit_depths,
    comparison_df[
        "Final Energy_Adaptive"
    ],
    marker="s",
    label="Proposed Adaptive VQA"
)

plt.xlabel("Circuit Depth")
plt.ylabel("Final Objective Energy")
plt.title(
    "Final Energy Comparison "
    "Across Circuit Depths"
)

plt.legend()
plt.grid(True)
plt.show()
