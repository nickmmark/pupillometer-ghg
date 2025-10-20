
import numpy as np
from pathlib import Path
from pupillo.params import SPEC_CASES, PENLIGHT_SP_KG, LOS_DAYS
from pupillo.model import grid
from pupillo.plots import heatmap_with_isobars, comparison_barchart

FIG_DIR = Path(__file__).resolve().parents[1] / "figures"
FIG_DIR.mkdir(parents=True, exist_ok=True)

occ_vals = np.linspace(0.6, 1.0, 81)
use_vals = np.linspace(0.0, 1.0, 81)

max_spec = SPEC_CASES["high"].sp_kg * (365.0 / LOS_DAYS)

for name in ["low", "mid", "high"]:
    case = SPEC_CASES[name]
    OCC, USE, Z = grid(occ_vals, use_vals, sp_kg=case.sp_kg, los_days=LOS_DAYS)
    heatmap_with_isobars(
        OCC, use_vals, Z,
        title=f"CO₂e savings per bed-year — SPEC {name} (Sₚ={case.sp_kg:.2f} kg/patient)",
        xlabel="ICU bed occupancy (fraction)",
        ylabel="Pupillometry\nuse fraction",
        outfile=FIG_DIR / f"SPEC_{name}.png",
        vmin=0.0, vmax=max_spec, levels=np.arange(2, 36, 2)
    )

OCC, USE, Zpl = grid(occ_vals, use_vals, sp_kg=PENLIGHT_SP_KG, los_days=LOS_DAYS)
max_pl = PENLIGHT_SP_KG * (365.0 / LOS_DAYS)
heatmap_with_isobars(
    OCC, use_vals, Zpl,
    title="CO₂e savings per bed-year — Penlight (single vs shared use)",
    xlabel="ICU bed occupancy (fraction)",
    ylabel="Fraction of patients issued\na disposable penlight",
    outfile=FIG_DIR / "Penlight_combined.png",
    vmin=0.0, vmax=max_pl, levels=np.arange(2, 36, 2),
    hlines=[(0.99, (0,(3,3))), (0.2, (0,(6,2,1,2)))]
)

names = [
    "Inhaler (MDI→DPI)",
    "Penlight (single→shared)",
    "Pupillometry (SPEC→software)",
    "Bronchoscope reuse",
    "Pulse-ox probe reuse",
    "Reusable BP cuff",
    "ECG lead reuse"
]
mids  = [18, 14, 10, 10, 14, 10, 4]
lows  = [15,  8,  6,  5, 13,  7, 2]
highs = [20, 20, 13, 15, 16, 12, 5]
proposed = {"Penlight (single→shared)", "Pupillometry (SPEC→software)"}

comparison_barchart(names, mids, lows, highs, FIG_DIR / "Comparison_ranked_bw.png",
                    proposed_labels=proposed)

print("All figures written to", FIG_DIR)
