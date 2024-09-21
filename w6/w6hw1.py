
"""Bir sözlük oluşturulur ve bu sözlükte öğrencilerin isimleri ve Matematik, Fizik, Kimya notları tutulur. Kullanıcıdan isim ve ders ismi(Matematik, Fizik, Kimya) istenir ve bu bilgilere göre çıktı verilir.

Sözlük üzerinde değerleri değiştirme, yeni değer ekleme, kullanıcıya ulaşmak istediği bilgileri sorma gibi uygulamalar yapın."""
students = {
    "Deniz": {"Fizik": 90, "Kimya": 80, "Matematik": 70},
    "Doğukan": {"Fizik": 80, "Kimya": 70, "Matematik": 60},
    "Tuğba": {"Fizik": 70, "Kimya": 60, "Matematik": 50},
}

# Öğrenci listesini döndüren fonksiyon
def ogrenci_listesi():
    return list(students.keys())

# Belirli bir öğrenciyi kontrol eden fonksiyon
def ogrenci_var_mi(name):
    return name in students

# Belirli bir dersin öğrenci notları arasında olup olmadığını kontrol eden fonksiyon
def ders_var_mi(name, lesson):
    return lesson in students[name]

# Tüm notları ya da belirli bir öğrencinin notlarını gösteren fonksiyon
def not_goruntuleme():
    print("\nMENU\n a - Tüm Öğrencilerin Notları\n b - Belirli Bir Öğrencinin Notları")
    islem = input("Seçiminizi yapınız: ").lower()
    
    if islem == "a":
        for student, dersler in students.items():
            print(f"{student} isimli öğrencinin notları: {dersler}")
    
    elif islem == "b":
        name = input("Öğrenci adı giriniz: ")
        if ogrenci_var_mi(name):
            print(f"{name} isimli öğrencinin notları: {students[name]}")
        else:
            print("Öğrenci bulunamadı.")
    
    else:
        print("Geçersiz işlem.")
        
# Yeni ders ve not ekleyen fonksiyon
def ders_ekleme():
    name = input("Öğrenci adı giriniz: ")
    
    if ogrenci_var_mi(name):
        lesson = input("Eklemek istediğiniz dersin adını giriniz: ")
        
        if ders_var_mi(name, lesson):
            print("Bu ders zaten mevcut.")
        else:
            try:
                grade = float(input("Not giriniz: "))
                students[name][lesson] = grade
                print(f"{lesson} dersi eklendi.")
            except ValueError:
                print("Geçerli bir not giriniz.")
    else:
        print("Öğrenci bulunamadı.")
        
# Var olan bir notu güncelleyen fonksiyon
def not_guncelle():
    name = input("Öğrenci adı giriniz: ")
    
    if ogrenci_var_mi(name):
        lesson = input("Güncellemek istediğiniz dersin adını giriniz: ")
        
        if ders_var_mi(name, lesson):
            try:
                grade = float(input("Yeni not giriniz: "))
                students[name][lesson] = grade
                print(f"{lesson} dersi için not güncellendi.")
            except ValueError:
                print("Geçerli bir not giriniz.")
        else:
            print("Bu ders bulunamadı.")
    else:
        print("Öğrenci bulunamadı.")
        
# Ana menü fonksiyonu
def get_student_knowledge():
    while True:
        print("\nANA MENÜ")
        islem = input("a - Öğrenci Listesi\nb - Not Görüntüleme\nc - Ders ve Not Ekleme\nd - Not Güncelle\nq - Çıkış\nSeçiminizi yapınız: ").lower()
        
        if islem == "a":
            print("Öğrenci Listesi:", ogrenci_listesi())
        
        elif islem == "b":
            not_goruntuleme()
        
        elif islem == "c":
            ders_ekleme()
        
        elif islem == "d":
            not_guncelle()
        
        elif islem == "q":
            print("Çıkış yapılıyor...")
            break
        
        else:
            print("Geçersiz seçim, lütfen tekrar deneyin.")

# Programı başlat
get_student_knowledge()
