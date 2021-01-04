import pytest
from battleships import *
    
s1 = (2, 2, False, 3, {(2,2), (3,2), (4,2)})
#we use global variables if certain ships or fleets are used in multiple test functions
s2 = (5, 7, False, 3, set())
s3 = (3, 0, True, 4, set())
s4 = (9, 9, True, 1, set())
s5 = (5, 3, True, 2, set())
s6 = (1, 8, True, 1, set())

    
def test_ship_type1():
    assert ship_type(s1) == "Cruiser"
    assert ship_type(s2) == "Cruiser"
    assert ship_type(s3) == "Battleship"
    assert ship_type(s4) == "Submarine"
    assert ship_type(s5) == "Destroyer"

def test_place_ship_at1():
    f = []
    place_ship_at(s2[0],s2[1],s2[2],s2[3],f)
    expected = [s2]
    assert expected == f
    place_ship_at(s3[0],s3[1],s3[2],s3[3],f)
    expected = [s2,s3]
    assert expected == f
    place_ship_at(s4[0],s4[1],s4[2],s4[3],f)
    expected = [s2,s3,s4]
    assert expected == f
    place_ship_at(s5[0],s5[1],s5[2],s5[3],f)
    expected = [s2,s3,s4,s5]
    assert expected == f
    place_ship_at(s6[0],s6[1],s6[2],s6[3],f)
    expected = [s2,s3,s4,s5,s6]
    assert expected == f
    print(f)

fleet = [s3,s6]

def test_is_open_sea1():
    #add at least one test for open_sea by the deadline of session 7 assignment
    '''fleet = [(4,1,True,4),(7,0,False,3),(9,0,True,1),(9,7,True,1),(9,9,True,1),(8,4,True,3),
             (0,0,False,2),(2,6,False,2),(9,0,True,2),(5,3, True,1)]'''
    assert is_open_sea(s5[0],s5[1],fleet) == True
    assert is_open_sea(s4[0],s4[1],fleet) == True
    assert is_open_sea(s2[0],s2[1],fleet) == True
    assert is_open_sea(s1[0],s1[1],fleet) == False
    assert is_open_sea(0,9,fleet) == False

def test_ok_to_place_ship_at1():   
    assert ok_to_place_ship_at(s5[0],s5[1],s5[2],s5[3],fleet) == True
    assert ok_to_place_ship_at(s4[0],s4[1],s4[2],s4[3],fleet) == True
    assert ok_to_place_ship_at(s2[0],s2[1],s2[2],s2[3],fleet) == True
    assert ok_to_place_ship_at(s1[0],s1[1],s1[2],s1[3],fleet) == False
    assert ok_to_place_ship_at(0,9,True,2,fleet) == False

'''
def test_is_sunk1():
    assert is_sunk(s1) == True
    
def test_check_if_hits1():
    #add at least one test for check_if_hits by the deadline of session 7 assignment
    fleet = [(4,1,True,4),(7,0,False,3),(9,0,True,1),(9,7,True,1),(9,9,True,1),(8,4,True,3),
             (0,0,False,2),(2,6,False,2),(9,0,True,2),(5,3, True,1)]
    assert check_if_hits1(3,2,fleet) == True
          
          
    #provide at least five tests in total for check_if_hits by the project submission deadline

def test_hit1():
    #add at least one test for hit by the deadline of session 7 assignment
    fleet2 = [(4,1,True,4),(7,0,False,3),(9,0,True,1),(9,7,True,1),(9,9,True,1),(8,4,True,3),
               (0,0,False,2),(2,6,False,2),(9,0,True,2)]
    fleet1 = [(4,1,True,4),(7,0,False,3),(9,0,True,1),(9,7,True,1),(9,9,True,1),(8,4,True,3),
              (0,0,False,2),(2,6,False,2),(9,0,True,2),(5,3,True,1)] 
    assert hit1(5,3,fleet1) == (fleet2,(5,3,True,1)    
    #provide at least five tests in total for hit by the project submission deadline

def test_are_unsunk_ships_left1():
    #add at least one test for are_unsunk_ships_left by the deadline of session 7 assignment
    fleet = [(4,1,True,4),(7,0,False,3),(9,0,True,1),(9,7,True,1),(9,9,True,1),(8,4,True,3),
             (0,0,False,2),(2,6,False,2),(9,0,True,2),(5,3, True,1)]
    assert are_unsunk_ships_left1(fleet) == True
    #provide at least five tests in total for are_unsunk_ships_left by the project submission deadline
    
'''