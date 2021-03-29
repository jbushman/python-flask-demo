import pytest
import sqlalchemy
from sqlalchemy import orm
from model.customer import Customer
from db.dao.base_dao import BaseDao


@pytest.fixture
def general_test_customer():
    customer = Customer()
    customer.set_identifier("9b4a56ea-de9b-4662-9c12-646033d77483")
    customer.set_first_name("Test")
    customer.set_last_name("User")
    customer.set_middle_initial("R")
    return customer


@pytest.fixture
def expected_find_all_result():
    customer = Customer()
    customer.set_identifier("9186630c-a671-4d20-b38d-c627d21da302")
    customer.set_first_name("John")
    customer.set_last_name("Doe")
    customer.set_middle_initial("S")

    results = set()
    results.add(customer)
    return results


def test_find_all(mocker, expected_find_all_result):

    mock_query = mocker.patch.object(sqlalchemy.orm.Query, 'all', name="mock_result_proxy")
    mock_query.all.return_value = expected_find_all_result

    mock_session = mocker.patch.object(sqlalchemy.orm.Session, 'query', name="mock_session")
    mock_session.query.return_value = mock_query

    base_dao = BaseDao(Customer, mock_session)
    _results = base_dao.find_all()

    mock_session.query.assert_called_once()
    mock_query.all.assert_called_once()

    assert _results is not None
    assert len(_results) == 1


@pytest.fixture
def expected_find_by_id_result():
    customer = Customer()
    customer.set_identifier("7d0e2324-7057-435f-8510-f05a6bb2d7f5")
    customer.set_first_name("Jane")
    customer.set_last_name("Smith")
    customer.set_middle_initial("K")
    return customer


def test_find_by_id(mocker, expected_find_by_id_result):
    mock_query = mocker.patch.object(sqlalchemy.orm.Query, 'get', name="mock_result_proxy")
    mock_query.get.return_value = expected_find_by_id_result

    mock_session = mocker.patch.object(sqlalchemy.orm.Session, 'query', name="mock_session")
    mock_session.query.return_value = mock_query

    base_dao = BaseDao(Customer, mock_session)
    _actual_result = base_dao.find_by_id("7d0e2324-7057-435f-8510-f05a6bb2d7f5")

    mock_query.get.assert_called_once()
    mock_session.query.assert_called_once()

    assert _actual_result is not None
    assert _actual_result.get_identifier() == expected_find_by_id_result.get_identifier()


@pytest.fixture
def expected_save_result():
    customer = Customer()
    customer.set_identifier("ecf7d5ab-b609-4926-b584-491228739440")
    customer.set_first_name("Kevin")
    customer.set_last_name("Anderson")
    customer.set_middle_initial("A")
    return customer


def test_save(mocker, expected_save_result):
    mock_session = mocker.patch.object(sqlalchemy.orm.Session, 'add', name="mock_session")
    mock_session.add.return_value = expected_save_result

    base_dao = BaseDao(Customer, mock_session)
    _actual_result = base_dao.save(expected_save_result)

    mock_session.add.assert_called_once()

    assert _actual_result is not None
    assert _actual_result.get_identifier() == expected_save_result.get_identifier()


def test_save_exception(mocker, general_test_customer):
    mock_session = mocker.patch.object(sqlalchemy.orm.Session, 'add', name="mock_session")
    mock_session.add.side_effect = RuntimeError("Error saving customer")

    base_dao = BaseDao(Customer, mock_session)

    try:
        base_dao.save(general_test_customer)
    except RuntimeError as e:
        assert str(e) == "Error saving customer"


@pytest.fixture
def expected_update_result():
    customer = Customer()
    customer.set_identifier("ba6a4e88-534f-416d-bf6e-985bd6d03b84")
    customer.set_first_name("Ann")
    customer.set_last_name("Jones")
    customer.set_middle_initial("B")
    return customer


def test_update(mocker, expected_update_result):
    mock_session = mocker.Mock(sqlalchemy.orm.Session)

    base_dao = BaseDao(Customer, mock_session)
    actual_result = base_dao.update(expected_update_result)

    mock_session.merge.assert_called_once()
    mock_session.add.assert_called_once()

    assert actual_result is not None
    assert actual_result.get_identifier() == expected_update_result.get_identifier()


def test_update_exception(mocker, general_test_customer):
    mock_session = mocker.patch.object(sqlalchemy.orm.Session, 'add', name="mock_session")
    mock_session.add.side_effect = RuntimeError("Error updating customer")

    base_dao = BaseDao(Customer, mock_session)

    try:
        base_dao.update(general_test_customer)
    except RuntimeError as e:
        assert str(e) == "Error updating customer"


def test_delete(mocker):
    mock_session = mocker.Mock(sqlalchemy.orm.Session)

    base_dao = BaseDao(Customer, mock_session)
    actual_result = base_dao.delete("ce05ae37-75ae-4b2c-b4e2-4384e5be0c73")

    mock_session.delete.assert_called_once()
    assert actual_result is True


def test_delete_exception(mocker, general_test_customer):
    mock_session = mocker.patch.object(sqlalchemy.orm.Session, 'delete', name="mock_session")
    mock_session.delete.side_effect = RuntimeError("Error deleting customer")

    base_dao = BaseDao(Customer, mock_session)

    try:
        base_dao.delete(general_test_customer.get_identifier())
    except RuntimeError as e:
        assert str(e) == "Error deleting customer"
