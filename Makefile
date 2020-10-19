install:
	poetry install
build:
	poetry build
package-install:
	pip3 install --user dist/*.whl
lint:
	poetry run flake8 brain_games
