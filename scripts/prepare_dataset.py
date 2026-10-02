from pathlib import Path
from ase.io import iread
from collections import Counter
import numpy as np

DATASET = "data/raw/mag188_sample_trajectories.extxyz"
print("=" * 60)
print("MAG188 DATASET ANALYSIS")
print("=" * 60)

print("Dataset:", DATASET)

# Statistics
num_configs = 0
atom_counts = []
formulas = Counter()
material_ids = set()
config_types = Counter()
ionic_steps = []

energies = []
force_magnitudes = []

print("\nReading structures...")

for atoms in iread(DATASET, index=":"):

    num_configs += 1

    # Number of atoms
    atom_counts.append(len(atoms))

    # Formula
    formulas[atoms.get_chemical_formula()] += 1

    # Metadata
    material_ids.add(atoms.info.get("material_id"))

    config_types[atoms.info.get("config_type")] += 1

    ionic_step = atoms.info.get("ionic_step")
    if ionic_step is not None:
        ionic_steps.append(ionic_step)

    # Energy
    try:
        energies.append(atoms.get_potential_energy())
    except Exception:
        pass

    # Forces
    try:
        forces = atoms.get_forces()

        magnitudes = np.linalg.norm(forces, axis=1)

        force_magnitudes.extend(magnitudes)

    except Exception:
        pass


print("\n" + "=" * 60)
print("BASIC STATISTICS")
print("=" * 60)

print("Configurations:", num_configs)

print("Unique materials:", len(material_ids))

print(
    "Unique formulas:",
    len(formulas)
)

print(
    "Atoms per structure:",
    min(atom_counts),
    "to",
    max(atom_counts)
)

print(
    "Average atoms per structure:",
    np.mean(atom_counts)
)

print(
    "Median atoms per structure:",
    np.median(atom_counts)
)


print("\n" + "=" * 60)
print("CONFIGURATION TYPES")
print("=" * 60)

for key, value in config_types.items():
    print(f"{key}: {value}")


print("\n" + "=" * 60)
print("ENERGY STATISTICS")
print("=" * 60)

if energies:

    energies = np.array(energies)

    print("Minimum:", energies.min())
    print("Maximum:", energies.max())
    print("Mean:", energies.mean())
    print("Std:", energies.std())


print("\n" + "=" * 60)
print("FORCE STATISTICS")
print("=" * 60)

if force_magnitudes:

    force_magnitudes = np.array(force_magnitudes)

    print("Minimum magnitude:", force_magnitudes.min())
    print("Maximum magnitude:", force_magnitudes.max())
    print("Mean magnitude:", force_magnitudes.mean())
    print("Std magnitude:", force_magnitudes.std())


print("\n" + "=" * 60)
print("MOST COMMON FORMULAS")
print("=" * 60)

for formula, count in formulas.most_common(20):

    print(f"{formula}: {count}")


print("\nAnalysis complete!")