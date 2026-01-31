# Policy Slips Updated - Prefab Housing Focus

**Date**: 2026-01-31  
**Status**: ✅ Complete

## Problem Identified

The original `simulatedPolicies.json` contained policies for:
- Quantum cryptographic systems
- Autonomous freight networks
- Grid energy infrastructure
- Digital asset custody
- Regulatory consulting

**These had nothing to do with the actual website focus**: Prefab housing installation contractors serving three market segments.

## Solution Implemented

Created 5 new policies aligned with the actual business model:

### Policy 1: IMCI-STU-2026-001
**Phoenix Student Housing Builders LLC**
- **Market**: Student Housing (ASU campuses)
- **Annual Volume**: 70 units
- **Premium**: $45,000
- **Key Risks**: Tight occupancy deadlines, foundation challenges, utility integration
- **Claims History**: 4 claims, $87,500 incurred

### Policy 2: IMCI-MUL-2026-002
**Generations United Construction Inc**
- **Market**: Multi-Generational (Rent-to-Equity ADUs)
- **Annual Volume**: 45 units
- **Premium**: $35,000
- **Key Risks**: Accessibility features, dual-utility metering, financial instrument deadlines
- **Claims History**: 2 claims, $52,000 incurred

### Policy 3: IMCI-RUR-2026-003
**Desert Frontier Builders LLC**
- **Market**: Rural Development (Off-Grid)
- **Annual Volume**: 35 units
- **Premium**: $57,500
- **Key Risks**: Septic systems, well water, solar power, foundation on unstable soil
- **Claims History**: 5 claims, $142,000 incurred

### Policy 4: IMCI-STU-2026-004
**Wildcat Housing Solutions Inc**
- **Market**: Student Housing (University of Arizona)
- **Annual Volume**: 62 units
- **Premium**: $50,000
- **Key Risks**: HVAC in extreme heat, monsoon flooding, UV degradation
- **Claims History**: 6 claims, $118,000 incurred

### Policy 5: IMCI-MUL-2026-005
**Heritage Home Builders LLC**
- **Market**: Multi-Generational (Casita-Style ADUs)
- **Annual Volume**: 40 units
- **Premium**: $35,000
- **Key Risks**: HOA compliance, architectural integration, shared utilities
- **Claims History**: 3 claims, $68,000 incurred

## Risk Alignment with Website Content

All policies now reflect the three risk categories from the website:

### Construction Defects (40% of claims)
- Structural integrity issues
- Material defects
- Installation errors
- Code compliance failures
- Foundation problems
- Accessibility feature failures

### Utility Integration (40% of claims)
- Water connection failures
- Electrical system issues
- Gas line problems
- Septic system failures
- Solar power systems
- Dual-meter installations

### Schedule Delays (20% of claims)
- GC availability constraints
- Supply chain disruptions
- Weather delays
- Permit processing
- HOA approval processes

## Summary Statistics

- **Total Policies**: 5 (representing 5 of the 12 GCs in the captive)
- **Total Premium Income**: $222,500
- **Total Units Installed Annually**: 252
- **Market Distribution**: 
  - Student Housing: 2 policies
  - Multi-Generational: 2 policies
  - Rural Development: 1 policy
- **Total Claims (3 years)**: 20 claims
- **Total Incurred (3 years)**: $467,500
- **Loss Ratio**: 70% (aligns with actuarial assumptions)

## Lloyd's MRC Format Features

Each policy slip includes:

### ACORD 25 Header
- Producer information (Integral Mass Captive)
- Insured entity details
- Underwriter information
- Certificate holder (Arizona DOI)

### Lloyd's MRC Body
1. **Risk Details**: Classification, limits, deductibles, premiums, covered perils
2. **Risk Narrative**: Business operations, risk factors, loss control measures
3. **Claims History**: Prior 3-year claims with detailed descriptions
4. **Reinsurance Structure**: Retention levels and reinsurer information
5. **Special Conditions**: Tail coverage, sublimits, specific warranties

## File Location

**Single Source of Truth**: `captive.integralmass.com/docs/data/simulatedPolicies.json`

This is the ONLY copy. Edit this file to update policy data.

## Verification

✅ JSON syntax valid  
✅ Server loading file successfully (HTTP 200)  
✅ All 5 policies display on policy-slips.html  
✅ Risk narratives written in formal Lloyd's style  
✅ Claims history reflects realistic prefab housing risks  
✅ Premiums align with $50K base rate from policies.html  
✅ Market segments match website content (Student, Multi-Gen, Rural)  

## Next Steps

The policy slips page is now fully functional and aligned with the website's actual business model. Users can:

1. View all 5 policy cards on http://localhost:8080/policy-slips.html
2. Click "View Slip" to see detailed Lloyd's MRC format documentation
3. Review risk narratives specific to prefab housing installation
4. See realistic claims history for construction defects, utility integration, and schedule delays

The policies now accurately represent the captive insurance model for the 12 General Contractors installing prefab housing across three market segments in Arizona.
