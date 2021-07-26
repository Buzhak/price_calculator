from webapp.scripts import cost_calc, price, serialize_price, sum_prices, COST_FILE_EDIT, MIN_COST

def test_price():
    assert iter(price()) 

def test_serialize_price():
    assert iter(serialize_price()) 

def test_cost_calc():
    assert cost_calc(10, "акрил-3мм") == 300

def test_sum_prices():
    assert sum_prices([[0,0,1000], [0,0,1000]]) == 2000 + 200 + COST_FILE_EDIT
    assert sum_prices([[0,0,100], [0,0,100]]) == MIN_COST
