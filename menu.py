import autofileio

class Menu:

    def Menu_Selection(self):
        import auto
        import inventory
        
        while True:
            try:
                print("Please select from the following menu:");
                print("1: Add new vehicle to inventory");
                print("2: Delete vehicle from inventory");
                print("3: Update vehicle information");
                print("4: Print vehicle information");
                print("5: Exit program");
                print("")
                
                selection = int(input("Please enter a selection: "))

            except ValueError:
                print("ERROR: Only value accepted are digits.")
            else:
                print(f"you selected option {selection}")
                
                if selection == 1:
                    auto.Add_Vehicle()
                elif selection == 2:
                    auto.Delete_Vehicle()
                elif selection == 3:
                    auto.Update_Vehicle()
                elif selection == 4:
                    print("Printing vehicle information")
                    print("")
                    for i in range(len(inventory.Inventory.Car_List)):
                        inventory.Print_Vehicle_Info(i)
                    print("")
                elif selection == 5:
                    print("Thank you for using Jason's Inventory program!")
                    print("end of program")
                    break
        

