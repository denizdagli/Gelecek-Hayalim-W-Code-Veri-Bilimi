""" Kullanıcıdan maaş bilgisini istenir ve bu bilgiye göre maaşından ne kadar vergi kesileceğini hesaplanır. Kullanıcının geliri;


 10000 ve altındaysa maaşından %5 kesinti olur. 
 25000 ve altındaysa maaşından %10 kesinti olur. 
 45000 ve altındaysa maaşından %25 kesinti olur. 
 Diğer koşullarda %30 kesinti olur. 

Bu durumlara göre kullanıcının yeni maaşı yazdırılır.
"""
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

