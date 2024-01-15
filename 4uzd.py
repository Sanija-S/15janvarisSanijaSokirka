def nolasit_un_izdrukats(nosaukums, formats):
    try:
        fails_cesta = f"{nosaukums}.{formats}"
        with open(fails_cesta, 'r') as fails:
            saturs = fails.read()
            print(f"Faila saturs ({nosaukums}.{formats}):")
            print(saturs)
    except FileNotFoundError:
        print(f"Kļūda: Fails '{nosaukums}.{formats}' netika atrasts.")
    except IOError as e:
        print(f"Kļūda: Nevarēja nolasīt failu. {e}")
    except Exception as e:
        print(f"Kļūda: Nezināma kļūda. {e}")

nosaukums = input("Ievadiet faila nosaukumu: ")
formats = input("Ievadiet faila formātu (paplašinājumu): ")


nolasit_un_izdrukats(nosaukums, formats)
