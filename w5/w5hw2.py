""""Aşağıdaki işlemleri indexing ve slicing kullanarak liste üzerinde uygulayın.

liste = ["Python",True,9,"3",8.4,"Hi-Kod","False",4.7]
"3" değerine ulaşmak için indexleme yapın.

"Hi-Kod" değerine ulaşmak için indexleme yapın.

4.7 değerine ulaşmak için indexleme yapın.

9,"3",8.4,"Hi-Kod" değerlerine ulaşmak için slicing yapın.

8.4,"Hi-Kod","False",4.7 değerlerine ulaşmak için slicing yapın.
"""
liste = ["Python",True,9,"3",8.4,"Hi-Kod","False",4.7]

print(liste[3])
print(liste[5])
print(liste[-1])
print(liste[2:6])
print(liste[4:])

#Verilen listede bulunan string veri tipindeki öğeleri yeni_liste isimli listeye eklenir.
new_list=[string for string in liste if type(string)==str]
print(new_list)

#Enumerate methodunu araştırın ve aşağıdaki örneği enumerate methodu ile yapın.

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
for index in range(len(fruits)):
     print("{}. indexte bulunan meyve: {}".format(index,fruits[index]))

for i, fruit in enumerate(fruits):
    print("{}. indexte bulunan meyve: {}".format(i,fruit))
