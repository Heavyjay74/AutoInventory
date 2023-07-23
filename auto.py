import menu
import inventory
import autofileio

class Automobile:

    def __init__(self, make, model, color, year, mileage):
        self.make = make
        self.model = model
        self.color = color
        self.year = year
        self.mileage = mileage

    
    def main():
        
        inventory.update_car_list()  #updates temp list of cars in Inventory module
        menu1 = menu.Menu()
        menu1.Menu_Selection()

    if __name__ == "__main__":
        main()

def Add_Vehicle():

    make = input("Please enter the make: ")
    model = input("Please enter the model: ")
    color = input("Please enter the color: ")
    while True:
        try:
            year_input = int(input("Please enter the year: "))
            
        except ValueError:
            print("Please enter only digits for the year")
        else:
            year = year_input
            break
    while True:
        try:
            mileage_input = int(input("Please enter the mileage: "))
        except ValueError:
            print("Please enter only digits for the mileage")
        else:
            mileage = mileage_input
            break
        
    a = Automobile(make, model, color, year, mileage)
    
    print(f"You entered a {a.color} {a.year} {a.make} {a.model} with {a.mileage:,d} miles")
    
    while True:
        answer = input("Do you want to add this vehicle to the permanent inventory? Type 'yes' or 'no': ")
        if answer == "yes":
            inventory.Inventory.Car_List.append(a)  #adds new vehicle to temp Car_List
            autofileio.write_to_file()              #writes temp Car_List to permanent carlist.txt
            print("Car added to permanent inventory")
            break
        elif answer == "no":
            print("Car not added to permanent inventory")
            break
        else:
            print("please enter 'yes' or 'no'")

def Delete_Vehicle():
    for i in range(len(inventory.Inventory.Car_List)):
        inventory.Print_Vehicle_Info(i)
        max = len(inventory.Inventory.Car_List)

    print("")
    while True:
        try:
            user_input = int(input("Please enter an inventory number to delete, or '0' to go back to menu: "))
            if user_input == 0:
                break
        except :
            print(f"please enter a number between 1 and {max} ")
        else:
            try:
                n = (user_input - 1)
                inventory.Inventory.Car_List.pop(n)
            except:
                print(f"Please only enter a number between 1 and {max} ")
            else:
                autofileio.write_to_file()
                print(f"Vehicle number {user_input} removed from inventory")
                print("")
                break

def Update_Vehicle():
    for i in range(len(inventory.Inventory.Car_List)):
        inventory.Print_Vehicle_Info(i)
        max = len(inventory.Inventory.Car_List)

    print("")
    while True:
        try:
            user_input = int(input("Please enter an inventory number to update, or '0' to go back to menu: "))
            if user_input == 0:
                break
        except :
            print(f"please enter a number between 1 and {max} ")
        else:
            try:
                n = (user_input - 1)
                assert (user_input > 0 and user_input <= len(inventory.Inventory.Car_List))
            except:
                print(f"Please only enter a number between 1 and {max} ")
            else:
                make = input("Please enter the make: ")
                model = input("Please enter the model: ")
                color = input("Please enter the color: ")
                while True:
                    try:
                        year_input = int(input("Please enter the year: "))
            
                    except ValueError:
                        print("Please enter only digits for the year")
                    else:
                        year = year_input
                        break
                while True:
                    try:
                        mileage_input = int(input("Please enter the mileage: "))
                    except ValueError:
                        print("Please enter only digits for the mileage")
                    else:
                        mileage = mileage_input
                        break
        
                a = Automobile(make, model, color, year, mileage)
    
                print(f"You entered a {a.color} {a.year} {a.make} {a.model} with {a.mileage:,d} miles")
    
                while True:
                    answer = input(f"Do you want to update this to vehicle number {user_input} to the permanent inventory? Type 'yes' or 'no': ")
                    if answer == "yes":
                        inventory.Inventory.Car_List[n] = a  #adds new vehicle to temp Car_List
                        autofileio.write_to_file()              #writes temp Car_List to permanent carlist.txt
                        print("Car added to permanent inventory")
                        break
                    elif answer == "no":
                        print("Inventory not updated")
                        break
                    else:
                        print("please enter 'yes' or 'no'")

                print("")
                break
            
    
            
