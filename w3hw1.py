
#1-Değişkenlere atanmış değerlerin veri tipleri arasında dönüşüm yapılır.
print("Ödev 1")
x=5
new_x=float(x)
y='5'
new_y=int(y)
z=5.0
new_z=str(z)

print(f"x'in veri tipi: { type(x)}" )
print(f"x kesirli sayıya dönüşür, tipi: {type(new_x)}")
print("-------------------------------------------------")
print(f"y'nin veri tipi: { type(y)}")
print(f"y tam sayıya dönüşür, tipi: {type(new_y)}")
print("-------------------------------------------------")
print(f"z'nin veri tipi: {type(z)}")
print(f"z metine dönüşür, tipi: {type(new_z)}")
print("-------------------------------------------------")

# İsimlerden oluşan üç değişkene yaş değerleri atanır.
#  Belirlenen üç değişken birbiriyle karşılaştırma operatörleri ile karşılaştırılır. 
# Bu karşılaştırmalara mantıksal operatörler de eklenir.

print("Ödev 2")

age_a=20
age_b=28
age_c=25

def find_max_age(age1,age2,age3):
    # Mantıksal operatörlerle karşılaştırma yapıyoruz
    if age1 > age2 and age1 > age3:
        return f"En büyük yaş: {age1} (age_a)"
    elif age2 > age1 and age2 > age3:
        return f"En büyük yaş: {age2} (age_b)"
    else:
        return f"En büyük yaş: {age3} (age_c)"
print(find_max_age(age_a,age_b,age_c)) 

print("-------------------------------------------------")

