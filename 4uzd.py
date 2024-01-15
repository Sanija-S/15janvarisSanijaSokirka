def ierakstit_vardu_faila(vards, fails_cesta):
    try:
        with open(fails_cesta, 'a') as fails:
            fails.write(vards + '\n')
        print("Vārds veiksmīgi ierakstīts failā.")
    except IOError as e:
        print(f"Kļūda: Nevarēja ierakstīt failā. {e}")
    except Exception as e:
        print(f"Kļūda: Nezināma kļūda. {e}")


vards = input("Ievadiet savu vārdu: ")


fails_cesta = 'lietotajs.txt'

ierakstit_vardu_faila(vards, fails_cesta)
