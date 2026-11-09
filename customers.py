# ==========================================
# ISM2411 Lab 11 — Customer Dictionary & Lookup
# Name: Your Name Here
#
# Reflection Questions:
# 1. In Exercise 3 you saw the difference between .get() and bracket notation. When in real work 
#    would you use each one, and what's your rule of thumb for choosing?
#    - Use .get() when a missing key is expected or optional, allowing you to provide a safe fallback 
#      default without crashing your program. Use bracket notation when the key must exist for the program 
#      to operate correctly, so that a missing key immediately raises a KeyError and alerts you to data bugs.
# 2. Exercise 8 asked you to build a summary dictionary with a loop. What does this pattern remind 
#    you of from Excel, and why might the Python version be more useful for large datasets?
#    - This pattern reminds you of a Pivot Table or SUMIF/SUMIFS formula in Excel. The Python version is 
#      more useful for large datasets because it is faster, automates easily without formula corruption risks, 
#      scales seamlessly to millions of rows, and integrates directly into automated data processing pipelines.
# ==========================================

# EXERCISE 1 · Beginner: One customer
customer = {
    "name": "Alice Smith",
    "email": "alice@example.com",
    "tier": "gold",
    "ytd_spend": 1250.50
}

print("--- Exercise 1: Individual Fields ---")
print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])

print("\n--- Exercise 1: Full Dict ---")
print(customer)


# EXERCISE 2 · Beginner: Update and add
print("\n--- Exercise 2: Update and Add ---")
customer["phone"] = "555-0199"
print("After adding phone:", customer)

customer["tier"] = "platinum"
print("After updating tier to platinum:", customer)

del customer["email"]
print("After deleting email:", customer)


# EXERCISE 3 · Beginner: Safe lookup
print("\n--- Exercise 3: Safe Lookup ---")
# Safe lookup with .get() providing a default value
missing_email = customer.get("email", "no email on file")
print("Safe lookup (.get):", missing_email)

# Bracket notation lookup with try/except to catch KeyError
try:
    print(customer["email"])
except KeyError as e:
    print(f"KeyError caught successfully: Missing key {e}")


# EXERCISE 4 · Beginner: Iterate
print("\n--- Exercise 4: Iterate ---")
print("Iterating with .items():")
for key, value in customer.items():
    print(f"{key}: {value}")

# Explanation of iterating without .items():
# If you loop directly over a dictionary (e.g., 'for key in customer:'), 
# Python only iterates through the keys, leaving out the values. 
# Using .items() allows you to access both simultaneously.


# EXERCISE 5 · Intermediate: Lookup table
print("\n--- Exercise 5: Lookup Table ---")
tier_discounts = {"bronze": 0, "silver": .05, "gold": .10, "platinum": .15}
current_tier = customer["tier"]
discount_rate = tier_discounts.get(current_tier, 0)

purchase_amount = 200.00
final_price = purchase_amount * (1 - discount_rate)

print(f"Tier: {current_tier} · Discount Rate: {discount_rate * 100}% · Final Price: ${final_price:.2f}")


# EXERCISE 6 · Intermediate: List of dicts
print("\n--- Exercise 6: List of Dicts ---")
customer1 = {"name": "Alice", "tier": "platinum"}
customer2 = {"name": "Bob", "tier": "silver"}
customer3 = {"name": "Charlie", "tier": "bronze"}

customers_list = [customer1, customer2, customer3]
purchase_target = 300.00

for c in customers_list:
    rate = tier_discounts.get(c["tier"], 0)
    discount_amount = purchase_target * rate
    print(f"{c['name']} · Tier: {c['tier']} · Discount Amount: ${discount_amount:.2f}")


# EXERCISE 7 · Intermediate: Nested catalog
print("\n--- Exercise 7: Nested Catalog ---")
catalog = {
    "Widget A": {"price": 9.99, "stock": 150},
    "Gadget C": {"price": 49.99, "stock": 8}
}

print("Catalog Stock Check:")
for product_name, info in catalog.items():
    if info["stock"] < 20:
        print(f"{product_name} · LOW STOCK (Stock: {info['stock']})")
    else:
        print(f"{product_name} · Stock OK (Stock: {info['stock']})")


# EXERCISE 8 · Advanced: Sales by region
print("\n--- Exercise 8: Sales by Region ---")
transactions = [
    {"region": "South", "amount": 300},
    {"region": "North", "amount": 150},
    {"region": "South", "amount": 200}
]

sales_summary = {}
for tx in transactions:
    reg = tx["region"]
    amt = tx["amount"]
    sales_summary[reg] = sales_summary.get(reg, 0) + amt

print("Final Sales Summary (Sorted):")
for reg in sorted(sales_summary.keys()):
    print(f"{reg}: {sales_summary[reg]}")
