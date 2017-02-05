#this code asks for your weight and tells you what your weight would be on another planet

weight = int(input("Please enter your current earth weight (lb only): "))

print("\nI have info for the following planets: ")
print("1. Venus     2. Mars      3. Jupiter")
print("4. Saturn    5. Uranus    6. Neptune")

choice = int(input("\nWhich planet are you visiting? "))

if (choice == 1):
    pweight = weight*0.78
    planet = "Venus"
elif (choice == 2):
    pweight = weight*0.39
    planet = "Mars"
elif (choice == 3):
    pweight = weight*2.65
    planet = "Jupiter"
elif (choice == 4):
    pweight = weight*1.17
    planet = "Saturn"
elif (choice == 5):
    pweight = weight*1.05
    planet = "Uranus"
elif (choice == 6):
    pweight = weight*1.23
    planet = "Neptune"

print("Your weight would be",pweight,"pounds on the planet", planet)



