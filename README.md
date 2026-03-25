# Curve Skeletonization (Milestone 1)

This project provides Milestone 1 scaffolding for NIfTI-based curve skeletonization.

## What Works in Milestone 1

- NIfTI load and save utilities.
- CLI that reads an input volume and writes an output volume.
- Multi-object decomposition and merge utilities.
- Synthetic fixture generation for test volumes.

Skeletonization core modules are present as explicit stubs and are implemented in later milestones.

## Installation

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Usage

```bash
python main.py -i /path/to/input.nii.gz -o /path/to/out.nii.gz
```

Optional arguments:

- `--root-method {max_fdt,topmost}`
- `--threshold-scale FLOAT`
- `--min-object-size INT`
- `--label-objects`

## Generate Synthetic Fixtures

```bash
python tests/fixtures/generate_fixtures.py
```

This creates:

- `tests/fixtures/straight_tube.nii.gz`
- `tests/fixtures/y_tube.nii.gz`
- `tests/fixtures/y_tube_noisy.nii.gz`
- `tests/fixtures/two_tubes.nii.gz`
