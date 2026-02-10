import pytest
from checkout import Checkout

@pytest.fixture
def checkout():
    return Checkout()

# Happy path: Test adding a single item

def test_add_item(checkout):
    checkout.add_item('apple', 1.0)
    assert checkout.get_total() == 1.0

# Happy path: Test removing an item

def test_remove_item(checkout):
    checkout.add_item('apple', 1.0)
    checkout.remove_item('apple', 1.0)
    assert checkout.get_total() == 0.0

# Edge case: Test adding multiple items and getting the total

def test_multiple_items(checkout):
    checkout.add_item('apple', 1.0)
    checkout.add_item('banana', 2.0)
    assert checkout.get_total() == 3.0

# Edge case: Test removing an item that was added multiple times

def test_remove_item_multiple_times(checkout):
    checkout.add_item('apple', 1.0)
    checkout.add_item('apple', 1.0)
    checkout.remove_item('apple', 1.0)
    assert checkout.get_total() == 1.0

# Error handling: Test removing an item that is not in the cart

def test_remove_non_existent_item(checkout):
    with pytest.raises(ValueError):
        checkout.remove_item('apple', 1.0)

# Happy path: Test resetting the cart

def test_reset_cart(checkout):
    checkout.add_item('apple', 1.0)
    checkout.reset_cart()
    assert checkout.get_total() == 0.0