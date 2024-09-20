#• Kullanıcıdan pi değeri ve yarıçap bilgisi alarak dairenin alanını hesaplayan bir fonksiyon oluşturulur.

def calculate_circle_area():
    pi_value=float(input("Enter the value of pi: "))
    circle_radius=float(input("Enter the radius of the circle: "))
    circle_area=pi_value*circle_radius**2
    return circle_area

print(calculate_circle_area())

#• Faktöriyel adında fonksiyon oluşturulur. Döngü kullanarak parametre olarak girilen sayının faktöriyeli hesaplanır. Format metodunu kullanılarak ekrana yazdırılır.
number=int(input("Enter a number: "))

def factorial(number):
    for i in range(1,number):
        number*=i
    return number
print("factorial of the {} is: {} ".format(number,factorial(number)))

#• Kişinin fonksiyona doğum yılını vererek kaç yaşında olduğunu hesaplayan bir fonksiyon oluşturun. 
def calculate_age(year_of_birth):
    current_year=2024
    age=current_year-year_of_birth
    return age

#print(calculate_age(2001))

"""Doğum yılı ve isim bilgisi verilen fonksiyon kişinin emekli olup olmadığını söylesin.
(Kişi 65 yaşında ise emekli olur.) Burada yaş hesabını yukarıdaki örnekteki fonksiyonu kullanarak yapsın.(Yani fonksiyon içinde fonksiyon kullanmanızı istiyorum :)) Kişi 65 yaşında ya da daha fazlaysa "Emekli oldunuz" yanıtını, 
65 yaşından küçükse emekliliğine kaç yıl kaldığını da hesaplayarak "(isim) emekliliğine (yıl) kaldı." yanıtını versin."""

def retirement_status(year_of_birth,name):
    age=calculate_age(year_of_birth)
    if age<65:
        remaining_year=65-age
        return f"{name} is not retired, {remaining_year} years left to retirement"
    else:
        return f"{name} is retired"
    
print(retirement_status(1950,"Emre"))