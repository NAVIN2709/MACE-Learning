# Fine-Tuning MACE for Atomistic Energy & Force Prediction

A Materials Informatics project using **MACE (Multi-Atomic Cluster Expansion)** to fine-tune a machine-learning interatomic potential for predicting **atomic energies and forces**.

## Material

**Fe₂Mn₄O₁₂Re₂**

The data was extracted from the **MAG188** atomistic trajectory dataset.

| Dataset    | Configurations |
| ---------- | -------------: |
| Train      |            887 |
| Validation |            110 |
| Test       |            112 |
| **Total**  |      **1,109** |

## Model

**ScaleShiftMACE**

* 2 interaction layers
* `128x0e + 128x1o`
* Cutoff: **5 Å**
* Epochs: **100**
* Batch size: **4**
* Optimizer: **Adam**
* Learning rate: **0.01**
* Energy : Force loss = **1 : 100**
* GPU: **CUDA**

## Results

Initial test performance:

| Metric |               RMSE |
| ------ | -----------------: |
| Energy | **167.5 meV/atom** |
| Forces |    **256.4 meV/Å** |

## Tools

`Python` · `PyTorch` · `MACE` · `ASE` · `NumPy` · `CUDA`

## Workflow

```text
MAG188 Dataset
      ↓
Material Selection
      ↓
Data Preparation
      ↓
Train / Validation / Test Split
      ↓
MACE Fine-Tuning
      ↓
Energy & Force Evaluation
```
