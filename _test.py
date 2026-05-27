import pytest 

##function to test square
def square(n):
    return n*n

##function to test cube
def cube(n):
    return n*n*n

##function to test fifth power
def fifth(n):
    return n**5


##Test cases for square
def test_square():
    assert square(2) == 4  ##"Test Failed: Square of 2 should be 4"
    assert square(3) == 9  ##"Test Failed: Square of 3 should be 9"
    assert square(4) == 16  ##"Test Failed: Square of 4 should be 16"

##Test cases for cube
def test_cube():
    assert cube(2) == 8  ##"Test Failed: Cube of 2 should be 8"
    assert cube(3) == 27  ##"Test Failed: Cube of 3 should be 27"
    assert cube(4) == 64  ##"Test Failed: Cube of 4 should be 64"

##Test cases for fifth power
def test_fifth():
    assert fifth(2) == 32  ##"Test Failed: Fifth power of 2 should be 32"
    assert fifth(3) == 243  ##"Test Failed: Fifth power of 3 should be 243"
    assert fifth(4) == 1024  ##"Test Failed: Fifth power of 4 should be 1024"

##Test for invalid input
def test_invalid_input():
    with pytest.raises(TypeError):
        square("string")
    with pytest.raises(TypeError):
        cube("string")
    with pytest.raises(TypeError):
        fifth("string")
