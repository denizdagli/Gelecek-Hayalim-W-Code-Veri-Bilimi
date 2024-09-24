import numpy as np
""" Sayılardan oluşan bir boyutlu array oluşturulur. Arrayi oluştururken 
sayıların veri tipini integer olarak belirtilir. Oluşturulan arrayin boyut, 
eleman sayısı bilgilerine bakılır. """
array_1d = [1, 2, 3, 4, 5, 6]  # Tüm sayılar integer
print(array_1d)
print("Eleman sayısı:", len(array_1d))
print("Boyut:", 1)  #bir boyutlu dizi
print("--------------------")

""" İki ve üç boyutlu arrayler oluşturulur. Bu arraylerin boyut, eleman sayısı, satır, sütun bilgilerine ulaşılır. Arrayler üzerinde indexleme ve dilimleme(slicing) işlemi yapılır. """

array_2d= [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # Tüm sayılar integer
print(array_2d)
print("Eleman sayısı:", len(array_2d)*len(array_2d[0]))
print("Boyut:", 2)  #iki boyutlu dizi
print("Satır sayısı:", len(array_2d))
print("Sütun sayısı:", len(array_2d[0]))
print("İndexleme:", array_2d[1][1])
print("Slicing:", array_2d[1][1:])

print("--------------------")

array_3d = [[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]]  # Tüm sayılar integer
print(array_3d)
print("Eleman sayısı:", len(array_3d)*len(array_3d[0])*len(array_3d[0][0]))
print("Boyut:", 3)  #üç boyutlu dizi
print("Satır sayısı:", len(array_3d))
print("Sütun sayısı:", len(array_3d[0]))
print("Derinlik sayısı:", len(array_3d[0][0]))
print("İndexleme:", array_3d[1][1][1])
print("Slicing:", array_3d[1][1][1:])


print("--------------------")
"""Numpy fonksiyonu kullanarak bir, iki ve üç boyutlu arrayler oluşturulur. Arrayler üzerinde indexleme ve dilimleme(slicing) işlemi yapılır """


one_d_array = np.array([1, 2, 3], dtype=int)
print(one_d_array)
print("1D array'in eleman sayısı: ", one_d_array.size)
print("1D array'in boyutu: ", one_d_array.ndim)
print("1D array'in şekli: ", one_d_array.shape)
print("Indexleme: ", one_d_array[0])
print("Slicing: ", one_d_array[1:])

print("--------------------")

two_d_array = np.array([[1, 2, 3]], dtype=int)
print(two_d_array)
print("2D array'in eleman sayısı: ", two_d_array.size)
print("2D array'in boyutu: ", two_d_array.ndim)
print("2D array'in şekli: ", two_d_array.shape)
print("2D array'in sütun sayısı: ", two_d_array.shape[1])
print("2D array'in satır sayısı: ", two_d_array.shape[0])
print("Indexleme: ", two_d_array[0, 1])
print("Slicing: ", two_d_array[0, 1:])

print("--------------------")
three_d_array = np.array([[[1, 2, 3], [4, 5, 6]], 
                          [[7, 8, 9], [10, 11, 12]]], dtype=int)
print(three_d_array)

print("3D array'in eleman sayısı: ", three_d_array.size)
print("3D array'in boyutu: ", three_d_array.ndim)
print("3D array'in şekli: ", three_d_array.shape)
print("3D array'in sütun sayısı: ", three_d_array.shape[1])
print("3D array'in satır sayısı: ", three_d_array.shape[0])
print("3D array'in derinlik sayısı: ", three_d_array.shape[2])
print("Indexleme: ", three_d_array[1, 1, 1])
print("Slicing: ", three_d_array[1, 1, :])

print("--------------------")

"""Sıfırlardan oluşan ve birlerden oluşan iki tane iki boyutlu array oluşturulur. Bu arrayler satır ve sütun bazında birleştirilir. """

zeros_array = np.zeros((2, 2), dtype=int)
print("Sıfırlardan oluşan array:\n ", zeros_array) 
print("--------------------")
ones_array = np.ones((2, 2), dtype=int)
print("Birlerden oluşan array: \n",  ones_array)
print("--------------------")
concatenate_array_c = np.concatenate((zeros_array, ones_array), axis=1)
print("Sütun bazlı birleştirildiğinde: \n",   concatenate_array_c)
print("--------------------")

concatenate_array_r = np.concatenate((zeros_array, ones_array), axis=0)
print("Satır bazlı birleştirildiğinde: \n",concatenate_array_r)
print("--------------------")
