# genpark-loyalty-program-designer-skill

> **GenPark AI Agent Skill** -- Design tiered customer loyalty programs with points, rewards, and ROI projections.

## Features

- 2-5 tier configurations (Bronze/Silver/Gold/Platinum/Diamond)
- Points earning rules, multipliers, and redemption calculator
- Pre-built tier benefits library
- Bonus points events (birthday, referrals, reviews)
- ROI projection: retention lift, cost per member, net benefit

## Quick Start

```python
from client import LoyaltyProgramClient

client = LoyaltyProgramClient()
program = client.design(
    brand_name="MyStore",
    avg_order_value=50,
    purchase_frequency=4,
    num_tiers=3,
)
print(program["program_name"])
for tier in program["tiers"]:
    print(f"{tier['tier']}: {tier['annual_spend_threshold_usd']} USD threshold")
```

## Installation

```bash
python example_usage.py  # No external dependencies
```

---
Built by [GenPark](https://genpark.ai) | [alphaparkinc](https://github.com/alphaparkinc)
