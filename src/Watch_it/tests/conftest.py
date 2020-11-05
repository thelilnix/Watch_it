import pytest
from Watch_it import app as flask_app

# Change directory to `src/` then run `python -m pytest`


@pytest.fixture
def app():
    yield flask_app


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def wrong_user_pass():
    return {"username": "pytest", "password": "testpassword"}
