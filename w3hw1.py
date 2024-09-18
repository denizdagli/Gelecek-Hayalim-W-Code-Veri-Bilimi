
#Değişkenlere atanmış değerlerin veri tipleri arasında dönüşüm yapılır.
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

#Kullanıcıdan iki değer girmesini istenir. Girilen değerlerin toplama, çıkarma, çarpma, bölme sonuçlarını yazdırılır.
print("Ödev 3")

value1=int(input("Birinci sayıyı giriniz: "))
value2=int(input("İkinci sayıyı giriniz: "))
print(f"Toplama: {value1 + value2}")
print(f"Çıkarma: {value1 - value2}")
print(f"Çarpma: {value1 * value2}")
print(f"Bölme: {value1 / value2}")

print("-------------------------------------------------")
#Kullanıcıdan isim, yaş, şehir ve meslek bilgilerini istenir ve cevaplarını yazdırılır.

print("Ödev 4")
name=input("Adınızı giriniz: ")
age=int(input("Yaşınızı giriniz: "))
city=input("Şehir giriniz: ")
job=input("Meslek giriniz: ")

print(f"Adınız: {name}\nYaşınız: {age}\nŞehir: {city}\nMeslek: {job}")

print("-------------------------------------------------")
""""Gelecek Hayalim: W-Code Veri Bilimi Atölyesi" ifadesini bir değişkene tanımlanır.

İfadedeki her bir kelimeyi ("Gelecek Hayalim: W-Code", "Veri", "Bilimi", "Atölyesi") değişken içinden seçilir.

İfadeyi hepsini büyük harf olacak hale çevrilir. ("GELECEK HAYALİM: W-CODE VERİ BİLİMİ ATÖLYESİ")

İfadeyi hepsini büyük harf olacak hale çevrilir.("gelecek hayalim: w-code veri bilimi atölyesi")

"0123456789" ifadesindeki yalnızca çift sayıları ve yalnızca tek sayıları seçilir. ("02468", "13579")
"""
print("Ödev 5")

string_value="Gelecek Hayalim: W-Code Veri Bilimi Atölyesi"

gelecek_hayalim_wcode=string_value[0:23]
veri_bilimi=string_value[24:35]
atolyesi=string_value[36:]

capital_string_value=string_value.upper()
print(capital_string_value)
lower_string_value=string_value.lower()
print(lower_string_value)

numbers="0123456789"

even_numbers=numbers[::2]
print(even_numbers)
odd_numbers=numbers[1::2]
print(odd_numbers)


