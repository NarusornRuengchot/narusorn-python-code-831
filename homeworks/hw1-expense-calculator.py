"""
Personal Finance Calculator
Student: Narusorn Ruengchot 6730202246 831
Date: 26/7/2568
Purpose: Calculate monthly budget and savings
"""
monthly_income = float(input("User's monthly income in THB : "))
rent_cost = float(input("Monthly rent/housing cost : "))
food_budget = int(input("Monthly food budget in THB : "))
transportation_cost = float(input("Monthly transportation expenses : "))
entertainment_budget = int(input("Monthly entertainment budget : "))
emergency_fund_percent = float(input("Percentage to save for emergency (e.g., 10.5) : "))
investment_percent = float(input("Percentage to invest (e.g., 15.0) : "))

total_fixed_expenses = rent_cost + transportation_cost
total_variable_expenses = food_budget + entertainment_budget
total_expenses = total_fixed_expenses + total_variable_expenses
remaining_income = monthly_income - total_expenses
emergency_fund_amount = monthly_income * (emergency_fund_percent / 100)
investment_amount = monthly_income * (investment_percent / 100)
available_for_savings = remaining_income - emergency_fund_amount - investment_percent
expense_ratio = (total_expenses / monthly_income) * 100

print("\n=== MONTHLY BUDGET REPORT ===")
print(f"Income : {monthly_income} THB")
print(f"Fixed Expenses : {total_fixed_expenses} THB")
print(f"Variable Expenses : {total_variable_expenses} THB")
print(f"Total Expenses : {total_expenses} THB")
print(f"Remaining : {remaining_income} THB")

print("\n=== SAVINGS BREAKDOWN ===")
print(f"Emergency Fund (10%) : {emergency_fund_amount} THB")
print(f"Investment (15%) : {investment_amount} THB")
print(f"Available for Savings : {available_for_savings} THB")

print("\n=== ANALYSIS ===")
print(f"Expense Ratio : {expense_ratio} THB")