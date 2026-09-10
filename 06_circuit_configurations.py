circuit_depths = [3, 6, 9, 12, 15]

num_parameters = {
    3: 4,
    6: 8,
    9: 12,
    12: 16,
    15: 20
}

num_gates = {
    3: 5,
    6: 10,
    9: 15,
    12: 20,
    15: 25
}

configuration_df = pd.DataFrame({
    "Circuit Depth": circuit_depths,
    "Number of Gates": [num_gates[d] for d in circuit_depths],
    "Number of Parameters": [num_parameters[d] for d in circuit_depths]
})

configuration_df
