registered_plates = []      #List for registered display_plates
registered_cards = []       #List all registered credit cards
charges = 0                 #Counter for charges

def register_vehicle():
    '''
    Function to take user input for vehicle and card
    '''

    print("The parking lot has spaces for your vehicle")
    display_plates = input("Enter your plate number: ")

    if display_plates in registered_plates:
        print(f"{display_plates} is already in the list.")
        null = input("Press enter to continue...")
        if null == "":
            return (), ()
        
    else:
        credit_card = input("Enter your Credit Card Number ($4.00): ")
        registered_plates.append(display_plates)
        registered_cards.append(credit_card)
        print(f"Thank you, your plate {display_plates} has been added to the lot.")
        return display_plates, credit_card


 
def check_password():
    '''
    Function to check password
    '''

    while True:
        password_verify = input("Enter your password: ").upper()
        if password_verify == "password".upper():
            return True 
        else:
            print("Password is incorrect!")
            null = input("Press enter to continue...")
            if null == "":
                return False
            
             
 
def verify_vehicle():
    '''
    Function to check if vehicle is registered
    '''
    display_plates =input("Enter your plate number: ")
    if display_plates in registered_plates:
            print(f"The vehicle with plate {display_plates} is registered in the lot")
    if display_plates not in registered_plates:
        print("The vehicle is NOT registered")



def display_plates(plate_number):
    '''
    function to display then save plate numbers to '"vehicles.txt" 
    '''
    if registered_plates:
        with open("vehicles.txt", "w") as file:
            print(f"==========================\
            \nPlates\t\n\
==========================")
            for plate_number in registered_plates:
                print(f"{plate_number}")
                file.writelines("Daily Plates Registry:\n"
                                "==========================\n")
                file.writelines(f"Plate: {plate_number}\n")
            print(f"==========================\n")
    else:
        print("The parking lot is empty")




def display_charges(display_plates, credit_card, charges):
    '''
    Function to display and save charges to "charges.txt
    "'''
    with open("charges.txt", "w") as file:
        print(f"Daily parking summary for 17/11/2023\n\
================================================================\
              \nPlates\t\tCredit Card\t\tCharges In $\n\
              \n\
================================================================")
        for display_plates, credit_card in zip(registered_plates, registered_cards):
            charges += 4
            print(f"{display_plates}\t\t{credit_card}\t\t\t4")
            file.writelines(f"Plate: {display_plates}, Credit Card: {credit_card}, Charge: 4\n")
        print(f"================================================================\n\
Total                                   {charges}\
")

        
def remove_vehicle(registered_plates):
    """
    Function to remove a vehicles plate from the parking lot
    """
    deleting_plate = input("What is your plate number?\n")
            
    if deleting_plate in registered_plates:
        print(f"{deleting_plate} is removed")
        deleting = registered_plates.index(deleting_plate)
        del registered_plates[deleting]

        with open("vehicles.txt", "w") as file:
            for display_plates in registered_plates:
                file.writelines(f"=============================\n")
                file.writelines("Plate\n")
                file.writelines({display_plates})
                file.writelines("\n")

    else:
        print("Vehicle is not Registered")


def clearvehicles():
    """
    Function to clear the vehicles in the parking lot
    """
    print("All vehicles were removed and the lot is empty")
    registered_plates.clear()
    with open ("vehicles.txt", "w") as file:
        file.write("")

 
def print_menu():
    '''
    Function to print a menu with options
    '''

    print("""
***********************************************************
*** Welcome to Park and Go Parking Application! ***
Park from 6 PM - Midnight for a flat fee of $4.00
***********************************************************
Select from the following options
1- Register a vehicle
2- Verify vehicle registration
3- Display registered vehicles and save them to a file
4- Display daily charges and save them to a file
5- Remove a vehicle
6- Clear vehicles
0- Exit""")
 
exit = ("0","0-")    
print_menu()


while True:
    """
    Loop for inputs based upon print_menu() function
    """
    user_Input = input(">>> ")
    match user_Input:
        case "0":
            print("Thanks and Good Bye!")
            null = input("Press enter to continue...")
            if null == "":
                print_menu()

        case outside_of_range_number if int(outside_of_range_number) > 6:
            print("Invalid Input")

        case "1":
            lPlates, cCards = register_vehicle()

        case "2" if check_password():
            verify_vehicle()

        case "3" if check_password():
            display_plates(registered_plates)

        case "4" if check_password():
            display_charges(lPlates, cCards, charges)

        case "5" if check_password():
            remove_vehicle(registered_plates)

        case "6" if check_password():
            clearvehicles()


    null = input("Press enter to continue...")
    if null == "":
         print_menu()