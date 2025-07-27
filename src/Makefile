run:
	python manage.py runserver 0.0.0.0:8000

migrations:
	python manage.py makemigrations
	make precommit

migrate:
	python manage.py migrate

superuser:
	python manage.py createsuperuser

loaddata:
	python manage.py loaddata fixtures/users.json
	python manage.py loaddata fixtures/polls.json

dumpdata:
	python manage.py dumpdata users.customuser --indent 2 > fixtures/users.json
	python manage.py dumpdata polls --indent 2 > fixtures/polls.json

precommit:
	isort . --skip ./sso --settings-path pyproject.toml
	black . --config pyproject.toml
	flake8 . --config pyproject.toml
	djlint . --reformat

bandit:
	bandit -r .

rate:
	pylint *

deadcode:
	vulture . --min-confidence 100

update:
	pip install --upgrade pip
	pur -r ../requirements/base.txt
	pip install -r ../requirements/base.txt -r ../requirements/dev.txt

docs:
	mkdir -p ../docs/images
	python manage.py graph_models --pygraphviz  auth --exclude-models BaseModel,AbstractBaseUser,PermissionsMixin,AbstractUser,Permission,Group -g -o ../docs/images/auth.png
	python manage.py graph_models --pygraphviz polls -g -o ../docs/images/polls.png
