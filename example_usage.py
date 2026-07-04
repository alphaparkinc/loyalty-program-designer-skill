"""
example_usage.py -- Demonstrates the LoyaltyProgramClient SDK.
"""
from client import LoyaltyProgramClient

def main():
    client = LoyaltyProgramClient()

    print("[Loyalty Program Designer]")
    result = client.design(
        brand_name="GlowBeauty",
        avg_order_value=65.00,
        purchase_frequency=4.5,
        num_tiers=3,
        points_per_dollar=2.0,
        redemption_rate_per_point=0.005,
    )
    print(f"Program: {result['program_name']}")
    print(f"\nTier Structure:")
    for tier in result["tiers"]:
        print(f"  {tier['color']} {tier['tier']}")
        print(f"    Threshold: ${tier['annual_spend_threshold_usd']:,}/yr | {tier['points_threshold']:,} pts | {tier['point_multiplier']}x multiplier")
        print(f"    Est. Customers: {tier['estimated_pct_of_customers']}")
        for b in tier["benefits"][:2]:
            print(f"    + {b}")
    ps = result["points_system"]
    print(f"\nPoints System:")
    print(f"  Earn Rate: {ps['base_earn_rate']}")
    print(f"  Redemption: {ps['redemption_value']}")
    print(f"  Example: {ps['example']}")
    print(f"  Bonus Events: {len(ps['bonus_events'])} special earning opportunities")
    roi = result["roi_projection"]
    print(f"\nROI Projection:")
    print(f"  Avg Reward Cost per Order: ${roi['avg_reward_cost_per_order']:.2f} ({roi['avg_reward_pct_of_sale']}% of sale)")
    print(f"  Est. Retention Lift: +{roi['estimated_retention_lift_pct']}%")
    print(f"  Net Benefit per Member/yr: ${roi['net_benefit_per_member']:.2f}")

if __name__ == "__main__":
    main()
