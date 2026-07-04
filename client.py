"""
loyalty-program-designer-skill: Client SDK
Design tiered customer loyalty programs with points, rewards, and ROI projections.
"""
from __future__ import annotations
from typing import Optional

TIER_CONFIGS = {
    2: [
        {"name": "Member", "color": "Silver", "threshold_multiplier": 0, "point_multiplier": 1.0, "emoji": ""},
        {"name": "Elite", "color": "Gold", "threshold_multiplier": 5, "point_multiplier": 2.0, "emoji": ""},
    ],
    3: [
        {"name": "Member", "color": "Silver", "threshold_multiplier": 0, "point_multiplier": 1.0, "emoji": ""},
        {"name": "Gold", "color": "Gold", "threshold_multiplier": 3, "point_multiplier": 1.5, "emoji": ""},
        {"name": "Platinum", "color": "Platinum", "threshold_multiplier": 8, "point_multiplier": 2.0, "emoji": ""},
    ],
    4: [
        {"name": "Bronze", "color": "Bronze", "threshold_multiplier": 0, "point_multiplier": 1.0, "emoji": ""},
        {"name": "Silver", "color": "Silver", "threshold_multiplier": 2, "point_multiplier": 1.25, "emoji": ""},
        {"name": "Gold", "color": "Gold", "threshold_multiplier": 5, "point_multiplier": 1.75, "emoji": ""},
        {"name": "Platinum", "color": "Platinum", "threshold_multiplier": 10, "point_multiplier": 2.5, "emoji": ""},
    ],
    5: [
        {"name": "Bronze", "color": "Bronze", "threshold_multiplier": 0, "point_multiplier": 1.0, "emoji": ""},
        {"name": "Silver", "color": "Silver", "threshold_multiplier": 2, "point_multiplier": 1.2, "emoji": ""},
        {"name": "Gold", "color": "Gold", "threshold_multiplier": 4, "point_multiplier": 1.5, "emoji": ""},
        {"name": "Platinum", "color": "Platinum", "threshold_multiplier": 8, "point_multiplier": 2.0, "emoji": ""},
        {"name": "Diamond", "color": "Diamond", "threshold_multiplier": 15, "point_multiplier": 3.0, "emoji": ""},
    ],
}

TIER_BENEFITS = {
    "Member":   ["Welcome bonus: 100 points", "Birthday reward: 2x points", "Early access to sales"],
    "Bronze":   ["Welcome bonus: 100 points", "Birthday reward: 2x points", "Early access to sales"],
    "Silver":   ["Free standard shipping on all orders", "Priority customer support", "Quarterly bonus points event"],
    "Gold":     ["Free expedited shipping", "Exclusive member pricing (5% off)", "Early product launches", "Dedicated account manager"],
    "Elite":    ["Free expedited shipping", "Exclusive member pricing (5% off)", "Early product launches", "Dedicated account manager"],
    "Platinum": ["Free express shipping", "Exclusive pricing (10% off)", "VIP event invitations", "Free gift with every order", "Personal stylist / advisor"],
    "Diamond":  ["Free express shipping", "Exclusive pricing (15% off)", "Annual VIP gift package", "Concierge service", "Invitations to brand events", "Co-creation opportunities"],
}


class LoyaltyProgramClient:
    """
    SDK for designing tiered customer loyalty programs.
    Generates tier definitions, points systems, and ROI projections.
    """

    def design(
        self,
        brand_name: str,
        avg_order_value: float,
        purchase_frequency: float,
        num_tiers: int = 3,
        points_per_dollar: float = 1.0,
        redemption_rate_per_point: float = 0.01,
    ) -> dict:
        """
        Design a complete loyalty program.

        Args:
            brand_name:               Brand name.
            avg_order_value:          Average order value (USD).
            purchase_frequency:       Average purchases per year.
            num_tiers:                Number of tiers (2-5).
            points_per_dollar:        Points earned per USD spent.
            redemption_rate_per_point: USD value per point at redemption.

        Returns:
            dict with program_name, tiers, points_system, roi_projection
        """
        num_tiers = max(2, min(num_tiers, 5))
        annual_spend = avg_order_value * purchase_frequency
        tier_configs = TIER_CONFIGS.get(num_tiers, TIER_CONFIGS[3])

        # Build tiers
        tiers = []
        for tc in tier_configs:
            threshold_annual = round(annual_spend * tc["threshold_multiplier"])
            threshold_points = int(threshold_annual * points_per_dollar)
            benefits = TIER_BENEFITS.get(tc["name"], TIER_BENEFITS["Member"])
            tiers.append({
                "tier": tc["name"],
                "color": tc["color"],
                "annual_spend_threshold_usd": threshold_annual,
                "points_threshold": threshold_points,
                "point_multiplier": tc["point_multiplier"],
                "benefits": benefits,
                "estimated_pct_of_customers": self._estimate_pct(tc["threshold_multiplier"]),
            })

        points_system = {
            "base_earn_rate": f"{points_per_dollar} point per $1 spent",
            "redemption_value": f"${redemption_rate_per_point:.3f} per point",
            "min_redemption": 500,
            "expiry": "Points expire after 12 months of inactivity",
            "bonus_events": [
                "2x points on your birthday month",
                "3x points during member appreciation events",
                "Bonus points for leaving a product review (50 pts)",
                "Referral bonus: 200 points per successful referral",
            ],
            "example": (
                f"Customer spends ${avg_order_value:.2f}: earns "
                f"{int(avg_order_value * points_per_dollar)} points "
                f"= ${avg_order_value * points_per_dollar * redemption_rate_per_point:.2f} in rewards value"
            )
        }

        roi = self._project_roi(avg_order_value, purchase_frequency, redemption_rate_per_point, points_per_dollar)

        program_name = self._name_program(brand_name, num_tiers)

        return {
            "program_name": program_name,
            "brand": brand_name,
            "tiers": tiers,
            "points_system": points_system,
            "roi_projection": roi,
            "num_tiers": num_tiers,
        }

    @staticmethod
    def _estimate_pct(multiplier: float) -> str:
        if multiplier == 0: return "100% (all members)"
        if multiplier <= 2: return "40-60%"
        if multiplier <= 5: return "15-25%"
        if multiplier <= 10: return "5-10%"
        return "1-3%"

    @staticmethod
    def _project_roi(aov: float, freq: float, redemption_rate: float, ppd: float) -> dict:
        avg_reward_cost = aov * ppd * redemption_rate
        avg_reward_pct = avg_reward_cost / aov * 100
        retention_lift = 15.0
        freq_lift = 0.2
        new_annual_revenue = aov * (freq * (1 + freq_lift))
        annual_cost_per_member = avg_reward_cost * freq
        annual_revenue_per_member = aov * freq
        net_benefit = new_annual_revenue - annual_cost_per_member
        return {
            "avg_reward_cost_per_order": round(avg_reward_cost, 2),
            "avg_reward_pct_of_sale": round(avg_reward_pct, 2),
            "estimated_retention_lift_pct": retention_lift,
            "estimated_purchase_frequency_lift_pct": freq_lift * 100,
            "annual_revenue_per_member": round(annual_revenue_per_member, 2),
            "annual_reward_cost_per_member": round(annual_cost_per_member, 2),
            "net_benefit_per_member": round(net_benefit, 2),
            "break_even_orders": round(annual_cost_per_member / max(aov * 0.1, 1), 1),
        }

    @staticmethod
    def _name_program(brand: str, tiers: int) -> str:
        names = {2: "Circle", 3: "Rewards", 4: "Club", 5: "Elite"}
        suffix = names.get(tiers, "Rewards")
        return f"{brand} {suffix} Program"
