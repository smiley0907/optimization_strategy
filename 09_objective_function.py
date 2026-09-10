def objective_function(params, depth):
    qc = create_parameterized_circuit(params, depth)

    state = Statevector.from_instruction(qc)

    energy = np.real(
        state.expectation_value(H)
    )

    return float(energy)
