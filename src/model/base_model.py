from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import DateTime
from datetime import datetime


class BaseModel(object):

    @declared_attr
    def __tablename__(self):
        name = self.__name__.lower()
        return name

    __table_args__ = {'mysql_engine': 'InnoDB'}
    # __mapper_args__ = {'always_refresh', True}

    identifier = Column('id', String(36), primary_key=True)
    created_at = Column(DateTime, default=datetime.now, nullable=False)

    def get_identifier(self):
        return self.identifier

    def set_identifier(self, identifier):
        self.identifier = identifier

    def get_created_at(self):
        return self.created_at
