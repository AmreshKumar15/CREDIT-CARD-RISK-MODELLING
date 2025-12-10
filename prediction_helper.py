"""
Credit Risk Modelling - Prediction Helper Module
Simplified version for Streamlit deployment
"""

import pandas as pd
import numpy as np


def predict(age, income, loan_amount, loan_tenure_months,
            avg_dpd_per_delinquency, delinquency_ratio,
            credit_utilization_ratio, num_open_accounts,
            residence_type, loan_purpose, loan_type):
    """
    Calculate credit risk based on input parameters.

    Args:
        age: Customer age (18-100)
        income: Annual income (₹)
        loan_amount: Loan amount (₹)
        loan_tenure_months: Loan tenure in months
        avg_dpd_per_delinquency: Average DPD per delinquency
        delinquency_ratio: Delinquency ratio (%)
        credit_utilization_ratio: Credit utilization ratio (%)
        num_open_accounts: Number of open accounts
        residence_type: Type of residence (Owned/Rented/Mortgage)
        loan_purpose: Purpose of loan (Education/Home/Auto/Personal)
        loan_type: Type of loan (Secured/Unsecured)

    Returns:
        Tuple of (default_probability, credit_score, rating)
    """

    # Calculate loan to income ratio
    loan_to_income = loan_amount / income if income > 0 else 0

    # Risk scoring algorithm
    risk_factors = 0

    # Age factor (optimal: 25-60)
    if age < 25 or age > 60:
        risk_factors += 1.0

    # Income factor (optimal: > 300,000)
    if income < 300000:
        risk_factors += 1.0

    # Loan to income factor (optimal: < 2.5)
    if loan_to_income > 3.5:
        risk_factors += 1.5
    elif loan_to_income > 2.5:
        risk_factors += 0.75

    # Loan tenure factor
    if loan_tenure_months > 60:
        risk_factors += 0.5

    # Delinquency factor (optimal: < 10%)
    if delinquency_ratio > 25:
        risk_factors += 2.0
    elif delinquency_ratio > 15:
        risk_factors += 1.0

    # Credit utilization factor (optimal: < 50%)
    if credit_utilization_ratio > 80:
        risk_factors += 1.5
    elif credit_utilization_ratio > 60:
        risk_factors += 1.0

    # DPD factor (optimal: < 5)
    if avg_dpd_per_delinquency > 30:
        risk_factors += 1.5
    elif avg_dpd_per_delinquency > 15:
        risk_factors += 1.0

    # Number of accounts factor
    if num_open_accounts > 4:
        risk_factors += 1.0
    elif num_open_accounts > 3:
        risk_factors += 0.5

    # Residence type factor
    if residence_type == "Rented":
        risk_factors += 0.75

    # Loan purpose factor
    if loan_purpose in ["Auto"]:
        risk_factors -= 0.5  # Lower risk for auto loans
    elif loan_purpose in ["Personal"]:
        risk_factors += 0.25  # Slightly higher risk

    # Loan type factor
    if loan_type == "Unsecured":
        risk_factors += 0.5

    # Calculate normalized probability (0-1 range)
    default_probability = min(max(risk_factors / 10.0, 0.01), 0.99)

    # Calculate credit score (300-850 scale)
    credit_score = int(300 + (1 - default_probability) * 550)

    # Determine risk rating
    if default_probability < 0.15:
        rating = "🟢 LOW RISK"
    elif default_probability < 0.35:
        rating = "🟡 MEDIUM RISK"
    else:
        rating = "🔴 HIGH RISK"

    return default_probability, credit_score, rating
