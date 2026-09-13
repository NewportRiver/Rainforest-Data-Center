#!/usr/bin/env python3
"""Transparent first-pass balance calculator; not a certification model."""

import json
import sys
from pathlib import Path


def calculate(data: dict) -> dict:
    it_mwh = float(data["annual_it_energy_mwh"])
    facility_mwh = it_mwh * float(data["pue"])
    heat_mwh = facility_mwh * float(data["heat_rejection_fraction"])
    useful_heat_mwh = heat_mwh * float(data["heat_reuse_fraction"])

    net_water = (
        float(data["annual_water_withdrawal_m3"])
        - float(data["annual_water_returned_m3"])
        - float(data["verified_replenishment_m3"])
    )
    operational = facility_mwh * float(data["electricity_tco2e_per_mwh"])
    gross_carbon = operational + float(data["annualized_embodied_tco2e"])
    net_carbon = (
        gross_carbon
        - float(data["verified_avoided_tco2e"])
        - float(data["durable_additional_removals_tco2e"])
    )

    return {
        "facility_energy_mwh": round(facility_mwh, 2),
        "gross_heat_rejected_mwh": round(heat_mwh, 2),
        "useful_heat_recovered_mwh": round(useful_heat_mwh, 2),
        "residual_heat_mwh": round(heat_mwh - useful_heat_mwh, 2),
        "net_watershed_use_m3": round(net_water, 2),
        "gross_lifecycle_tco2e": round(gross_carbon, 2),
        "net_climate_impact_tco2e": round(net_carbon, 2),
    }


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("Usage: python model/balance.py model/example.json")
    source = Path(sys.argv[1])
    result = calculate(json.loads(source.read_text(encoding="utf-8")))
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
