#!/usr/bin/env python3.10
"""
Monte Carlo simulation for actuarial risk modeling.
Simulates thousands of years of operation to test solvency.
"""
import numpy as np
import pandas as pd
from typing import Dict, List
from datetime import datetime
import random

class CaptiveInsuranceModel:
    """
    Monte Carlo simulation for the Integral Mass Captive Insurance Company.
    """
    
    def __init__(self, 
                 initial_capital: float = 1_000_000,
                 num_gcs: int = 12,
                 premium_per_gc_annual: float = 50_000):
        """
        Initialize the captive insurance model.
        
        :param initial_capital: Starting capital for the captive
        :param num_gcs: Number of General Contractors insured
        :param premium_per_gc_annual: Annual premium per GC
        """
        self.initial_capital = initial_capital
        self.num_gcs = num_gcs
        self.premium_per_gc_annual = premium_per_gc_annual
        self.annual_premium_income = num_gcs * premium_per_gc_annual
        
        # Risk parameters (calibrated from queue simulation)
        self.claim_probability = 0.15  # 15% chance of claim per GC per year
        self.claim_severity_mean = 25_000
        self.claim_severity_std = 10_000
        
        # Investment return on reserves
        self.investment_return_rate = 0.04  # 4% annual return
        
    def simulate_year(self, current_capital: float) -> Dict:
        """
        Simulate one year of operations.
        
        :param current_capital: Capital at start of year
        :return: Dictionary with year results
        """
        # Premium income
        premium_income = self.annual_premium_income
        
        # Investment income on reserves
        investment_income = current_capital * self.investment_return_rate
        
        # Simulate claims for each GC
        total_claims = 0
        num_claims = 0
        
        for _ in range(self.num_gcs):
            if random.random() < self.claim_probability:
                # Claim occurred - sample severity from lognormal distribution
                claim_amount = max(0, np.random.normal(
                    self.claim_severity_mean, 
                    self.claim_severity_std
                ))
                total_claims += claim_amount
                num_claims += 1
        
        # Operating expenses (10% of premium)
        operating_expenses = premium_income * 0.10
        
        # Calculate end of year capital
        net_income = premium_income + investment_income - total_claims - operating_expenses
        ending_capital = current_capital + net_income
        
        # Calculate solvency ratio (capital / expected annual claims)
        expected_annual_claims = self.num_gcs * self.claim_probability * self.claim_severity_mean
        solvency_ratio = ending_capital / expected_annual_claims if expected_annual_claims > 0 else 0
        
        return {
            'premium_income': premium_income,
            'investment_income': investment_income,
            'total_claims': total_claims,
            'num_claims': num_claims,
            'operating_expenses': operating_expenses,
            'net_income': net_income,
            'ending_capital': ending_capital,
            'solvency_ratio': solvency_ratio,
            'is_solvent': ending_capital > 0
        }
    
    def run_monte_carlo(self, num_simulations: int = 10_000, years: int = 10) -> pd.DataFrame:
        """
        Run Monte Carlo simulation across multiple scenarios.
        
        :param num_simulations: Number of simulation runs
        :param years: Number of years to simulate per run
        :return: DataFrame with simulation results
        """
        results = []
        
        for sim in range(num_simulations):
            capital = self.initial_capital
            sim_solvent = True
            
            for year in range(years):
                year_result = self.simulate_year(capital)
                capital = year_result['ending_capital']
                
                if capital <= 0:
                    sim_solvent = False
                
                results.append({
                    'simulation': sim,
                    'year': year,
                    **year_result
                })
            
            # Record final outcome
            if sim % 1000 == 0:
                print(f"Completed simulation {sim}/{num_simulations}")
        
        return pd.DataFrame(results)
    
    def calculate_ruin_probability(self, results_df: pd.DataFrame) -> float:
        """
        Calculate the probability of ruin (insolvency) from simulation results.
        
        :param results_df: DataFrame from run_monte_carlo
        :return: Probability of ruin
        """
        # Get final year for each simulation
        final_years = results_df.groupby('simulation').last()
        
        # Count how many ended insolvent
        insolvent_count = (final_years['ending_capital'] <= 0).sum()
        total_sims = len(final_years)
        
        return insolvent_count / total_sims
    
    def calculate_required_capital(self, 
                                   target_ruin_prob: float = 0.01,
                                   years: int = 10,
                                   num_simulations: int = 1000) -> float:
        """
        Calculate the required initial capital to achieve target ruin probability.
        
        :param target_ruin_prob: Target probability of ruin (e.g., 0.01 = 1%)
        :param years: Planning horizon
        :param num_simulations: Number of simulations per test
        :return: Required initial capital
        """
        # Binary search for required capital
        low_capital = 100_000
        high_capital = 5_000_000
        tolerance = 0.005  # 0.5% tolerance on ruin probability
        
        while high_capital - low_capital > 10_000:
            test_capital = (low_capital + high_capital) / 2
            
            # Test this capital level
            self.initial_capital = test_capital
            results = self.run_monte_carlo(num_simulations, years)
            ruin_prob = self.calculate_ruin_probability(results)
            
            print(f"Testing capital ${test_capital:,.0f}: Ruin prob = {ruin_prob:.4f}")
            
            if ruin_prob > target_ruin_prob + tolerance:
                # Need more capital
                low_capital = test_capital
            elif ruin_prob < target_ruin_prob - tolerance:
                # Can use less capital
                high_capital = test_capital
            else:
                # Within tolerance
                return test_capital
        
        return high_capital

def generate_summary_statistics(results_df: pd.DataFrame) -> Dict:
    """
    Generate summary statistics from Monte Carlo results.
    
    :param results_df: DataFrame from run_monte_carlo
    :return: Dictionary of summary statistics
    """
    final_years = results_df.groupby('simulation').last()
    
    stats = {
        'mean_final_capital': final_years['ending_capital'].mean(),
        'median_final_capital': final_years['ending_capital'].median(),
        'std_final_capital': final_years['ending_capital'].std(),
        'min_final_capital': final_years['ending_capital'].min(),
        'max_final_capital': final_years['ending_capital'].max(),
        'probability_of_ruin': (final_years['ending_capital'] <= 0).mean(),
        'mean_solvency_ratio': final_years['solvency_ratio'].mean(),
        'percentile_5_capital': final_years['ending_capital'].quantile(0.05),
        'percentile_95_capital': final_years['ending_capital'].quantile(0.95)
    }
    
    return stats

if __name__ == "__main__":
    print("Running Monte Carlo Risk Simulation...")
    print("=" * 60)
    
    # Initialize model
    model = CaptiveInsuranceModel(
        initial_capital=1_000_000,
        num_gcs=12,
        premium_per_gc_annual=50_000
    )
    
    # Run simulation
    print("\nRunning 1,000 simulations over 10 years...")
    results = model.run_monte_carlo(num_simulations=1_000, years=10)
    
    # Calculate statistics
    stats = generate_summary_statistics(results)
    
    print("\n" + "=" * 60)
    print("SIMULATION RESULTS")
    print("=" * 60)
    print(f"Mean Final Capital: ${stats['mean_final_capital']:,.2f}")
    print(f"Median Final Capital: ${stats['median_final_capital']:,.2f}")
    print(f"5th Percentile: ${stats['percentile_5_capital']:,.2f}")
    print(f"95th Percentile: ${stats['percentile_95_capital']:,.2f}")
    print(f"Probability of Ruin: {stats['probability_of_ruin']:.2%}")
    print(f"Mean Solvency Ratio: {stats['mean_solvency_ratio']:.2f}")
    print("=" * 60)
