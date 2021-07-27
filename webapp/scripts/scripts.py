PRICE_MATERIAL = {
    "акрил-3мм":30,
    "акрил-4мм":40,
    "акрил-5мм":50,
    "акрил-6мм":60,
    "акрил-8мм":100,
    "акрил-10мм":120,
    "зеркальный-полистирол-2мм":35,
    "зеркальный-полистирол-3мм":45,
    "полистирол-3мм":30,
    "полистирол-4мм":40,
    "фанера-3мм":30, 
    "фанера-4мм":35,
    "фанера-6мм":60,
    "фанера-8мм":80
    }
COST_FILE_EDIT = 300
MIN_COST = 600

def serialize_price() -> list:
    return [(name, name) for name in PRICE_MATERIAL.keys()]

def cost_calc(cutting_len: int, material: str) -> int:
    return cutting_len * PRICE_MATERIAL[material]

def sum_prices(prices: list) -> int:
    
    cost = sum([price[2] for price in prices])
    cost += cost/100*10+COST_FILE_EDIT # +10% + working with a file
    if cost < MIN_COST:
        cost = MIN_COST
    return cost
