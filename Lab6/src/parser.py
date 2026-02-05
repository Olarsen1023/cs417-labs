def parse_product_basic(response = dict()):
    basic = dict()
    name = "name"
    id = "id"
    basic[id] = response[id]
    basic[name] = response[name]
    return basic

def parse_availability(response = dict()):
    if response["in_stock"] == True:
        return True
    return False