principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the interest rate (%): "))
time = float(input("Enter the time period (in years): "))

interest = (principal * rate * time) / 100
total_amount = principal + interest

print("Simple Interest:", interest)
print("Total Amount:", total_amount)