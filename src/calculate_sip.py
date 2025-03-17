# src/calculate_sip.py

def calculate_sip(monthly_investment, months, annual_rate):
    """
    Calculate the future value of a Systematic Investment Plan (SIP).

    Args:
        monthly_investment (float): The fixed amount invested every month.
        months (int): The total number of months.
        annual_rate (float): The annual interest rate (percentage).

    Returns:
        float: The future value of the SIP investment.
    """
    r = annual_rate / (12 * 100)  # Convert annual rate to monthly decimal
    future_value = monthly_investment * ((1 + r) ** months - 1) / r * (1 + r)
    return round(future_value, 2)
