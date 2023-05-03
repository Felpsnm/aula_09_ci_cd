import methods
 
def test_area():
    # given a width of 2 and a height of 5
    width = 2
    height = 5

    # when we calculate the area
    output = methods.area_of_rectangle(width, height)

    # then the area should be 10
    assert output == 10
 
def test_perimeter():
    # given a width of 2 and a height of 5
    width = 2
    height = 5

    # when we calculate the perimeter
    output = methods.perimeter_of_rectangle(width, height)
    
    # then the perimeter should be 14
    assert output == 14

def test_sum():
    # given the 2 values
    value1 = 2
    value2 = 5
    
    # when we calculate the sum
    output = methods.sum(value1, value2)
    
    # then the result should be 7
    assert output == 7
    
def test_sub():
    # given the 2 values
    value1 = 7
    value2 = 5
    
    # when we calculate the subtraction
    output = methods.sub(value1, value2)
    
    # then the result should be 2
    assert output == 2
    
def test_mul():
    # given the 2 values
    value1 = 2
    value2 = 5
    
    # when we calculate the multiplication
    output = methods.mul(value1, value2)
    
    # then the result should be 10
    assert output == 10
    
def test_div():
    # given the 2 values
    value1 = 4
    value2 = 2
    
    # when we calculate the division
    output = methods.div(value1, value2)
    
    # then the result should be 2
    assert output == 2