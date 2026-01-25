#!/usr/bin/env python3.10
"""
Defines the actors in the simulation: General Contractors, Prefab Units, and Tenants.
"""
from dataclasses import dataclass
from enum import Enum
from typing import List
import random

class MarketType(Enum):
    """The three market segments for prefab housing."""
    STUDENT = "student"
    MULTIGEN = "multigen"
    RURAL = "rural"

class RiskType(Enum):
    """Types of risks that can occur during installation."""
    CONSTRUCTION_DEFECT = "construction_defect"
    UTILITY_FAILURE = "utility_failure"
    SCHEDULE_DELAY = "schedule_delay"
    NONE = "none"

@dataclass
class GeneralContractor:
    """
    Represents one of the 12 General Contractors installing prefab homes.
    """
    id: int
    name: str
    skill_level: float  # 0.0 to 1.0, affects risk probability
    specialization: MarketType
    current_jobs: int = 0
    max_concurrent_jobs: int = 3
    completed_jobs: int = 0
    
    def is_available(self) -> bool:
        """Check if GC can take on another job."""
        return self.current_jobs < self.max_concurrent_jobs
    
    def start_job(self):
        """Assign a new job to this GC."""
        if self.is_available():
            self.current_jobs += 1
            return True
        return False
    
    def complete_job(self):
        """Mark a job as completed."""
        if self.current_jobs > 0:
            self.current_jobs -= 1
            self.completed_jobs += 1
    
    def calculate_risk_probability(self, market: MarketType) -> float:
        """
        Calculate the probability of a risk event based on GC skill and market match.
        Returns a probability between 0.0 and 1.0.
        """
        base_risk = 0.15  # 15% base risk
        
        # Skill reduces risk
        skill_modifier = (1.0 - self.skill_level) * 0.1
        
        # Specialization match reduces risk
        specialization_modifier = 0.0 if self.specialization == market else 0.05
        
        return min(0.3, base_risk + skill_modifier + specialization_modifier)

@dataclass
class PrefabUnit:
    """
    Represents a prefab housing unit to be installed.
    """
    id: int
    market_type: MarketType
    asset_value: float
    installation_time_days: int
    assigned_gc: GeneralContractor = None
    installation_complete: bool = False
    risk_events: List[RiskType] = None
    
    def __post_init__(self):
        if self.risk_events is None:
            self.risk_events = []
    
    def assign_contractor(self, gc: GeneralContractor) -> bool:
        """Assign a GC to this unit."""
        if gc.start_job():
            self.assigned_gc = gc
            return True
        return False
    
    def simulate_installation(self) -> RiskType:
        """
        Simulate the installation process and determine if a risk event occurs.
        Returns the type of risk event (or NONE).
        """
        if not self.assigned_gc:
            return RiskType.SCHEDULE_DELAY
        
        risk_prob = self.assigned_gc.calculate_risk_probability(self.market_type)
        
        if random.random() < risk_prob:
            # Determine which type of risk occurred
            risk_weights = {
                RiskType.CONSTRUCTION_DEFECT: 0.4,
                RiskType.UTILITY_FAILURE: 0.4,
                RiskType.SCHEDULE_DELAY: 0.2
            }
            risk_event = random.choices(
                list(risk_weights.keys()),
                weights=list(risk_weights.values())
            )[0]
            self.risk_events.append(risk_event)
            return risk_event
        
        return RiskType.NONE
    
    def complete_installation(self):
        """Mark installation as complete and free up the GC."""
        self.installation_complete = True
        if self.assigned_gc:
            self.assigned_gc.complete_job()

@dataclass
class Tenant:
    """
    Represents a tenant in the multi-generational housing model.
    """
    id: int
    monthly_income: float
    payment_reliability: float  # 0.0 to 1.0
    months_in_residence: int = 0
    missed_payments: int = 0
    
    def will_pay_this_month(self) -> bool:
        """Determine if tenant will make payment this month."""
        return random.random() < self.payment_reliability
    
    def make_payment(self) -> bool:
        """Process monthly payment."""
        self.months_in_residence += 1
        if self.will_pay_this_month():
            return True
        else:
            self.missed_payments += 1
            return False

def create_gc_roster() -> List[GeneralContractor]:
    """
    Create the roster of 12 General Contractors with varied skills and specializations.
    """
    gcs = []
    specializations = [
        MarketType.STUDENT, MarketType.STUDENT, MarketType.STUDENT, MarketType.STUDENT,
        MarketType.MULTIGEN, MarketType.MULTIGEN, MarketType.MULTIGEN, MarketType.MULTIGEN,
        MarketType.RURAL, MarketType.RURAL, MarketType.RURAL, MarketType.RURAL
    ]
    
    for i in range(12):
        gc = GeneralContractor(
            id=i + 1,
            name=f"GC-{i+1:02d}",
            skill_level=random.uniform(0.6, 0.95),
            specialization=specializations[i],
            max_concurrent_jobs=random.randint(2, 4)
        )
        gcs.append(gc)
    
    return gcs

if __name__ == "__main__":
    # Test the GC roster creation
    roster = create_gc_roster()
    print(f"Created {len(roster)} General Contractors:")
    for gc in roster:
        print(f"  {gc.name}: Skill={gc.skill_level:.2f}, Specialization={gc.specialization.value}")
