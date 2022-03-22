#! /usr/bin/python3 

import calculator

def test_calculator ():
    assert calculator.calculator("add",1,1) == 2
def test_calculator2():
    assert calculator.calculator("add",-1,1) == 0 #counts the number of test passed if we have seperate functions for each test 
def test_calculator3():
    assert calculator.calculator("multiply",1,1) ==1
    assert calculator.calculator("multiply",4,0) ==0
    assert calculator.calculator("multiply",-2,2) ==-4
    assert calculator.calculator("multiply",3,3) ==9


