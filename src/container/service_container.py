from dependency_injector import providers, containers
from .dao_container import DaoContainer
from service.customer_service import Customer


class ServiceContainer(containers.DeclarativeContainer):

    customer_service = providers.Factory(Customer, dao=DaoContainer.customer_dao)
