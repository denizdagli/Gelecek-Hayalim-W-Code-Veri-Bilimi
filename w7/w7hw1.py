
import pandas as pd


sozluk = {"Kategori": ["Giyim","Giyim", "Ayakkabı","Aksesuar","Ayakkabı","Giyim","Aksesuar","Aksesuar","Ayakkabı","Giyim"],


  "Ürün" : ["Kazak","T-shirt","Sandalet","Küpe","Spor Ayakkabı","Pantolon","Kolye","Yüzük","Çizme","Ceket"],


"Fiyat" : [300,180,450,50,700,400,150,80,850,900]}

# Yukarıdaki sözlük DataFrame’e dönüştürülür. 

df =pd.DataFrame(sozluk)

print(df)   

print("--------------------")
# 2.indexte bulunan kategori bulunur. (Sadece kategori bilgisi) 
print(" 2.indexte bulunan kategori: ", df["Kategori"][2]) 
#2. indexte bulunan ürün bulunur. (Sadece ürün bilgisi) 
print(" 2.indexte bulunan ürün: ", df["Ürün"][2]) 
#4.indexten 9.indexe kadar olan veriler bulunur. (Kategori,ürün,fiyat bilgisi beraber) 
print("4.indexten 9.indexe kadar olan veriler:\n",df.iloc[4:9])
print("--------------------")
print(" 1.indexten 6.indexe kadar olan ürünler:\n", df["Ürün"][1:6])
print("--------------------")
# Giyim kategorisinde bulunan ürünler gösterilir. 
print("Giyim kategorisinde bulunan ürünler gösterilir:\n",df.loc[df.Kategori == "Giyim", "Ürün"]) 
print("--------------------")
# Ayakkabı kategorisinde bulunan ürünler gösterilir. 
print("Ayakkabı kategorisinde bulunan ürünler gösterilir:\n",df.loc[df.Kategori == "Ayakkabı", "Ürün"])
print("--------------------")
#Aksesuar kategorisinde bulunan ürünler gösterilir. 
print("Aksesuar kategorisinde bulunan ürünler gösterilir:\n", df.loc[df.Kategori == "Aksesuar", "Ürün"])

print("--------------------")
#Giyim kategorisinde fiyatı 300'den fazla olan ürünler gösterilir. 
print("Giyim kategorisinde fiyatı 300'den fazla olan ürünler:\n", df[(df["Fiyat"] > 300) & (df["Kategori"] == "Giyim")])
print("--------------------")
# Ayakkabı kategorisinde fiyatı 600'den az olan ürünler gösterilir. 
print("Ayakkabı kategorisinde fiyatı 600'den az olan ürünler:\n", df[(df["Fiyat"] < 600) & (df["Kategori"] == "Ayakkabı")])
print("--------------------")
#Aksesuar kategorisinde fiyatı 100'den fazla olan aksesuar gösterilir. 
print("Aksesuar kategorisinde fiyatı 100'den fazla olan aksesuar:\n", df[(df["Fiyat"] > 100) & (df["Kategori"] == "Aksesuar")])