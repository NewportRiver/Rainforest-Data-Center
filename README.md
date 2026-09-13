# Rainforest Data Center

An open research and engineering project exploring how data centers and tropical ecosystems could coexist as a coupled system—exchanging heat, water, carbon, and nutrients while targeting net-zero operational emissions, no consumptive freshwater loss, and measurable ecological restoration.

> **Status:** Early concept and modeling framework. Computing ultimately releases heat. The engineering goal is zero harmful net thermal impact at the defined system boundary through heat avoidance, recovery, displacement, storage, and ecosystem-compatible rejection.

## Vision

Conventional data centers treat their surroundings as a source of electricity and water and as a sink for heat. This project explores a facility designed as an ecological participant:

- renewable electricity and flexible computing loads;
- useful recovery of low-grade heat before environmental discharge;
- recirculated cooling water and rain harvesting without watershed depletion;
- constructed wetlands and biological systems for water polishing;
- reforestation, soil carbon, habitat connectivity, and local livelihoods;
- transparent mass, energy, water, and carbon accounting.

## Core architecture

```mermaid
flowchart TD
    DC["Data center"] -->|recoverable heat| HR["Heat recovery"]
    HR --> GH["Greenhouse / drying / biochar"]
    DC -->|closed-loop water| WT["Water treatment"]
    WT --> CW["Constructed wetland"]
    CW -->|polished water| DC
    RF["Rainforest restoration"] -->|shade, evapotranspiration, carbon| SITE["Local microclimate"]
    SITE --> DC
    GH -->|biochar and nutrients| RF
```

## Mars biodome extension

The project now includes a researched 100-person Mars settlement architecture in which a liquid-cooled data center serves as the habitat's thermal and computational core.

- [Mars biodome research report](MARS_BIODOME.md)
- [Mars mass and energy balance model](model/mars_balance.py)
- [100-person scenario](model/mars_100_people.json)

Run the Mars model:

```bash
python model/mars_balance.py model/mars_100_people.json
```

## Design principles

1. Avoid intact-forest clearing; prefer degraded land or brownfields.
2. Do not compete with communities or ecosystems for water.
3. Respect thermodynamics: heat can be reused, shifted, or rejected safely—not destroyed.
4. Count construction, backup power, refrigerants, hardware, transmission, and land-use change.
5. Require additional, measurable ecological benefit.
6. Design with local and Indigenous communities.
7. Publish auditable methods, sensor data, boundaries, and uncertainty.

## Repository map

- `docs/concept.md` — system concept, boundaries, risks, and research questions
- `docs/roadmap.md` — staged path from model to field demonstrator
- `model/balance.py` — first-pass energy, water, and carbon calculator
- `model/example.json` — illustrative scenario inputs
- `CONTRIBUTING.md` — responsible contribution guidance

## Quick start

```bash
python model/balance.py model/example.json
```

## License

Apache License 2.0.
