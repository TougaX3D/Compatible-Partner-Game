#this program is made to practice my knowledge on *args **kwargs

def girl1(*args, **kwargs):
    for arg in args:
        print(f"{arg}", end=" ")
    print()
    for keys, values in kwargs.items():
        print(f"{keys}: {values}")
    print()  

def girl2(*args, **kwargs):
    for arg in args:
        print(f"{arg}", end=" ")
    print()
    for keys, values in kwargs.items():
        print(f"{keys}: {values}")
    print()

def girl3(*args, **kwargs):
    for arg in args:
        print(f"{arg}", end=" ")
    print()
    for keys, values in kwargs.items():
        print(f"{keys}: {values}")
    print()


while True:
    print("---------------------------------------------------")
    print(" Goodday! This is the Compatible Partner Game!!!")
    print("---------------------------------------------------\n")
    print("In this game you find which girl is most compatible with you, and you pick them to be your partner!!!")
    ans = input("Do you wanna play the game? (Y/N): ").upper()

    if ans == "Y":
        print("\n--- Candidate 1 ---")
        girl1("Candice", "D", "Fitinyomout",
              age=16,
              vibe="chill",
              pros=["pretty", "matching music tastes", "no baggage"],
              cons=["replies late", "low eq"])

        print("--- Candidate 2 ---")
        girl2("Hali", "Maw", "Magaral",
              age=17,
              vibe="passionate",
              pros=["cute", "academic achiever", "nerdy", "high eq & iq"],
              cons=["focused on acads"])

        print("--- Candidate 3 ---")
        girl3("shea", "f", "ordastritz",
              age=19,
              vibe="attention - seeking",
              pros=["sexy", "beautiful", "clingy", "high eq"],
              cons=["in multiple situationships", "emotional instability"])
        
        while True:
            ans2 = (input("Please enter which candidate to choose as your partner!!!(1/2/3):"))

            if ans2 == 1:
                print("\n---------------------------------------------------------------------------------------------------------------------")
                print("At first you and candice vibed well. but after a while her cons of replies late and low eq started to burn you out")
                print("At the end you guys started to fight alot, and the relation ship ended...")
                print("------------------------------------------------------YOU LOST!!!-----------------------------------------------------\n")
                break
            elif ans2 == 2:
                print("\n----------------------------------------------------------------------------------------------------------------------------------------")
                print("You and hali actually vibed really well. You liked how weird and nerdy she was, and her con of (focused on acads) didnt even phase you")
                print("At the end you guys started to get closer, and the relation ship continued to grow!")
                print("---------------------------------------------------------------YOU WON!!!----------------------------------------------------------------\n")
                break
            elif ans2 == 3:
                print("\n---------------------------------------------------------------------------------------------------------------------------------------------")
                print("You and shea vibed well. You even experienced some things ;). but her cons of having multiple situationships and her emotional instability")
                print("continued to trouble you. Leading you to have fights with her and with her situationships. at the end you and her broke up...")
                print("-----------------------------------------------------------------YOU LOST!!!------------------------------------------------------------------\n")
                break
            else:
                print("\nYou did not input correctly! please choose between (1/2/3)\n")
        
        again = input("Play again? (Y/N): ").upper()
        if again != "Y":
            print("Thanks for playing!")
            break
    else:
        print("Maybe next time!")
        break