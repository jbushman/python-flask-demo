import logging
from model.customer import Customer
from config.server_config import ServerConfig


class CustomerService(object):

    _logger = logging.getLogger('app')
    _server_config = ServerConfig()
    _customer_dao = None

    def __init__(self, customer_dao):
        self._customer_dao = customer_dao

    def find_all(self):
        self._logger.info("Retrieving all customers")

        _customers = self._customer_dao.find_all()

        return _customers

    def find_by_id(self, identifier):
        self._logger.info("Retrieving customer by id")
        _customer = self._customer_dao.find_by_id(identifier)

        return _customer

    def save(self, customer):
        _new_customer = Customer.new_from_dict(customer)
        _saved_customer = self._customer_dao.save(_new_customer)

        return _saved_customer

    def update(self, customer):
        _modified_customer = Customer.from_dict(customer)
        _updated_customer = self._customer_dao.update(_modified_customer)
        return _updated_customer

    def delete(self, identifier):
        self._customer_dao.delete(identifier)


