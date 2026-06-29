# SIP Calculator

monthly_investment = 0
annual_rate = 0
time = 0

# Monthly Investment Input
while True:
    monthly_investment = float(input("Enter monthly SIP amount: "))

    if monthly_investment <= 0:
        print("Amount must be greater than 0.")
    else:
        break

# Interest Rate Input
while True:
    annual_rate = float(input("Enter annual interest rate (%): "))

    if annual_rate < 0:
        print("Rate cannot be negative.")
    else:
        break

# Time Input
while True:
    time = int(input("Enter investment time in years: "))

    if time <= 0:
        print("Time must be greater than 0.")
    else:
        break

# SIP Calculation
monthly_rate = annual_rate / 12 / 100
months = time * 12

future_value = 0
month = 1

# While loop for monthly investment growth
while month <= months:

    future_value = (future_value + monthly_investment) * (1 + monthly_rate)

    month += 1

total_invested = monthly_investment * months
returns = future_value - total_invested

# Output
print("\n===== SIP RESULT =====")
print(f"Total Invested: ${total_invested:,.2f}")
print(f"Estimated Returns: ${returns:,.2f}")
print(f"Final Amount: ${future_value:,.2f}")