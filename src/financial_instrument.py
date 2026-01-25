#!/usr/bin/env python3.10
import pandas as pd
from dataclasses import dataclass, field
from datetime import datetime, timedelta

@dataclass
class AccessibilityFeatures:
    """Defines the prefab specs that enable the residence swap later."""
    wheelchair_accessible: bool = True
    wide_doorways: bool = True
    smart_monitoring: bool = False

class MultigenEquityInstrument:
    """
    A financial model representing a Rent-to-Equity agreement between
    Parent (Investor) and Child (Tenant/Future Owner).
    
    This instrument is the asset backing the insurance policy.
    """

    def __init__(self, 
                 total_asset_value: float, 
                 monthly_payment: float, 
                 interest_rate_apy: float, 
                 start_date: datetime):
        
        # Financial Configuration
        self.asset_value = total_asset_value  # Cost of the Prefab Unit
        self.monthly_payment = monthly_payment
        self.monthly_rate = (1 + interest_rate_apy) ** (1/12) - 1
        self.start_date = start_date
        
        # State Tracking
        self.current_balance = 0.0
        self.vested_equity_percent = 0.0
        self.months_elapsed = 0
        self.is_fully_vested = False
        self.residence_swapped = False # Has parent moved in?
        
        # The Ledger (for generating graphs later)
        self.history = []

        # Technical Specs (The physical asset)
        self.specs = AccessibilityFeatures()

    def process_month(self, risk_event_occurred: bool = False):
        """
        Simulates one month of time.
        
        :param risk_event_occurred: If True, child missed payment (Insurance Event).
        """
        current_date = self.start_date + timedelta(days=30 * self.months_elapsed)
        
        # 1. Apply Interest to existing balance
        interest_earned = self.current_balance * self.monthly_rate
        self.current_balance += interest_earned
        
        # 2. Add Payment (Unless a risk event occurred)
        contribution = 0.0
        if not risk_event_occurred:
            contribution = self.monthly_payment
            self.current_balance += contribution
        else:
            # This is where the Captive Insurance Logic triggers in the main loop
            # The Captive would step in to pay the 'contribution' to protect the asset
            pass 

        # 3. Calculate Vesting
        self.vested_equity_percent = min(1.0, self.current_balance / self.asset_value)
        
        if self.vested_equity_percent >= 1.0 and not self.is_fully_vested:
            self.is_fully_vested = True
            # In a real app, this might trigger a contract generation event

        # 4. Record State for Visualization
        self.history.append({
            "date": current_date,
            "month": self.months_elapsed,
            "balance": round(self.current_balance, 2),
            "vesting_percent": round(self.vested_equity_percent * 100, 2),
            "interest_earned": round(interest_earned, 2),
            "risk_event": risk_event_occurred
        })
        
        self.months_elapsed += 1

    def trigger_residence_swap(self):
        """
        Activates the clause where parents swap homes with the child
        due to aging/accessibility needs.
        """
        if self.specs.wheelchair_accessible:
            self.residence_swapped = True
            return "SWAP_SUCCESSFUL: Parent moved to ADU."
        else:
            return "SWAP_FAILED: Unit not accessible."

    def export_data(self):
        """Returns a Pandas DataFrame for easy plotting in the website generator."""
        return pd.DataFrame(self.history)

# --- QUICK TEST BLOCK (Runs if you execute this file directly) ---
if __name__ == "__main__":
    # Simulate a $150k Prefab ADU, $1,200/mo rent, 4.5% APY
    plan = MultigenEquityInstrument(150000, 1200, 0.045, datetime.now())
    
    # Simulate 10 years (120 months)
    for _ in range(120):
        plan.process_month()
        
    print(f"Final Balance: ${plan.current_balance:,.2f}")
    print(f"Equity Vested: {plan.vested_equity_percent*100:.2f}%")
