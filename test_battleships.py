import pytest
from battleships import *
    
def test_is_sunk1():
    s = (2, 3, False, 3, {(2,3), (3,3), (4,3)})
    assert is_sunk(s) == True
    t1 = (2,3,True,3,{(2,3), (2,4)})
    assert is_sunk(t1) == False
    t2 = (1,0,True,1,{(1,0)}
    assert is_sunk(t2) == True
    t3 = (5,7,False,3,{(5,7),(6,7)}
    assert is_sunk(t3) == True
    t4 = (8,4,True, 4, {(8,6),(8,7),(8,4)}
    assert is_sunk(t4) == False

def test_ship_type1():
    #add at least one test for ship_type by the deadline of session 7 assignment
     ship1 = (8,4,True,4)
     assert ship_type1(ship1) == 'battleship'
    #provide at least five tests in total for ship_type by the project submission deadline

def test_is_open_sea1():
    #add at least one test for open_sea by the deadline of session 7 assignment
    fleet = [(4,1,True,4),(7,0,False,3),(9,0,True,1),(9,7,True,1),(9,9,True,1),(8,4,True,3),
             (0,0,False,2),(2,6,False,2),(9,0,True,2),(5,3, True,1)]
    assert is_open_sea1(5,6,fleet) == True
          
    #provide at least five tests in total for open_sea by the project submission deadline

def test_ok_to_place_ship_at1():   
        #add at least one test for ok_to_place_ship_at by the deadline of session 7 assignment
        fleet = [(4,1,True,4),(7,0,False,3),(9,0,True,1),(9,7,True,1),(9,9,True,1),(8,4,True,3),
                 (0,0,False,2),(2,6,False,2),(9,0,True,2),(5,3, True,1)]
        assert ok_to_place_ship_at(5,3,True,1,fleet) == True
        #provide at least five tests in total for ok_to_place_ship_at by the project submission deadline

def test_place_ship_at1():
    #add at least one test for place_ship_at by the deadline of session 7 assignment
          fleet2 = [(4,1,True,4),(7,0,False,3),(9,0,True,1),(9,7,True,1),(9,9,True,1),(8,4,True,3),
                     (0,0,False,2),(2,6,False,2),(9,0,True,2)]
          fleet1 = [(4,1,True,4),(7,0,False,3),(9,0,True,1),(9,7,True,1),(9,9,True,1),(8,4,True,3),
                     (0,0,False,2),(2,6,False,2),(9,0,True,2),(5,3,True,1)]
          assert place_ship_at1(5,3,True,1,fleet2) == fleet1
    #provide at least five tests in total for place_ship_at by the project submission deadline

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
    
