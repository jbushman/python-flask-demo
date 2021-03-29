from dependency_injector import providers, containers
from db.session_manager import SessionManager
from db.dao.customer_dao import CustomerDao


class DaoContainer(containers.DeclarativeContainer):

    _session_manager = SessionManager()
    customer_dao = providers.Factory(CustomerDao, connection=_session_manager.get_session())
