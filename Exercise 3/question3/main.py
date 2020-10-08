def num_atoms(amount_elements, atomic_weight=196.97):
    num_moles = amount_elements/atomic_weight
    atom_number = (num_moles*6.022) * (10**23)
    print(atom_number)

num_atoms(10)
num_atoms(10, 12.001)
num_atoms(10, 1.008)





