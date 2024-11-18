import Lab2.Lab2 as Lab2

def test_find_min_max():
    
    test_list = [3, 1, 7, -5, 10, 0, 4]
    min_value , max_value =Lab2.find_min_max(test_list)
    assert min_value == -5
    assert max_value == 10
def test_calc_average():
    test_list = [2,2]
    average_value = Lab2.calc_average(test_list)
    assert average_value == 2

def test_calc_median_temperature():
    test_list = [3, 1, 7, -5, 10, 0, 4]
    median_value = Lab2.calc_median_temperature(test_list)
    assert median_value == 3
