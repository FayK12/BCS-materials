#this program allows a user to buy keychains, by adding and removing chains from their checkout order
#and to view their order

def add_keychains(current_numberofkeychains):
    add = input("You have "+ str(current_numberofkeychains) + " keychains. How many to add? " )       #must convert to str for display  
    newnumberofchains = int(add) + current_numberofkeychains                                #must convert var add to int for addition      
    return newnumberofchains

def remove_keychains(current_numberofkeychains):
    remove = input("You have "+ str(current_numberofkeychains) + " keychains. How many to remove? " )        #must convert to str for display  
    newnumberofchains = current_numberofkeychains - int(remove)                                     #must convert var add to int for addition      
    return newnumberofchains

def view_order(current_numberofkeychains,cost):
    print("You have " + str(current_numberofkeychains) + " keychains in your cart")
    print("Each keychain costs $" + str(cost))
    totalcost = cost * int(current_numberofkeychains)
    print("Your total order comes to $" + str(totalcost)+ ".")

def checkout(current_numberofkeychains,cost):
    name = input("What is the customer's name: ")
    view_order(current_numberofkeychains,cost)
    print (name + ", thanks for shopping at Ye Olde Keychain today! See you next time.")

print ("\nYe Olde Keychain Shoppe")
user_choice = 1
current_numberofkeychains = 0
cost = 10
while (user_choice != 4) and (user_choice !=0):
    
    print("\n0. Exit")
    print("1. Add Keychains to Order")
    print("2. Remove Keychains from Order")
    print("3. View Current Order")
    print("4. Checkout")
    print()
    user_choice = int(input("Please enter your choice: "))
    
    if user_choice == 1:      #must use == to evaluate user input                                                              
        current_numberofkeychains=add_keychains(current_numberofkeychains)
        print("You now have " + str(current_numberofkeychains) + " keychains")
    elif user_choice == 2:
        current_numberofkeychains=remove_keychains(current_numberofkeychains)
        print("You now have " + str(current_numberofkeychains) + " keychains")
    elif user_choice == 3:
        view_order(current_numberofkeychains,cost)
    elif user_choice == 4:
        checkout(current_numberofkeychains,cost)
    elif (user_choice==0):
        print ("Goodbye.")              
