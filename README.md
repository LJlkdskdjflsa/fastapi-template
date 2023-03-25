# external-cms-auth

- [Notion Page](https://www.notion.so/xrexuiux/External-CMS-Auth-9445d5af95f84e628f231a43d173b040)

## Contents

- Folder Structure
- Set up Environment
- Set up poetry
- Set up DB
- Run Project
- Run the tests

## Folder Structure

### - In `/app`

```markdown
.
├── core # folder about core library
│ ├── config # get config from `.env`
├── middleware # folder about middleware
├── dependency # folder about fastapi dependency
├── api # folder about api route (Controller)
├── service # folder about service (Business Logic)
├── repository # ORM model (Data Access Layer)
├── entity # database schema entity object (Data Object)
├── dto # DTO object
├── metaclass
├── enum_utils # folder about enum utils
└── utils # utility functions
```

## Set up Environment

copy the `.env.example` and rename it to `.env` than write the parameters you use when local developing

## Set up poetry

* please download [poetry](https://python-poetry.org/en/latest/) first and install it

 ```shell
brew install poetry
```

* create virtual environment (using project python version (find in `pyproject.toml``))

```shell
poetry env use python<python version>
# example: poetry env use 3.11.1
```

* activate virtual environment

```shell
poetry shell
```

* install package

```shell
poetry install
```

## Set up DB

### MySQL

Can use local DB or use DB on fasterdev

#### Local DB

create database

##### Set up database schema using alembic

### upgrade DB schema to newest version

### make migrations (when change entity)

```shell
alembic revision --autogenerate -m "migraion_message"
```

```shell
alembic upgrade head
```

## Run Project

```shell
uvicorn main:app --host 0.0.0.0 --port 5001
```

## VI. Run the tests

* run test using `poetry` and `pytest`
    * using -n=20: run 20 tests in parallel thread
    * using --reruns 5: rerun 5 times if test failed

```shell
poetry run pytest -n=20 --reruns 5

// run with coverage
pytest --cov=app -v --cov-report=html
```

