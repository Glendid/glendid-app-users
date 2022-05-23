# install project requirements
install:
		@pip install -r requirements.txt
		@pip install -r test-requirements.txt

#Create code lint report
lint: venv
	pylint ./src

#Run unit test
test: venv
	coverage run -m pytest

#Run test coverage
coverage: venv
	coverage report
	coverage html