import inventory
    
def write_to_file():
    f = open("carlist.txt", "w")
    for car in inventory.Inventory.Car_List:
        f.write(f"{car.make} {car.model} {car.color} {car.year} {car.mileage}\n")
    f.close()

def read_from_file():
    f = open("carlist.txt", "r")
    
    print(f.read())
    
    
