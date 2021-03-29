import pytest
import service.customer
from model.customer import Customer
from helper.customer_helper import convert_customer_list
from app import initialize_web_app


@pytest.fixture
def app():
    app = initialize_web_app()
    return app.app


@pytest.fixture
def customer_test_value():
    customer = Customer()
    customer.set_identifier("7d0e2324-7057-435f-8510-f05a6bb2d7f5")
    customer.set_first_name("Tom")
    customer.set_last_name("Smith")
    customer.set_middle_initial("K")
    return customer


@pytest.fixture
def expected_find_all_value():

    customers = [customer_test_value]

    expected_value = {
        "success": True,
        "data": {
            "customers": convert_customer_list(customers)
        }
    }

    return expected_value


def test_find_all(client, mocker):

    customer = Customer()
    customer.set_identifier("7d0e2324-7057-435f-8510-f05a6bb2d7f5")
    customer.set_first_name("Tom")
    customer.set_last_name("Smith")
    customer.set_middle_initial("K")

    mock_customer_service = mocker.patch.object(service.customer.CustomerService, 'find_all', name='mock_customer_service')
    mock_customer_service.return_value = [customer]

    url = 'http://localhost:8000/api/customers'

    resp = client.get(url)
    assert resp.status_code == 200

    resp_body = resp.json

    first_customer = resp_body['data']['customers'][0]

    assert first_customer['first_name'] == 'Tom'
