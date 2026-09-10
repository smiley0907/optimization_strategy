final_results.to_csv(
    "adaptive_vqa_results.csv",
    index=False
)

configuration_df.to_csv(
    "vqa_circuit_configurations.csv",
    index=False
)

print("Results exported successfully.")
