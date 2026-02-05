from parser import parse_product_basic, parse_availability

def test_parse_product_basic_extracts_id(valid_product):
    basic = parse_product_basic(valid_product)
    assert "id" in basic, "The 'id' key should be in the dictionary"

def test_parse_product_basic_extracts_name(valid_product):
    basic = parse_product_basic(valid_product)
    assert "name" in basic, "The 'name' key should be in the dictionary"

def test_parse_product_basic_returns_only_id_and_name(valid_product):
    basic = parse_product_basic(valid_product)
    assert "name" and "id" in basic, "should only have id and name keys"

def test_parse_availability_when_in_stock(valid_product):
    aval = parse_availability(valid_product)
    assert aval is True, "Product in stock"

def test_parse_availability_when_out_of_stock(product_out_of_stock):
    aval = parse_availability(product_out_of_stock)
    assert aval is False, "Product out of stock"

def test_parse_availability_when_field_missing(minimal_product):
    aval = parse_availability(minimal_product)
    assert aval is False, "Product Missing"