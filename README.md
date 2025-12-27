# pupillometer-ghg
calculate the greenhouse gas emissions from penlights and hardware pupillometers

## Overview
All analyses and figures in this study were generated using open-source Python tools. The workflow models the life-cycle carbon footprint (kg CO₂e) of single-use ICU devices, annualized to per-bed-year values under varying occupancy and utilization.

The repository is structured as a lightweight, fully reproducible pipeline.

Try the interactive version of the calculator [here]().
```
pupillometry-carbon/
├── src/pupillo/
│   ├── __init__.py
│   ├── params.py          # Scenario parameters and constants
│   ├── model.py           # Core functions for per-patient and per-bed-year calculations
│   ├── plots.py           # Figure generation (heatmaps, contour plots, bar charts)
│   └── utils.py           # Shared helpers (unit conversions, color scales, etc.)
├── scripts/
│   ├── make_all_figures.py  # Main driver: regenerates all manuscript figures
│   ├── sensitivity_test.py  # Optional: uncertainty/sensitivity analysis
│   └── export_table.py      # Generates CSV summary tables
├── data/
│   ├── assumptions.json     # Emission factors and scenario metadata
│   └── results.csv          # Generated outputs (kg CO₂e/bed-year)
└── docs/
│   └── methods.md           # This file (detailed documentation)
│
└── index.html             # Interactive web based version of the primary figures (allows you to easily change assumptions)
```

Analyses were performed on macOS Sequioa 15.6 using:
* Python 3.11
* NumPy 1.26
* pandas 2.2
* Matplotlib 3.8
* SciPy 1.11 (for contour interpolation)
* Seaborn 0.13 (for color palettes)

