
def skapa():
    fil_namn = input("Vad ska filen heta? ")
    barn_namn = input("Vad heter barnet? ")
    with open(fil_namn, "w", encoding="utf8") as fil:
        fil.write(barn_namn+"\n\n")
        grejer = int(input("Hur många saker vill du skriva in ?"))
        for i in range(grejer):
            fil.write(input("Skriv vad du vill skriva in: ")+"\n")
    main()

def läsa():
    fil_namn = input("Vad heter filen du vill öppna? ")
    with open(fil_namn, "r", encoding="utf8") as fil:
        lines = fil.readlines()
        namn = lines[0].rstrip()
        print(f"Namnet på barnet är {namn}\n")
        print(f"{namn} ville ha följande:")
        for i in range(2, len(lines)):
            print(lines[i], end="")
        print("")
    main()

def naughty_list():
    with open("kolbarn.txt", "r", encoding="utf8") as fil:
        lines = fil.readlines()
        print("Följande barn är på stygglistan just nu: ")
        for namn in lines:
            print(namn.rstrip())
    choise = input("Vill du lägga till barn? ja eller nej\n:")
    if choise == "ja":
        with open("kolbarn.txt", "a", encoding="utf8") as fil:
            rep = int(input("Hur många namn vill du lägga till: "))
            for _ in range(rep):
                fil.write(input("Namn på barn: ")+"\n")
    else:
        print("ok, tillbaka till main-->")
    main()

def main():
    print("--Välkommen till main--")
    choise = input("Vill du 1) skapa önskelista eller 2) läsa upp önskelista\n3) the naughty list\n: ")
    if choise == "1":
        skapa()
    elif choise == "2":
        läsa()
    elif choise == "3":
        naughty_list()

if __name__ == "__main__":
    main()