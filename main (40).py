# Get input data
sale_price = float(input("Enter the sale price of the home: "))
commission_rate = float(input("Enter the commission rate for the real estate agent (as a decimal): "))
closing_costs = float(input("Enter the estimated closing costs: "))
repair_costs = float(input("Enter the estimated repair and improvement costs: "))

# Calculate real estate agent commission
agent_commission = sale_price * commission_rate

# Calculate net proceeds
net_proceeds = sale_price - agent_commission - closing_costs - repair_costs

# Output results
print(f"\nReal estate agent commission: ${agent_commission:,.2f}")
print(f"Closing costs: ${closing_costs:,.2f}")
print(f"Repair and improvement costs: ${repair_costs:,.2f}")
print(f"\nNet proceeds from sale: ${net_proceeds:,.2f}")
