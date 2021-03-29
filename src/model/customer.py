import uuid
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy.ext.declarative import declarative_base
from .base_model import BaseModel

Base = declarative_base(cls=BaseModel)


class Customer(Base, BaseModel):

    first_name = Column(String(50), index=True, nullable=False)
    last_name = Column(String(50), index=True, nullable=False)
    middle_initial = Column(String(1))

    def get_first_name(self):
        return self.first_name

    def set_first_name(self, first_name):
        self.first_name = first_name

    def get_last_name(self):
        return self.last_name

    def set_last_name(self, last_name):
        self.last_name = last_name

    def get_middle_initial(self):
        return self.middle_initial

    def set_middle_initial(self, middle_initial):
        self.middle_initial = middle_initial

    def str(self):
        return f"Customer [first_name: {self.first_name}, last_name: {self.last_name}]"

    def to_dict(self):
        return {
            'identifier': self.identifier,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'middle_initial': self.middle_initial
        }

    @classmethod
    def from_dict(cls, customer_dict):
        customer = Customer()
        customer.identifier = customer_dict["identifier"]
        customer.first_name = customer_dict["first_name"]
        customer.last_name = customer_dict["last_name"]
        customer.middle_initial = customer_dict["middle_initial"]
        return customer

    @classmethod
    def new_from_dict(cls, customer_dict):
        customer_dict["identifier"] = str(uuid.uuid4())
        customer = cls.from_dict(customer_dict)

        return customer


