

class Inventory:

    Car_List = []

    def __init__(self, Car_List):
        self.Car_List = Car_List
        

def Print_Vehicle_Info(inventory_Number):
    a = Inventory.Car_List[inventory_Number]
    print(f"{inventory_Number + 1}: {a.year} {a.color} {a.make} {a.model} with {a.mileage:,d} miles")
    
def update_car_list():  #add permanent inventory list into temporary list
    import auto
    try:
        f = open("carlist.txt", "x")
    except:
        print("opening existing file 'carlist.txt'")
        
    f = open("carlist.txt", "r")
    for x in f:
        line = x.split()
        make = line[0]
        model = line[1]
        color = line[2]
        year = int(line[3])
        mileage = int(line[4])
        a = auto.Automobile(make, model, color, year, mileage)
        Inventory.Car_List.append(a)
    f.close()
