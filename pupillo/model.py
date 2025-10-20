
import numpy as np

def patients_per_bed_year(occupancy: float, los_days: float) -> float:
    return (365.0 * occupancy) / los_days

def per_bed_year(sp_kg: float, occupancy: float, los_days: float, use_fraction: float) -> float:
    return sp_kg * patients_per_bed_year(occupancy, los_days) * use_fraction

def grid(occ_vals, use_vals, sp_kg: float, los_days: float):
    OCC, USE = np.meshgrid(occ_vals, use_vals)
    patients = OCC * 365.0 / los_days
    Z = sp_kg * patients * USE
    return OCC, USE, Z
