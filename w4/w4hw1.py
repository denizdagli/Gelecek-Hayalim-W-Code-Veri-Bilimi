salary= int(input("Enter the salary amount: "))
def calculate_tax(salary):
    
    if salary< 10000:
        tax_rate=0.05
    elif salary< 25000:
        tax_rate=0.1
    elif salary< 45000:
        tax_rate=0.25
    else:
        tax_rate=0.3
    

    tax_amount=salary*tax_rate
    net_salary=salary-tax_amount
    return net_salary

print(f"Net salary: {calculate_tax(salary)}")

