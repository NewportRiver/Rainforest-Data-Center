#!/usr/bin/env python3
"""First-order Mars biodome energy, heat, water, and gas balance."""

import json
import sys
from pathlib import Path


def calculate(d: dict) -> dict:
    people = float(d["population"])
    it_kw = float(d["average_it_load_kw"])
    pue = float(d["pue"])
    facility_kw = it_kw * pue
    lighting_kw = float(d["average_crop_lighting_kw"])
    other_kw = float(d["average_other_electrical_kw"])
    total_kw = facility_kw + lighting_kw + other_kw

    dc_heat_kw = facility_kw
    useful_dc_heat_kw = dc_heat_kw * float(d["useful_heat_fraction"])
    residual_dc_heat_kw = dc_heat_kw - useful_dc_heat_kw

    water_demand = people * float(d["gross_water_demand_kg_per_person_day"])
    recovered = water_demand * float(d["water_recovery_fraction"])
    makeup = water_demand - recovered

    oxygen_demand = people * float(d["oxygen_kg_per_person_day"])
    crop_oxygen = oxygen_demand * float(d["crop_oxygen_fraction"])
    backup_oxygen = oxygen_demand - crop_oxygen

    co2_output = people * float(d["co2_kg_per_person_day"])
    crop_co2 = co2_output * float(d["crop_co2_uptake_fraction"])
    remaining_co2 = co2_output - crop_co2

    return {
        "average_facility_compute_power_kw": round(facility_kw, 2),
        "average_total_electrical_load_kw": round(total_kw, 2),
        "daily_electrical_energy_mwh": round(total_kw * 24 / 1000, 2),
        "data_center_heat_kw": round(dc_heat_kw, 2),
        "useful_data_center_heat_kw": round(useful_dc_heat_kw, 2),
        "residual_data_center_heat_to_reject_kw": round(residual_dc_heat_kw, 2),
        "gross_water_demand_kg_day": round(water_demand, 2),
        "water_recovered_kg_day": round(recovered, 2),
        "water_makeup_kg_day": round(makeup, 2),
        "oxygen_demand_kg_day": round(oxygen_demand, 2),
        "crop_oxygen_credit_kg_day": round(crop_oxygen, 2),
        "backup_oxygen_required_kg_day": round(backup_oxygen, 2),
        "crew_co2_output_kg_day": round(co2_output, 2),
        "crop_co2_uptake_kg_day": round(crop_co2, 2),
        "co2_for_other_processing_kg_day": round(remaining_co2, 2),
    }


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("Usage: python model/mars_balance.py model/mars_100_people.json")
    data = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    print(json.dumps(calculate(data), indent=2))


if __name__ == "__main__":
    main()
