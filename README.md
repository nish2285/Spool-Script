# Spool-Script

A Python script to create fabrication spool sheets for piping systems.

## Features

- Generates plan view, isometric view, and section view drawings
- Includes dimensions and annotations
- Creates Bill of Materials (BOM)
- Provides legend for drawings

## Requirements

- Python 3.x
- matplotlib
- numpy

## Installation

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the script:
```bash
python create_spools.py
```

This will create sample spool sheets in the `spool_sheets` directory.

## Customization

Modify the `sample_pipes` list in `create_spools.py` to define your own pipe configurations.

Each pipe should have:
- `start`: [x, y, z] coordinates
- `end`: [x, y, z] coordinates
- `length`: length in mm
- `diameter`: diameter in mm