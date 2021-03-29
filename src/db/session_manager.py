from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from helper.config_helper import ConfigHelper


class SessionManager(object):

    instance = None
    engine = None
    session_factory = None
    session = None

    config_helper = None

    def __new__(cls):
        if cls.instance is None:
            cls.instance = super(SessionManager, cls).__new__(cls)

        return cls.instance

    def __init__(self):

        config_helper = ConfigHelper()
        dialect = config_helper.get("database", "dialect")
        host = config_helper.get("database", "host")
        port = config_helper.get("database", "port")
        name = config_helper.get("database", "name")
        username = config_helper.get("database", "username")
        password = config_helper.get("database", "password")

        # TODO: I couldn't get MySQL to work without added pymysql to the connection string
        # SQLAlchemy uses mysqldb by default but I couldn't find that module in PyPi
        self._engine = create_engine(f"{dialect}+pymysql://{username}:{password}@{host}:{port}/{name}")
        self.session_factory = sessionmaker(bind=self._engine)
        self.session = scoped_session(self.session_factory)

    def get_session(self):
        return self.session()

