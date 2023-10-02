purchase_amount = float(input("Enter the purchase amount in UAH: "))

if purchase_amount > 1000:
    discount = 0.05  # 5% discount
elif purchase_amount > 500:
    discount = 0.03  # 3% discount
else:
    discount = 0  # No discount

discount_amount = purchase_amount * discount
cost_after_discount = purchase_amount - discount_amount

print(f"Purchase amount: {purchase_amount} UAH")
print(f"Discount: {discount * 100}%")
print(f"Discount amount: {discount_amount} UAH")
print(f"Cost after discount: {cost_after_discount} UAH")








