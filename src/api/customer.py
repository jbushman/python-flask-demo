import logging
from config.server_config import ServerConfig
from db.dao.customer_dao import CustomerDao
from db.session_manager import SessionManager
from service.customer import CustomerService
from helper.customer_helper import convert_customer_list

# TODO: Keeping this here until dependency injection is solved.
# from container.service_container import ServiceContainer

_logger = logging.getLogger('app')

server_config = ServerConfig()
limiter = server_config.get_rate_limiter()

# TODO: Keeping this here until dependency injection is solved.
# _service_container = ServiceContainer()
# _customer_service = _service_container.customer_service

_session_manager = SessionManager()
_customer_dao = CustomerDao(_session_manager.get_session())
_customer_service = CustomerService(_customer_dao)


@limiter.limit("1/second")
def find_all():
    _logger.info("Retrieving all customers")
    _customers = _customer_service.find_all()

    _response = {
        "success": True,
        "data": {
            "customers": convert_customer_list(_customers)
        }
    }

    return _response


@limiter.limit("/second")
def find_by_id(identifier):
    _logger.info("Finding customer by id")
    _customer = _customer_service.find_by_id(identifier)

    _response = {
        "success": True,
        "data": {
            "customer": _customer.to_dict()
        }
    }

    return _response


@limiter.limit("1/second")
def save(customer):
    _logger.info("Creating new customer")
    _customer = _customer_service.save(customer)

    response = {
        "success": True,
        "data": {
            "customer": _customer.to_dict()
        }
    }

    return response


@limiter.limit("1/second")
def update(customer):
    _logger.info("Updating a customer")
    _customer = _customer_service.update(customer)

    response = {
        "success": True,
        "data": {
            "customer": _customer.to_dict()
        }
    }

    return response


@limiter.limit("1/second")
def delete(identifier):
    _logger.info("Deleting customer")
    _customer_service.delete(identifier)

    response = {
        "success": True
    }

    return response
