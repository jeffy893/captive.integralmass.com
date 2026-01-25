#!/usr/bin/env python3.10
"""
Queuing simulation for General Contractor resource allocation.
Uses SimPy to model the installation process across three markets.
"""
import simpy
import random
from typing import List, Dict
from actors import GeneralContractor, PrefabUnit, MarketType, RiskType, create_gc_roster

class InstallationQueue:
    """
    Manages the queuing system for prefab installations.
    """
    
    def __init__(self, env: simpy.Environment, gc_roster: List[GeneralContractor]):
        self.env = env
        self.gc_roster = gc_roster
        self.gc_resources = {gc.id: simpy.Resource(env, capacity=gc.max_concurrent_jobs) 
                            for gc in gc_roster}
        
        # Statistics tracking
        self.completed_units = []
        self.waiting_times = []
        self.risk_events = []
        self.queue_lengths = {market: [] for market in MarketType}
        
    def find_best_gc(self, market_type: MarketType) -> GeneralContractor:
        """
        Find the best available GC for a given market type.
        Prioritizes specialization match and availability.
        """
        # First, try to find a specialist who is available
        specialists = [gc for gc in self.gc_roster 
                      if gc.specialization == market_type and gc.is_available()]
        if specialists:
            return max(specialists, key=lambda gc: gc.skill_level)
        
        # Otherwise, find any available GC
        available = [gc for gc in self.gc_roster if gc.is_available()]
        if available:
            return max(available, key=lambda gc: gc.skill_level)
        
        # If none available, return the one with fewest jobs
        return min(self.gc_roster, key=lambda gc: gc.current_jobs)
    
    def installation_process(self, unit: PrefabUnit):
        """
        Simulates the installation process for a single prefab unit.
        """
        arrival_time = self.env.now
        
        # Find and assign a GC
        gc = self.find_best_gc(unit.market_type)
        
        # Wait for GC to be available
        with self.gc_resources[gc.id].request() as request:
            yield request
            
            wait_time = self.env.now - arrival_time
            self.waiting_times.append(wait_time)
            
            # Assign the contractor
            unit.assign_contractor(gc)
            
            # Simulate installation time
            yield self.env.timeout(unit.installation_time_days)
            
            # Check for risk events
            risk_event = unit.simulate_installation()
            if risk_event != RiskType.NONE:
                self.risk_events.append({
                    'time': self.env.now,
                    'unit_id': unit.id,
                    'market': unit.market_type,
                    'risk_type': risk_event,
                    'gc_id': gc.id
                })
                
                # Risk events add delay
                if risk_event == RiskType.CONSTRUCTION_DEFECT:
                    yield self.env.timeout(random.randint(5, 15))
                elif risk_event == RiskType.UTILITY_FAILURE:
                    yield self.env.timeout(random.randint(3, 10))
                elif risk_event == RiskType.SCHEDULE_DELAY:
                    yield self.env.timeout(random.randint(7, 20))
            
            # Complete installation
            unit.complete_installation()
            self.completed_units.append({
                'unit_id': unit.id,
                'market': unit.market_type,
                'completion_time': self.env.now,
                'wait_time': wait_time,
                'gc_id': gc.id,
                'had_risk_event': risk_event != RiskType.NONE
            })

def generate_unit_arrivals(env: simpy.Environment, 
                          queue: InstallationQueue,
                          market_type: MarketType,
                          arrival_rate: float,
                          total_units: int):
    """
    Generates arrivals of prefab units for a specific market.
    
    :param arrival_rate: Average days between arrivals
    :param total_units: Total number of units to generate
    """
    unit_id = 0
    for _ in range(total_units):
        # Wait for next arrival
        yield env.timeout(random.expovariate(1.0 / arrival_rate))
        
        # Create new unit
        unit = PrefabUnit(
            id=f"{market_type.value}_{unit_id}",
            market_type=market_type,
            asset_value=get_market_asset_value(market_type),
            installation_time_days=get_market_installation_time(market_type)
        )
        unit_id += 1
        
        # Start installation process
        env.process(queue.installation_process(unit))

def get_market_asset_value(market: MarketType) -> float:
    """Return typical asset value for each market type."""
    values = {
        MarketType.STUDENT: 120000,
        MarketType.MULTIGEN: 150000,
        MarketType.RURAL: 135000
    }
    return values[market] * random.uniform(0.9, 1.1)

def get_market_installation_time(market: MarketType) -> int:
    """Return typical installation time in days for each market type."""
    times = {
        MarketType.STUDENT: 30,
        MarketType.MULTIGEN: 45,
        MarketType.RURAL: 60
    }
    return times[market] + random.randint(-5, 10)

def run_simulation(simulation_days: int = 365, 
                   units_per_market: int = 50) -> Dict:
    """
    Run the complete queuing simulation.
    
    :param simulation_days: Total days to simulate
    :param units_per_market: Number of units to install per market
    :return: Dictionary of simulation results
    """
    # Setup
    env = simpy.Environment()
    gc_roster = create_gc_roster()
    queue = InstallationQueue(env, gc_roster)
    
    # Start arrival processes for each market
    arrival_rates = {
        MarketType.STUDENT: 5,    # New unit every 5 days on average
        MarketType.MULTIGEN: 7,   # New unit every 7 days
        MarketType.RURAL: 10      # New unit every 10 days
    }
    
    for market, rate in arrival_rates.items():
        env.process(generate_unit_arrivals(env, queue, market, rate, units_per_market))
    
    # Run simulation
    env.run(until=simulation_days)
    
    # Compile results
    results = {
        'completed_units': queue.completed_units,
        'risk_events': queue.risk_events,
        'waiting_times': queue.waiting_times,
        'gc_utilization': {gc.id: gc.completed_jobs for gc in gc_roster},
        'total_units_completed': len(queue.completed_units),
        'total_risk_events': len(queue.risk_events),
        'avg_wait_time': sum(queue.waiting_times) / len(queue.waiting_times) if queue.waiting_times else 0
    }
    
    return results

if __name__ == "__main__":
    print("Running Installation Queue Simulation...")
    print("=" * 60)
    
    results = run_simulation(simulation_days=365, units_per_market=30)
    
    print(f"\nSimulation Results:")
    print(f"  Total Units Completed: {results['total_units_completed']}")
    print(f"  Total Risk Events: {results['total_risk_events']}")
    print(f"  Average Wait Time: {results['avg_wait_time']:.2f} days")
    print(f"  Risk Event Rate: {results['total_risk_events']/results['total_units_completed']*100:.1f}%")
    
    print(f"\nGC Utilization:")
    for gc_id, jobs in results['gc_utilization'].items():
        print(f"  GC-{gc_id:02d}: {jobs} jobs completed")
