total_bill = float(input("Total bill amount: "))
amount_paid = float(input("Amount paid: "))
due_amount = total_bill - amount_paid

if due_amount > 0:
    print(f"Due amount: ${due_amount:.2f}")
elif due_amount < 0:
    print(f"Overpaid by: ${-due_amount:.2f}")
else:
    print("Fully paid.")


