

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

def main():
    print("--Välkommen till main--")
    choise = input("Vill du 1) skapa önskelista eller 2) läsa upp önskelista\n: ")
    if choise == "1":
        skapa()
    elif choise == "2":
        läsa()

if __name__ == "__main__":
    main()