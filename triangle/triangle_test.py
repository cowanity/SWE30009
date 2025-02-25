import pytest
import triangle


# test if a,b,c are sides of right-angle triangle (RAT)
def test_right_angle_triangle(): # take a,b,c as input
    a,b,c = 3,4,5 # input of triangle sides
    tri = triangle.Triangle(a,b,c) # call the function in triangle program
    expected = triangle.longDesc["RAT"] # get the expected output of RAT
    actual = tri.get_triangle_type() # get the actual output
    assert expected == actual
    print(actual)

# test if a,b,c are sides of an acute-angled triangle (AAT)
def test_acute_angle_triangle(): # take a,b,c as input
    a,b,c = 12,14,16 # input of triangle sides
    tri = triangle.Triangle(a,b,c) # call the function in triangle program
    expected = triangle.longDesc["AAT"] # get the expected output of RAT
    actual = tri.get_triangle_type() # get the actual output
    assert expected == actual
    print(actual)

# test if a,b,c are sides of Isosceles triangle (IsosT)
def test_isosceles_triangle(): # take a,b,c as input
    a,b,c = 5,5,8 # input of triangle sides
    tri = triangle.Triangle(a,b,c) # call the function in triangle program
    expected = triangle.longDesc["IsosT"] # get the expected output of RAT
    actual = tri.get_triangle_type() # get the actual output
    assert expected == actual
    print(actual)

# test if a,b,c are sides of Equilateral triangle (EqilT)
def test_equilateral_triangle(): # take a,b,c as input
    a,b,c = 2,2,2 # input of triangle sides
    tri = triangle.Triangle(a,b,c) # call the function in triangle program
    expected = triangle.longDesc["EqilT"] # get the expected output of RAT
    actual = tri.get_triangle_type() # get the actual output
    assert expected == actual
    print(actual)
    
    
# test if a,b,c are sides of obtuse-angled triangle (OAT)
def test_obtuse_angled_triangle(): # take a,b,c as input
    a,b,c = 3,4,6 # input of triangle sides
    tri = triangle.Triangle(a,b,c) # call the function in triangle program
    expected = triangle.longDesc["OAT"] # get the expected output of RAT
    actual = tri.get_triangle_type() # get the actual output
    assert expected == actual
    print(actual)
    
# default
if __name__ == "__main__":
    test_acute_angle_triangle()
    test_equilateral_triangle()
    test_isosceles_triangle()
    test_obtuse_angled_triangle()
    test_right_angle_triangle()