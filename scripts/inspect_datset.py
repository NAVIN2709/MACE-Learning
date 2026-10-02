from ase.io import read

DATASET = "data/raw/mag188_sample_trajectories.extxyz"

print("Loading dataset...")

structures = read(DATASET, index=":")

print("=" * 60)
print("DATASET SUMMARY")
print("=" * 60)

print("Number of configurations:", len(structures))

atoms = structures[0]

print("\n" + "=" * 60)
print("FIRST CONFIGURATION")
print("=" * 60)

print("Formula:", atoms.get_chemical_formula())
print("Number of atoms:", len(atoms))

print("\nChemical symbols:")
print(atoms.get_chemical_symbols())

print("\nPositions shape:")
print(atoms.get_positions().shape)

print("\nCell:")
print(atoms.cell)

print("\nPeriodic boundary conditions:")
print(atoms.pbc)

print("\nEnergy:")

try:
    print(atoms.get_potential_energy())
except Exception as e:
    print("Could not read energy:", e)

print("\nForces shape:")

try:
    print(atoms.get_forces().shape)
except Exception as e:
    print("Could not read forces:", e)

print("\n" + "=" * 60)
print("STRUCTURE METADATA")
print("=" * 60)

print("\natoms.info:")
for key, value in atoms.info.items():
    print(f"{key}: {value}")

print("\nAtoms arrays:")
for key, value in atoms.arrays.items():
    print(f"{key}: shape={value.shape}")