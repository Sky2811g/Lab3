import price_info 
price_list={'apple' : 1.5, 'orange':1.4 }
quantity_list={'apple' : 1, 'orange':1 }

def test_total_cost_shopping():
    assert price_info.total_cost_shopping(price_list,quantity_list)==2.9

def test_cost_of_fruit():
    price_list={'apple' : 1.5, 'orange':1.4 }
    assert price_info.cost_of_fruits('apple', 4,price_list) == 6