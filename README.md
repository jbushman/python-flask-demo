# Python Flask Microservice Demo

### Table of Contents
* [Description](#description)
* [Python Packages](#python-packages)
* [Configuration](#configuration)
* [Setup](#setup)
* [Testing](#testing)
* [Usage](#usage)
* [Useful Commands](#useful-commands)
* [Helpful Links](#helpful-links)
* [Contributing](#contributing)

## Description
The Python Flask Microservice recipe has been created to help teams in a variety of ways.

1. To bootstrap a new project.
2. As a reference to one of many ways to build an n-tier application architecture.
3. An example for engineers to start learning how to build a web application using Python and Flask as a microservices
4. A roadmap outlining the components needed for building a well build microservice.
5. Any other way one sees fit.

The implementation of this microservice and its inner patterns and components are perpetually open to constructive criticism for the purpose of improvement. The goal of this recipe is to give the best representation of a well-architected microservice, and to achieve that, such criticism is required. The authors of this recipe welcome constructive criticism for improvements around the areas of performance, scalability, readability, maintainability and other areas of `ility`. Criticism around styling and other subjective topics that do not follow the company Python guidelines will not be taken seriously and are subject to internal mocking and judgment, so be nice. 😀


## Python Packages

#### Required Python Version
3.8

#### dev-packages
* [yoyo-migrations]() (version 7.1.2)
	* [Documentation](https://ollycope.com/software/yoyo/latest/)
* [pytest](https://pypi.org/project/pytest/) (version 6.0.0)
	* [Documentation](https://docs.pytest.org/en/latest/)
* [pytest-mock](https://pypi.org/project/pytest-mock/) (version 3.2.0)
	* [Documentation](https://github.com/pytest-dev/pytest-mock/)
* [pytest-flask](https://pypi.org/project/pytest-flask/) (version 1.0.0)
	* [Documentation](https://github.com/pytest-dev/pytest-flask)
* [pytest-cov](https://pypi.org/project/pytest-cov/) (version 2.10.0)
	* [Documentation](https://github.com/pytest-dev/pytest-cov)

#### packages
* [flask](https://pypi.org/project/Flask/) (version 1.1.2)
	* [Documentation](https://flask.palletsprojects.com/en/1.1.x/)
* [connexion](https://pypi.org/project/connexion/) (version 2.7.0)
	* [Documentation](https://github.com/zalando/connexion)
* [flask-limiter](https://pypi.org/project/Flask-Limiter/) (version 1.2.1)
	* [Documentation](https://flask-limiter.readthedocs.io/en/stable/)
* [gunicorn](https://pypi.org/project/gunicorn/) (version 20.0.4)
	* [Documentation](https://gunicorn.org/#docs)
* [python-json-logger](https://pypi.org/project/python-json-logger/) (version 0.1.11)
	* [Documentation](https://github.com/madzak/python-json-logger)
* [sqlalchemy](https://pypi.org/project/SQLAlchemy/) (version 1.3.17)
    * [Documentation](https://www.sqlalchemy.org/)
* [pymysql](https://pypi.org/project/PyMySQL/) (version 0.10.0)
	* [Documentation](https://pymysql.readthedocs.io/en/latest/)

## Setup
This project uses `pipenv` to manage the Python virtual environment and dependency management.

Running the application requires access to a MySQL database. This can be a database running locally on the developers workstation or in a shared environment. Database configuration is located in `<project_root>/src/config/app.ini`. A configuration override file that is not tracked by Git will be added in the future.

#### Steps
* Install Python 3
* Install Pipenv
	* `pip install pipenv`
* Run `pipenv install`
* Configure the database properties in the `app.ini` file (see location above)

## Testing
Currently all tests are grouped in the default category. Future enhancements will include grouping tests by unit and integration tests using pytest markers (`@pytest.mark.unit`, `@pytest.mark.integration`)

#### Running the Test Suite
A make file exists for convenience. Tests can be executed by running the command `make test`. The full command for running the tests is `PYTHONPATH=src pipenv run pytest --cov-config=.coveragerc --cov-report=html --cov-report=term --cov=src tests/`


## Usage

#### Running Locally with `pipenv`
Execute the following commands from the project root directory in a terminal
1. Debug mode:   `FLASK_DEBUG=1 pipenv run python app.py`
2. Regular mode: `pipenv run python app.py`

#### Locally with Docker Compose
* `docker-compose build && docker-compose up`

## Useful Commands:
`pipenv run alembic revision -m "create account table"`
`piping run alembic upgrade head`

### Docker

#### Builds the docker image with a tag of `python-flask-recipe`
`docker build --rm --tag python-flask-recipe .`

#### Run the docker container on port 8000. Removes the container when stopped.
`docker run --rm -p 8000:8000 --name python-flask-app python-flask-recipe_web`

#### The following commands are used to clean-up docker containers and images

#### Remove all docker containers
`docker rm $(docker ps -aq)`

#### Remove all docker images
* `docker rmi -f $(docker image ls -q)`

## Helpful Links

#### Style Guide
Follow the [Google Style Guide](https://github.com/google/styleguide/blob/gh-pages/pyguide.md)

## Contributing
Pull requests are welcome and encouraged. The source is located [here](https://stash.endurance.com/projects/DEVOPS/repos/python-flask-recipe/browse)

#### Cloning the repository
`git clone ssh://git@stash.endurance.com:7999/devops/python-flask-recipe.git`

