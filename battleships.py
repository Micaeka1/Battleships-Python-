import random

'''
is_open_sea(row, column, fleet) -- checks if the square given by row and column neither contains 
nor is adjacent (horizontally, vertically, or diagonally) to some ship in fleet. Returns Boolean
True if so and False otherwise
'''
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
'''
ok_to_place_ship_at(row, column, horizontal, length, fleet)-- checks if addition of a 
ship, specified by row, column, horizontal, and length as in ship representation above, 
to the fleet results in a legal arrangement (see the figure above). If so, the function
returns Boolean True and it returns False otherwise. This function makes use of the 
function is_open_sea
'''
def ok_to_place_ship_at(row, column, horizontal, length, fleet):
    new_ship_coords = {(row,column)} 
    if horizontal == True:
        if column + length > 10:
            return False
        for i in range(1,length):
            new_ship_coords.add((row,column + i))
    else:
        if row + length > 10:
            return False
        for i in range(1,length):
            new_ship_coords.add((row + i,column))

    for elem in new_ship_coords:
        if is_open_sea(elem[0],elem[1],fleet) == False:
            return False

    return True

'''
place_ship_at(row, column, horizontal, length, fleet) -- returns a new fleet that is the result 
of adding a ship, specified by row, column, horizontal, and length as in ship representation above, 
to fleet. It may be assumed that the resulting arrangement of the new fleet is legal
'''
def place_ship_at(row, column, horizontal, length, fleet):
    return fleet.append((row,column,horizontal,length,set()))

'''
randomly_place_all_ships() -- returns a fleet that is a result of a random legal arrangement of 
the 10 ships in the ocean. This function makes use of the functions ok_to_place_ship_at and place_ship_at
'''
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

'''
ship_type(ship) -- returns one of the strings "Battleship", "Cruiser", "Destroyer", or "Submarine" identifying 
the type of ship
'''
def ship_type(ship):
    ships = {4:'Battleship', 3: 'Cruiser', 2: "Destroyer", 1: "Submarine"}
    return ships[ship[3]]

'''
is_sunk(ship) -- returns Boolean value, which is True if ship is sunk and False otherwise
'''
def is_sunk(ship):
    if ship[3] == len(ship[4]):
        return True
    else: return False

'''
check_if_hits(row, column, fleet) -- returns Boolean value, which is True if the shot of the human player at 
the square represented by row and column hits any of the ships of fleet, and False otherwise
'''
def check_if_hits(row, column, fleet):
    for elem in fleet:
        ship_coords= ship_coordinates(elem[0], elem[1],elem[2],elem[3])
        if (row,column) in ship_coords:
            return True
    return False

'''
ship_coordinates(row,column,horizontal, length) -- returns all the coordinates of the ship specified by row, column,
horizontal and length
'''
def ship_coordinates(row,column,horizontal, length):
    coords = [(row,column)]
    if horizontal == True:
        for i in range(1,length):
            coords.append((row,column + i))
    else:
        for i in range(1,length):
            coords.append((row + i,column)) 
    return coords

'''
hit(row, column, fleet) -- returns a tuple (fleet1, ship) where ship is the ship from the fleet fleet that 
receives a hit by the shot at the square represented by row and column, and fleet1 is the fleet resulting 
from this hit. It may be assumed that shooting at the square row, column results in of some ship in fleet
'''
def hit(row, column, fleet):
    for i in range(len(fleet)):
        ship_coords= ship_coordinates(fleet[i][0], fleet[i][1], fleet[i][2],fleet[i][3])
        if (row,column) in ship_coords:
            fleet[i][4].add((row,column) )
            ship = fleet[i]
            return (fleet, ship)

'''
are_unsunk_ships_left(fleet) -- returns Boolean value, which is True if there are ships in the fleet that are still 
not sunk, and False otherwise
'''
def are_unsunk_ships_left(fleet):
    if fleet != []:
        return True
    else: return False

'''
main() -- returns nothing. It prompts the user to call out rows and columns of shots and outputs the responses of 
the computer iteratively until the game stops.
'''
def main():
    current_fleet = randomly_place_all_ships()
    game_over = False
    shots = 0
    hits = []
    while not game_over:
        loc_str = input("Enter row and colum to shoot (separted by space): ").split()
        valid = False
        # Check that the user input is valid, plus, it gives the user the option to quit the game by entering 'q'
        while not valid:
            if len(loc_str) != 2:
                if loc_str == ['q']:
                    break
                else:
                    print("Error! Please enter integers between 0 and 9 (separted by space) to continue")
                    print("If you want to quit, type " + "q")
                    loc_str = input().split()
            else:
                try:
                    current_row = int(loc_str[0])
                    current_column = int(loc_str[1])  
                    if current_row < 0 or current_row >9 or current_column <0 or current_column > 9:
                        print("Error! Please enter integers between 0 and 9 (separted by space) to continue")
                        print("If you want to quit, type " + "q")
                        loc_str = input().split()
                    else: valid = True

                except ValueError:
                    print("Error! Please enter integers between 0 and 9 (separted by space) to continue")
                    print("If you want to quit, type " + "q")
                    loc_str = input().split()

        if loc_str == ['q']:
            break   
        
        shots += 1
        if (current_row, current_column) in hits:
            print("You missed!")
        elif check_if_hits(current_row, current_column, current_fleet):
            print("You have a hit!")
            hits.append((current_row, current_column))
            (current_fleet, ship_hit) = hit(current_row, current_column, current_fleet)
            if is_sunk(ship_hit):
                print("You sank a " + ship_type(ship_hit) + "!")
                current_fleet.remove(ship_hit)
        else:
            print("You missed!")

        if not are_unsunk_ships_left(current_fleet): game_over = True

    print("Game over! You required", shots, "shots.")


if __name__ == '__main__': #keep this in
   main()
