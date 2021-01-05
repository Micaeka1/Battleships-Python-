import pytest
from battleships import *
    
s1 = (2, 2, False, 3, {(2,2), (3,2), (4,2)})
#we use global variables if certain ships or fleets are used in multiple test functions
s2 = (5, 7, False, 3, set())
s3 = (3, 0, True, 4, set())
s4 = (9, 9, True, 1, set())
s5 = (5, 3, True, 2, set())
s6 = (1, 8, True, 1, set())
fleet = [s3,s6]
    
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


def test_is_open_sea1():
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


def test_is_sunk1():
    assert is_sunk(s1) == True
    assert is_sunk(s2) == False
    assert is_sunk(s3) == False
    s = (9, 9, True, 1, {(9,9)})
    t = (5, 3, True, 2, {(5,4)})
    assert is_sunk(s) == True
    assert is_sunk(t) == False

def test_ship_coordinates1():
    assert ship_coordinates(s1[0],s1[1],s1[2],s1[3]) == [(2,2),(3,2),(4,2)]
    assert ship_coordinates(s2[0],s2[1],s2[2],s2[3]) == [(5,7),(6,7),(7,7)]
    assert ship_coordinates(s3[0],s3[1],s3[2],s3[3]) == [(3,0),(3,1),(3,2), (3,3)]
    assert ship_coordinates(s4[0],s4[1],s4[2],s4[3]) == [(9,9)]
    assert ship_coordinates(s5[0],s5[1],s5[2],s5[3]) == [(5,3),(5,4)]
    
def test_check_if_hits1():
    assert check_if_hits(1,9,fleet) == False
    assert check_if_hits(3,3,fleet) == True
    assert check_if_hits(2,8,fleet) == False
    assert check_if_hits(5,1,fleet) == False
    assert check_if_hits(1,8,fleet) == True

f1 = [(1,1,True, 3, set()), (1,6, False, 2, set()), (2,9, False, 2, set()), (3,0,True, 1, set()), \
              (3,2,True,3, set()), (5,1,True,2, {(5,2)}), (5,4,True,1, set()), (5,7,True,1,set()), (6,9,False,4,set()), (9, 0, True, 1, set()) ] 

def test_hit1():
    (actual,s) = hit(3,0,fleet)
    s3[4].add((3,0))
    expected = fleet
    assert (actual, s) == (expected, s3)
    (actual,s) = hit(3,1,fleet)
    s3[4].add((3,1))
    expected = fleet
    assert (actual, s) == (expected, s3)
    (actual,s) = hit(3,2,fleet)
    s3[4].add((3,2))
    expected = fleet
    assert (actual, s) == (expected, s3)
    (actual,s) = hit(3,3,fleet)
    s3[4].add((3,3))
    expected = fleet
    assert (actual, s) == (expected, s3)
    (actual,s) = hit(1,8,fleet)
    s6[4].add((1,8))
    expected = fleet
    assert (actual, s) == (expected, s6)
    
def test_are_unsunk_ships_left1():
    f1 = [(1,1,True, 3, set()), (1,6, False, 2, set()), (2,9, False, 2, set())]
    f2 = []
    assert are_unsunk_ships_left(f1) == True
    assert are_unsunk_ships_left(f2) == False
    assert are_unsunk_ships_left(fleet) == True
    fleet.remove(s3)
    assert are_unsunk_ships_left(fleet) == True
    fleet.remove(s6)
    assert are_unsunk_ships_left(fleet) == False