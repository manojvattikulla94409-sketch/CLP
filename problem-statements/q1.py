def calculate_total_bill(amount: float, tip_percent: int) -> float:

    # Converting inputs into float for precision
    amount = float(amount)
    tip_percent = float(tip_percent)
    
    # Calculating total
    total = amount + (amount * tip_percent / 100)
    
    # Returning rounded value to exactly 2 decimal places
    return round(total, 2)

