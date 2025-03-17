def calculate_sip(monthly_investment, rate_of_return, years):
    """Calculate SIP returns"""
    months = years * 12
    monthly_rate = (rate_of_return / 100) / 12
    future_value = 0

    for _ in range(months):
        future_value = (future_value + monthly_investment) * (1 + monthly_rate)

    return round(future_value, 2)
