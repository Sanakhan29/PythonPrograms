ali = input('Is Ali Present Today? (y/n):')

sara = input('Is Sara Present Today? (y/n):')

if(ali == "y") and (sara == "y"):
    print("They both are present")
if(ali == "y") and (sara =="n"):
    print("Only ali is present")
if(ali == "n") and (sara == "n"):
    print("No one is present")


sana = input("Is sana playing outside? (y/n):")
marina = input("I marina playing outside? (y/n):")

if(sana == "y") or (marina == "y"):
    print("They both are playing outside")

