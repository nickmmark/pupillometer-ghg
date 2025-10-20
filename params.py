
from dataclasses import dataclass

@dataclass(frozen=True)
class EmissionFactors:
    plastic_prod: float = 3.3
    paperboard: float = 0.9
    truck_tkm: float = 0.12
    landfill_plastic: float = 0.27

EF = EmissionFactors()

@dataclass(frozen=True)
class SpecCase:
    plastic_g: float
    pouch_g: float
    carton_g: float
    electronics_kg: float
    sp_kg: float

SPEC_CASES = {
    "low":  SpecCase(plastic_g=15, pouch_g=6,  carton_g=4,  electronics_kg=0.0,   sp_kg=0.09),
    "mid":  SpecCase(plastic_g=20, pouch_g=8,  carton_g=5,  electronics_kg=0.010, sp_kg=0.13),
    "high": SpecCase(plastic_g=25, pouch_g=10, carton_g=6,  electronics_kg=0.020, sp_kg=0.20),
}

PENLIGHT_SP_KG = 0.20

LOS_DAYS = 4.0
