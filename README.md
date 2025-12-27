# pupillometer-ghg
calculate the greenhouse gas emissions from disposable penlights and hardware pupillometers

## Overview


### Calculations
Carbon emissions per ICU bed was the metric used.
```math
E_{bed} = S_p \times \left( \frac{365 \times occupancy}{LOS} \right) \times f_{use}
```
* Sp​ is the emission associated with one device per patient (kg CO₂e/patient). 

* Occupancy is the fraction of the year the bed is in use (e.g., 0.9 = 90 %). 

* LOS (length of stay) is the average number of days per patient in that ICU.

* f_{use}​ is the fraction of those patients who receive the device (for example, fraction of ICU patients who undergo pupillometry). 

## How this repository works
All analyses and figures in this study were generated using open-source Python tools. The workflow models the life-cycle carbon footprint (kg CO₂e) of single-use ICU devices, annualized to per-bed-year values under varying occupancy and utilization.

The repository is structured as a lightweight, fully reproducible pipeline.

Try the interactive version of the calculator [here](https://nickmmark.github.io/pupillometer-ghg/).

### Files
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

### Libraries
Analyses were performed on macOS Sequioa 15.6 using:
* Python 3.11
* NumPy 1.26
* pandas 2.2
* Matplotlib 3.8
* SciPy 1.11 (for contour interpolation)
* Seaborn 0.13 (for color palettes)


### References
