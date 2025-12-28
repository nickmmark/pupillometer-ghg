# pupillometer-ghg
calculate the greenhouse gas emissions from disposable penlights and hardware pupillometers

![demonstration of interactive carbon savings reduction](https://github.com/nickmmark/pupillometer-ghg/blob/main/interactive_demo.gif)

## Overview
Critical care is carbon intensive. Intensive Care Units (ICUs) in the US produce approximately 138 kg CO2 per bed day, equivalent to driving over 350 miles every day.
Strategies to enhance ICU sustainability and reduced carbon emissions are necessary. (see [ICU OnePager for examples](https://onepagericu.com/icu-sustainability))
One potential strategy is to replace disposable penlights and hardware pupillometers with disposable eye covers with software based pupillometry that does not have any disposable component.
I estimate the carbon footprint inherent in disposable penlights and harware pupillometers and the potential carbon emissions saved by switching to software based pupillometry.

### Calculations
The carbon footprint of penlights and disposable eye covers was estimated using:
* ~3.0–3.5 kg CO₂e per kg of plastic
* ~0.7–1.0 kg CO₂e per kg paperboard packaging
* ~0.062–0.12 kg CO₂e per tonne-km for road-truck freight
* ~0.27 kg CO₂e per kg for end-of-life disposal of plastics in a landfill

The carbon footprint of using disposable penlights or hardware pupillometers with disposable eye covers was estimated using:
```math
E_{bed} = S_p \times \left( \frac{365 \times occupancy}{LOS} \right) \times f_{use}
```
* $E_{bed}$ is the carbon emissions per ICU bed
* $S_p$​ is the emission associated with one device per patient (kg CO₂e/patient). 
* Occupancy is the fraction of the year the bed is in use (e.g., 0.9 = 90 %). 
* LOS (length of stay) is the average number of days per patient in that ICU.
* $f_{use}$​ is the fraction of those patients who receive the device (for example, fraction of ICU patients who undergo pupillometry). 

The total carbon footprint was estimated using differing assumptions about usage, and the low vs high estimates of carbon per device. Three estimates corresponding to low, medium, and high CO₂e cases were produced.


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
