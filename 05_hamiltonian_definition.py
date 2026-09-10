H = SparsePauliOp.from_list([
    ("ZZ", 1.0),
    ("XI", 0.5),
    ("IX", 0.5)
])

GROUND_ENERGY = -np.sqrt(2)

print("Hamiltonian:")
print(H)

print("\nReference Ground-State Energy:")
print(GROUND_ENERGY)
