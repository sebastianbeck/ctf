import numpy as np


arr0 = np.array([0, 1, 2, 3, 4])
print("arr0:\n{}".format(arr0))
print("Slicing arr0[1:3]: elemente von index 1 bis 3 (ohne letztes (3)")
print(arr0[1:3])
print("Slicing arr0[2:]: Alle Elemente ab 2")
print(arr0[2:])
print("Slicing arr0[:3]: Alle Elemente bis (und ohne) Index 3")
print(arr0[:3])
print("""Slicing arr0[:]: Alle Elemente. bei eindimensionalen Arrays gleich wie
      arr0 (siehe oben""")
print(arr0[:])

print("""\n\n\nFunktioniert auch bei mehrdimensionalen Arrays. Hier ist die
      Reihenfolge der Dimensionen von aussen nach innen (nach eckigen Klammern""")
arr1 = np.array([[0, 1, 2, 3, 4],
                 [1, 2, 3, 4, 5],
                 [2, 3, 4, 5, 6],
                 [3, 4, 5, 6, 7],
                 [4, 5, 6, 7, 8]])
print("arr1:\n{}".format(arr1))

print("Slicing arr1[0, :]: Erste Dimension des äusseren Arrays und alle Elemente davon.")
print(arr1[0, :])

print("Slicing arr1[:,0]: Alle Dimensionen des äusseren Arrays aber nur das 1te Element jeder davon.")
print(arr1[:, 1])

print("""Slicing arr1[2:4, 1:4]): 2te bis (und ohne) 4te Dimension des äusseren Arrays (Zeilen 2 und 3)
        und davon jeweils Elemente 1 bis (und ohne 4) (Spalten 2, 3, 4)""")
print(arr1[2:4, 1:4])
