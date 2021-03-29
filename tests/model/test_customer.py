import uuid
from model.customer import Customer


def test_new():
    customer = Customer()
    customer = customer.new_from_dict({"first_name": "John", "last_name": "Doe", "middle_initial": "F"})
    assert customer.str() == "Customer [first_name: John, last_name: Doe]"


def test_new_from_dict():
    customer = Customer()
    customer_dict = {"identifier": str(uuid.uuid4()), "first_name": "John",
                     "last_name": "Doe", "middle_initial": "F"}
    customer = customer.new_from_dict(customer_dict)
    assert customer.to_dict() == customer_dict


def test_get_set_identifier():
    customer = Customer()
    customer. set_identifier("4fd4efa6-7116-4976-b615-385179122723")
    assert customer.get_identifier() == "4fd4efa6-7116-4976-b615-385179122723"


def test_get_set_first_name():
    cust = Customer()
    cust.set_first_name("John")
    assert cust.get_first_name() == "John"


def test_get_set_last_name():
    cust = Customer()
    cust.set_last_name("Doe")
    assert cust.get_last_name() == "Doe"


def test_get_set_middle_initial():
    cust = Customer()
    cust.set_middle_initial("F")
    assert cust.get_middle_initial() == "F"

