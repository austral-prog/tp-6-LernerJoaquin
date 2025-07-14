# Replace the "ANSWER HERE" with your answer

def remove_elements(lista):
    # Eliminar primer, quinto y sexto elemento (índices 0, 4 y 5)
    # Para evitar problemas, se hace una copia y se elimina de atrás hacia adelante
    indices_a_remover = [5, 4, 0]
    copia = lista[:]  # Copia de la lista original
    for i in indices_a_remover:
        if i < len(copia):
            del copia[i]
    return copia


def add_elements(lista):
    return ['Pink'] + lista + ['Yellow']


def is_empty(lista):
    return len(lista) == 0


def check_lists(lista1, lista2):
    if len(lista1) >= 3 and len(lista2) >= 3:
        return lista1[2] == lista2[2]
    return False


def list_of_lists(lista_de_listas):
    resultado = []
    
    if len(lista_de_listas) >= 1:
        resultado.append(lista_de_listas[0][:2])  # primeros 2 elementos
    if len(lista_de_listas) >= 2:
        resultado.append(lista_de_listas[1][1:4])  # segundo a cuarto (índices 1 al 3)
    if len(lista_de_listas) >= 3:
        resultado.append(lista_de_listas[2][-2:])  # últimos 2 elementos
    
    return resultado
