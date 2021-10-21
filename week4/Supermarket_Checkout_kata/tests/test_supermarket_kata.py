# import pytest
# from lib.supermarket_kata import Checkout

# @pytest.fixture()
# def checkout():
#     checkout = Checkout()
#     return checkout

# def test_Can_Add_Item(checkout):
#     addItem = checkout.Can_Add_Item_andPrice_andDiscount("Item001")
#     assert addItem == [
#         {"name": "Item001", "price": None, "discount": None}]

# def test_Can_Add_Item_Price(checkout):
#     checkout.listItems = []
#     addItemPrice = checkout.Can_Add_Item_andPrice_andDiscount("Item001", "95")
#     assert addItemPrice == [
#         {"name": "Item001", "price": "95", "discount": None}]

# def test_Can_Add_Discount_Rules(checkout):
#     checkout.listItems = []
#     addDiscountRule = checkout.Can_Add_Item_andPrice_andDiscount(
#         "Item001", "95", "0.25")
#     assert addDiscountRule == [
#         {"name": "Item001", "price": "95", "discount": "0.25"}]

# def test_Can_Calculate_Current_Total(checkout):
#     total = checkout.Can_Calculate_Current_Total()
#     assert total == {"total": "94.75"}
#     pass

# def test_Can_Add_Multiple_Items_And_Get_Current_Total(checkout):
#     pass

# def test_Can_Apply_Discount_Rules_To_Total(checkout):
#     pass

# def test_Throw_Error_For_Item_With_No_Price():
#     pass
