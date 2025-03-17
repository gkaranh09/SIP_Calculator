def calculate_sip(monthly_investment, months, annual_rate):
    r = annual_rate / 100 / 12  # Convert annual rate to monthly
    future_value = monthly_investment * (((1 + r) ** months - 1) / r) * (1 + r)
    return round(future_value, 2)
