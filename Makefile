test:
	PYTHONPATH=src pipenv run pytest --cov-config=.coveragerc --cov-report=html --cov-report=term --cov=src tests/
