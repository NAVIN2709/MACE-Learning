from pathlib import Path
from ase.io import iread
from collections import Counter
import numpy as np
import matplotlib.pyplot as plt

DATASET = "data/raw/mag188_sample_trajectories.extxyz"
energies = []
force_magnitudes = []
configs_per_material = Counter()


print("Reading dataset...")

for atoms in iread(DATASET, index=":"):

    try:
        energy = atoms.get_potential_energy()
        energies.append(energy)
    except Exception:
        pass

    try:
        forces = atoms.get_forces()

        magnitudes = np.linalg.norm(forces, axis=1)

        force_magnitudes.extend(magnitudes)

    except Exception:
        pass

    material_id = atoms.info.get("material_id")

    if material_id is not None:
        configs_per_material[material_id] += 1


energies = np.array(energies)
force_magnitudes = np.array(force_magnitudes)

plt.figure(figsize=(8, 5))

plt.hist(energies, bins=50)

plt.xlabel("Energy (eV)")
plt.ylabel("Number of configurations")
plt.title("MAG188 Energy Distribution")

plt.tight_layout()
plt.show()


plt.figure(figsize=(8, 5))

plt.hist(force_magnitudes, bins=100)

plt.xlabel("Force magnitude (eV/Å)")
plt.ylabel("Number of atoms")
plt.title("MAG188 Force Distribution")

plt.tight_layout()
plt.show()

counts = list(configs_per_material.values())

plt.figure(figsize=(8, 5))

plt.hist(counts, bins=30)

plt.xlabel("Configurations per material")
plt.ylabel("Number of materials")
plt.title("Configurations per Material")

plt.tight_layout()
plt.show()


print("\n" + "=" * 60)
print("VISUALIZATION STATISTICS")
print("=" * 60)

print("Energy range:", energies.min(), "to", energies.max())

print(
    "Force magnitude range:",
    force_magnitudes.min(),
    "to",
    force_magnitudes.max()
)

print(
    "Configurations/material:",
    min(counts),
    "to",
    max(counts)
)

print(
    "Average configurations/material:",
    np.mean(counts)
)

print(
    "Median configurations/material:",
    np.median(counts)
)