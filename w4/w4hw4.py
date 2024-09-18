"""Kullanıcıdan isim ve şifre isteyeceğiz ve şifre girişi için üç hak verilir.


 Eğer önceden tanımlı şifre ile kullanıcıdan gelen şifre aynıysa "Giriş yapıldı." yazar. 
 Şifre girişi yanlışsa "Yanlış şifre girildi!" uyarısı verilsin ve üç yanlış denemede program biter. 
 Tercihe göre kalan hak bilgisi verilir. """


username=input("Enter your username: ")

max_attempt=3  #maximum number of attempts
original_password="deniz123"

for i in range(max_attempt):
        password=input("Enter your password: ")
        
        if password==original_password:
            print("Welcome",username)
            break
        else:
            remaining_attempts=max_attempt-i-1
            if remaining_attempts>0:
                print(f"Invalid password,TRY AGAIN you have {remaining_attempts} attempts left")
            else:
                print("Invalid password, your account is blocked")



    
    



