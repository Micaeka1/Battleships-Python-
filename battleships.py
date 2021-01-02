import random

def is_open_sea(row,column,fleet):
    if fleet == []:
        return True
    all_ship_coordinates = set()
    for elem in fleet:
        hor = elem[2]
        l = elem[3]
        all_ship_coordinates.add((elem[0],elem[1]))
        i = 1
        if hor == True:
            while i < l:
                all_ship_coordinates.add((elem[0],elem[1]+i))
                i += 1
        else:
            while i < l:
                all_ship_coordinates.add((elem[0]+i,elem[1]))
                i += 1

    for elem in all_ship_coordinates:
        if abs(row-elem[0]) <= 1 and abs(column - elem[1]) <= 1:
                return False
    return True  

def ok_to_place_ship_at(row, column, horizontal, length, fleet):
    new_ship_coords = {(row,column)} 
    if horizontal == True:
        if column + length > 9:
            return False
        for i in range(1,length):
            new_ship_coords.add((row,column + i))
    else:
        if row + length > 9:
            return False
        for i in range(1,length):
            new_ship_coords.add((row + i,column))

    for elem in new_ship_coords:
        if is_open_sea(elem[0],elem[1],fleet) == False:
            return False

    return True
        
    
    
def place_ship_at(row, column, horizontal, length, fleet):
    return fleet.append((row,column,horizontal,length,{}))

def randomly_place_all_ships():
    fleet = []
    ship_lengths = [1,2,3,4]
    # Place battleship
    row = random.randint(0,9)
    col = random.randint(0,9)
    horizontal = bool(random.getrandbits(1))
    place_ship_at(row,col,horizontal,ship_lengths[3],fleet)
    
    # Place cruisers
    i = 0
    while i != 2:
        row = random.randint(0,9)
        col = random.randint(0,9)
        horizontal = bool(random.getrandbits(1))
        if ok_to_place_ship_at(row, col, horizontal, ship_lengths[2], fleet):
            place_ship_at(row,col,horizontal,ship_lengths[2],fleet)
            i += 1
    
    # Place destroyers
    i = 0
    while i != 3:
        row = random.randint(0,9)
        col = random.randint(0,9)
        horizontal = bool(random.getrandbits(1))
        if ok_to_place_ship_at(row, col, horizontal, ship_lengths[1], fleet):
            place_ship_at(row,col,horizontal,ship_lengths[1],fleet)
            i += 1
    
    # Place destroyers
    i = 0
    while i != 4:
        row = random.randint(0,9)
        col = random.randint(0,9)
        horizontal = bool(random.getrandbits(1))
        if ok_to_place_ship_at(row, col, horizontal, ship_lengths[0], fleet):
            place_ship_at(row,col,horizontal,ship_lengths[0],fleet)
            i += 1
    
    return fleet

def ship_type(ship):
    ships = {4:'Battleship', 3: 'Cruiser', 2: "Destroyer", 1: "Submarine"}
    return ships[ship[3]]

'''def is_sunk(ship):
    #remove pass and add your implementation
    pass

def check_if_hits(row, column, fleet):
    #remove pass and add your implementation
    pass

def hit(row, column, fleet):
    #remove pass and add your implementation
    pass

def are_unsunk_ships_left(fleet):
    #remove pass and add your implementation
    pass

def main():
    #the implementation provided below is indicative only
    #you should improve it or fully rewrite to provide better functionality (see readme file)
    current_fleet = randomly_place_all_ships()

    game_over = False
    shots = 0

    while not game_over:
        loc_str = input("Enter row and colum to shoot (separted by space): ").split()    
        current_row = int(loc_str[0])
        current_column = int(loc_str[1])
        shots += 1
        if check_if_hits(current_row, current_column, current_fleet):
            print("You have a hit!")
            (current_fleet, ship_hit) = hit(current_row, current_column, current_fleet)
            if is_sunk(ship_hit):
                print("You sank a " + ship_type(ship_hit) + "!")
        else:
            print("You missed!")

        if not are_unsunk_shis_left(current_fleet): game_over = True

    print("Game over! You required", shots, "shots.")


if __name__ == '__main__': #keep this in
   main()
'''

f = randomly_place_all_ships()
print(f)
