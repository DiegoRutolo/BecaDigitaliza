planetas = ["Mercurio", "Venus", "Tierra", "Marte"]
tamanhos = [4879, 12103, 6271, 6794]
personas = ["Alicia", 24, 1.68, "Brais", 67, 1.58, "Carlos", 12, 1.38]

for i in planetas:
    print(i)
for i in tamanhos:
    print(i)
for i in personas:
    print(i)

print()

planeta = planetas[-1]
tamanho = tamanhos[-1]
persona = personas[-1]

print(personas[-3]+" mide "+str(persona)+" y vive en "+planeta+", que tiene un tamaño de "+str(tamanho)+"Km")
print()

libros = {"Robert Jordan": "La rueda del tiempo",
          "Stephen King": "El misterio de Salem's lot",
          "Christopher Paolini": "El legado",
          "George R. R. Martin": "Cancion de hielo y fuego",
          "C.S. Lewis": "Las cronicas de Narnia"
          }

print()
print(libros)
print(libros.keys())
print(libros.values())
for autor, saga in libros.items():
    print("\""+saga+"\" de "+autor+" es una muy buena.")
