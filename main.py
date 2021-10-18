def tipareste_meniu():
    print("1. Citire date")
    print("2. Eliminati duplicatele din lista")
    print("3. Suma primelor n numere pozitive")
    print("4. Toate numerele pozitive sunt in ordine crescatoare")
    print("5. Numerele care apar doar odata sunt inlocuite cu numarul de divizori proprii")
    print("6. Iesire")


def citeste_lista(lista: list) -> list[int]:
    """
    Citeste de la tastatura elementele unei liste
    :param lista: lista care trebuie citita de la tastatura
    :return: lista cu elemente citite de la tastatura
    """
    numar_elemente = int(input("Dati numarul de elemente ale liste: "))
    for i in range(numar_elemente):
        lista.append(int(input("Lista["+str(i)+"]= ")))
    return lista


def eliminare_duplicate(lista: list) -> list:
    """
    Elimina duplicatele dintr-o lista
    :param lista: Lista din care se elimina duplicate
    :return: Lista fara duplicate
    """
    rezultat = []
    for i in lista:
        if i not in rezultat:
            rezultat.append(i)
    return rezultat


def test_eliminare_duplicate():
    assert(eliminare_duplicate([10, 25, 13])) == [10, 25, 13]
    assert(eliminare_duplicate([10, 20, 10])) == [10, 20]
    assert (eliminare_duplicate([10, 25, 25, 25, 25])) == [10, 25]


def suma_primelor_n_pozitive(lista: list, n: int):
    """
    Calculeaza suma primelor n numere pozitive dintr-o lista
    :param lista: Lista in care se face calculul
    :param n: Suma primelor cate numere sa fie calculata
    :return: Daca exista cel putin n numere pozitive in lista, se retureanza suma lor, altfel se returneaza un mesaj
    """
    suma = 0
    for x in lista:
        if x > 0 and n > 0:
            suma = suma + x
            n = n - 1
    if n > 0:
        return "Dimensiunea listei este prea mică."
    else:
        return suma


def test_suma_primelor_n_pozitive():
    assert(suma_primelor_n_pozitive([15, -5, 26, 5], 2)) == 41
    assert(suma_primelor_n_pozitive([15, 25, -10, -14], 3)) == "Dimensiunea listei este prea mică."
    assert(suma_primelor_n_pozitive([10, 10, -14, 15, -9], 2)) == 20


def toate_elementele_pozitive_ordonate_crescator(lista: list) -> bool:
    """
    Verifica daca elementele pozitive dintr-o lista sunt ordonate crescator
    :param lista: Lista in care se efectueaza verificarea
    :return:
    """
    for x in lista:
        if x > 0:
            precedent = x
            break
    for x in lista:
        if 0 < x < precedent:
            return False
    return True


def test_toate_elementele_pozitive_ordonate_crescator():
    assert(toate_elementele_pozitive_ordonate_crescator([15, -5, 16, 17, 19])) is True
    assert (toate_elementele_pozitive_ordonate_crescator([15, 16, -5, 9])) is False
    assert (toate_elementele_pozitive_ordonate_crescator([8, 9, 10, 11])) is True


def numar_divizori_proprii(x) -> int:
    """
    Calculeaza numarul de divizori proprii ai unui numar
    :param x: Numar real
    :return: Numarul de divizori proprii ai parametrului x
    """
    numar_divizori = 0
    for i in range(2, x//2):
        if x % i == 0:
            numar_divizori += 1
    return numar_divizori


def test_numar_divizori_proprii():
    assert(numar_divizori_proprii(13)) == 0
    assert (numar_divizori_proprii(8)) == 2
    assert (numar_divizori_proprii(25)) == 1


def procesare_lista(lista: list) -> list:
    """
    Determina lista obtinuta din inlocuirea elementelor ce apar
    o singura data in lista cu numarul lor de divizori proprii
    :param lista: Lista asupra careia se face procesarea
    :return: Returneaza lista obtinuta in urma efectuarii procesarii
    """
    rezultat = []
    for x in lista:
        if lista.count(x) == 1:
            rezultat.append(numar_divizori_proprii(x))
        else:
            rezultat.append(x)
    return rezultat


def test_procesare_lista():
    assert(procesare_lista([25, 13, 26, 13, 19])) is [1, 13, 1, 13, 0]
    assert (procesare_lista([25, 13, 26, 19])) is [1, 0, 1, 0]
    assert (procesare_lista([25, 13, 25, 13])) is [25, 13, 25, 13]


def main():
    test_eliminare_duplicate()
    while True:
        tipareste_meniu()
        optiune = input("Introduceti optiunea: ")
        if optiune == "1":
            lista = []
            citeste_lista(lista)
        elif optiune == "2":
            print(eliminare_duplicate(lista))
        elif optiune == "3":
            n = int(input("Dati numarul n: "))
            print(suma_primelor_n_pozitive(lista, n))
        elif optiune == "4":
            if toate_elementele_pozitive_ordonate_crescator(lista) is True:
                print("DA")
            else:
                print("NU")
        elif optiune == "5":
            print(procesare_lista(lista))
        elif optiune == "6":
            break
        else:
            print("Optiune gresita, incercati din nou!")


main()
