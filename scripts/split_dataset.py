from pathlib import Path
from ase.io import iread, write
import random

DATASET = "data/raw/mag188_sample_trajectories.extxyz"
OUTPUT_DIR = Path("data/processed")

TARGET_FORMULA = "Fe2Mn4O12Re2"

SEED = 42
TRAIN_RATIO = 0.80
VALID_RATIO = 0.10

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

structures = []

# Read all configurations
for atoms in iread(DATASET, index=":"):
    if atoms.get_chemical_formula() == TARGET_FORMULA:
        structures.append(atoms)

print("Target formula:", TARGET_FORMULA)
print("Total configurations found:", len(structures))

if len(structures) == 0:
    raise RuntimeError("No configurations found!")

# Shuffle reproducibly
random.seed(SEED)
random.shuffle(structures)

# Calculate split sizes
n = len(structures)

n_train = int(n * TRAIN_RATIO)
n_valid = int(n * VALID_RATIO)

train_structures = structures[:n_train]
valid_structures = structures[n_train:n_train + n_valid]
test_structures = structures[n_train + n_valid:]

print("\nDataset split:")
print("Train:", len(train_structures))
print("Validation:", len(valid_structures))
print("Test:", len(test_structures))

# Output files
train_file = OUTPUT_DIR / "Fe2Mn4O12Re2_train.xyz"
valid_file = OUTPUT_DIR / "Fe2Mn4O12Re2_valid.xyz"
test_file = OUTPUT_DIR / "Fe2Mn4O12Re2_test.xyz"

write(train_file, train_structures)
write(valid_file, valid_structures)
write(test_file, test_structures)

print("\nFiles written:")
print(train_file)
print(valid_file)
print(test_file)