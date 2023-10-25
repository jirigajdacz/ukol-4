def hlavni():
    telefonni_cislo = input("Zadejte telefonní číslo: ")
    
    if overit_telefoni_cislo(telefonni_cislo):
        text_zpravy = input("Zadejte text zprávy: ")
        cena = cena_zpravy(text_zpravy)
        print(f"Cena zprávy: {cena} Kč")
    else:
        print("Neplatné telefonní číslo.")


def overit_telefoni_cislo(cislo):
    if (len(cislo) == 9) or (len(cislo) == 13 and cislo.startswith("+420")):
        if cislo.replace("+", "").isdigit():
            return True
    return False

def cena_zpravy(text_zpravy):
    delka_zpravy = len(text_zpravy)
    cena = (delka_zpravy // 180) * 3
    if delka_zpravy % 180 != 0:
        cena += 3
    return cena



hlavni()

overit_telefoni_cislo()

cena_zpravy()





