"""Helper class to manage a single instance of the application configuration.

This module is implemented as a Singleton to ensure that only one instance of
the ConfigHelper is created and managed.

"""
import os
import configparser


class ConfigHelper(object):

    _instance = None
    _config = None

    def __new__(cls):
        """Instantiates a new instance of the ConfigHelper class.

        If the instance has already been instantiated, the reference
        to that instance is returned.

        :arg
            cls testing the args documentation

        Returns:
            The single instance to the ConfigHelper class.

        :raises
            RuntimeException testing the raises documentation
        """
        if cls._instance is None:
            cls._instance = super(ConfigHelper, cls).__new__(cls)
            cls._instance._load_config()

        return cls._instance

    def _load_config(self):
        self._config = configparser.ConfigParser()
        path = os.path.dirname(os.path.realpath(__file__))
        results = self._config.read(f"{path}/../config//app.ini")
        assert len(results) == 1, f"the length of the list of read files should be 1: {results}"

    def get(self, category, name):
        return self._config[category][name]
