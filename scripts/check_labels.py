from ase.io import iread
from collections import Counter, defaultdict

DATASET = "data/raw/mag188_sample_trajectories.extxyz"

material_counts = Counter()
material_formulas = defaultdict(Counter)

for atoms in iread(DATASET, index=":"):
    material_id = atoms.info.get("material_id")

    # Actual structure formula from ASE
    formula = atoms.get_chemical_formula()

    material_counts[material_id] += 1
    material_formulas[material_id][formula] += 1

print("\nTop 20 MATERIAL IDs by number of configurations:\n")

for material_id, count in material_counts.most_common(20):
    formula = material_formulas[material_id].most_common(1)[0][0]
    print(f"{material_id:20} | {formula:20} | {count:4} configs")