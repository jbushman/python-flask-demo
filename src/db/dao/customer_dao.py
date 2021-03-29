from db.dao.base_dao import BaseDao
from model.customer import Customer


class CustomerDao(BaseDao):

    def __init__(self, session):
        super().__init__(Customer, session)

    def find_by_name(self, name):
        # TODO: Implement
        raise NotImplementedError()
