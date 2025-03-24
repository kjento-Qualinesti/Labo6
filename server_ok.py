import	sys
from keuze import keuze
from Servers import checkAllServers,loadServerList


def main():
    loadServerList()
    if len(sys.argv) > 1:
        if sys.argv[1] == "check":
            checkAllServers()
        else:
            print("U heeft iets fout ingegeven.")
    else:
        while True:
            print("Wat wil je doen:\n"
            "1. server toevoegen\n"
            "2. server verwijderen\n"
            "3. server lijst tonen\n"
            "4. server checken\n"
            "0. stoppen")
            try:
                nummer = int(input("keuze: "))
                keuze(nummer)
            except ValueError:
                print("U heeft iets fout ingevoerd probeer opnieuw.")
                
                



if __name__ == "__main__":
    main()