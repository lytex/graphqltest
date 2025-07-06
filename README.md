# graphqltest

## Installation

```bash
uv venv --python 3.12
source .venv/bin/activate
uv sync
python manage.py createsuperuser # enter user password to login in the web
```

## Running the development server

```bash
cd project
python manage.py runserver
```

Go to [http://127.0,0,1:8000](http://127.0,0,1:8000) to enter the interactive _GraphQL_ server
[http://127.0,0,1:8000/admin](http://127.0,0,1:8000/admin) is the admin interface. Here you can create the

## Running with docker

```bash
docker build . -t graphqltest
docker run --network host graphqltest
```
