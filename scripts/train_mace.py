import subprocess

# nvidia-smi --query-gpu=name,temperature.gpu,utilization.gpu,memory.used,memory.total,power.draw --format=csv -l 1
# to see how gpu is performing
command = [
    "mace_run_train",

    "--name=Fe2Mn4O12Re2_MACE",

    # Dataset
    "--train_file=data/processed/Fe2Mn4O12Re2_train.xyz",
    "--valid_file=data/processed/Fe2Mn4O12Re2_valid.xyz",

    # Reference labels
    "--energy_key=energy",
    "--forces_key=forces",

    # Atomic energies
    "--E0s=average",

    # Model
    "--model=ScaleShiftMACE",
    "--num_interactions=2",
    "--hidden_irreps=128x0e + 128x1o",

    # Cutoff
    "--r_max=5.0",

    # Training
    "--max_num_epochs=100",
    "--batch_size=4",
    "--valid_batch_size=4",

    # Loss
    "--loss=weighted",

    # Optimizer
    "--optimizer=adam",
    "--lr=0.01",

    # Device
    "--device=cuda",

    # Reproducibility
    "--seed=42",

    # Output
    "--results_dir=results/Fe2Mn4O12Re2",
]

print("Running MACE training...\n")

subprocess.run(command, check=True)
