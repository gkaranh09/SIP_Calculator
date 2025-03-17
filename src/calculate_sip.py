def calculate_sip(monthly_investment, years, annual_rate):
    months = years * 12
    r = annual_rate / (12 * 100)  # Convert annual rate to monthly decimal
    if r == 0:
        return round(monthly_investment * months, 2)  # No interest case
    future_value = monthly_investment * ((1 + r) ** months - 1) / r * (1 + r)
    return round(future_value, 2)
