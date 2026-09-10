def create_parameterized_circuit(params, depth):
    qc = QuantumCircuit(2)

    parameter_index = 0

    for _ in range(depth):
        qc.ry(params[parameter_index], 0)
        parameter_index += 1

        qc.ry(params[parameter_index], 1)
        parameter_index += 1

        qc.cx(0, 1)

    return qc
