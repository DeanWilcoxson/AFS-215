import pytest
from lib.checkout import Checkout

@pytest.fixture()
def checkout():
    checkout = Checkout()
    checkout.addItemPrice("a", 1)
    checkout.addItemPrice("b", 2)
    return checkout

def test_Can_Calculate_Current_Total(checkout):
    checkout.addItem("a")
    assert checkout.calculateTotal() == 1

def test_Get_Correct_Total_With_Multiple_Items(checkout):
    checkout.addItem("a")
    checkout.addItem("b")
    assert checkout.calculateTotal() == 3

def test_Can_Add_Discount_Rule(checkout):
    checkout.addDiscount("a", 3, 2)

def test_Can_Apply_Discounts_To_Total(checkout):
    checkout.addDiscount("a", 3, 2)
    checkout.addItem("a")    
    checkout.addItem("a")
    checkout.addItem("a")
    assert checkout.calculateTotal() == 2

def test_Exception_With_Bad_Item(checkout):
    with pytest.raises(Exception):
        checkout.addItem("c")