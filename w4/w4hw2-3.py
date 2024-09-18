print("Ödev-2,3")
"""Ödev-2: Kullanıcıdan kullanıcı adı ve şifre oluşturmasını istenir. Şifrenin uzunluğu altı haneye ulaşmışsa hesabınız oluşturuldu mesajı alınır, altı haneden azsa altı haneli şifre oluşturması gerektiğinin mesajı alınır. (Sadece koşul kullanılması yeterli.)


Ödev-3: Bir önceki örnek geliştirilir.


 Kullanıcı girdiği şifre 5 ve 10 hane arasında olmak zorunda. 
 Eğer bu koşula uyuyorsa "Hesabınız oluşturuldu." mesajı alır. 
 Koşulu sağlamıyorsa "Lütfen girdiniz şifre 5 haneden az 10 haneden fazla olmasın!" uyarısı alır. 
 Bunu oluştururken kullanıcı istediğimiz şartlarda şifre oluşturana kadar sormaya devam eder 
 """
user_name=input("Enter your name: ")
while True:
   password=input("Enter your password: ")
   if 5< len(password)<10:
      print("Welcome",user_name, "your password is saved")
      break
   else:
        print("Please enter a password between 5 and 10 characters")
        
