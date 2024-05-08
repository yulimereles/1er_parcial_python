def eliminar_duplicados(lista):
    #para almacenar los elementos unicos
    #El set() elimina los elementos duplicados de la lista.
    elementos_unicos = set()
    #se crea para almacenar los elementos unicos en el orden original
    lista_sin_duplicados = []

    #recorre la lista original 
    for elemento in lista: 
        #si el elemento no esta en el conjunto de elementos unicos, se le añade ala lista de duplicados
        #y se le agrega en el conjunto de elementos unicos.
        if elemento not in elementos_unicos:
            lista_sin_duplicados.append(elemento)
            elementos_unicos.add(elemento)
    return lista_sin_duplicados
print(eliminar_duplicados([1, 2, 3, 4, 4, 5, 6, 6, 7]))
#tiene que devolver una nueva lista: [1, 2, 3, 4, 5, 6, 7], sin los elementos duplicados y en el mismo orden :)

    