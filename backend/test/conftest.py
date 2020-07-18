import os
import pytest
from dotenv import load_dotenv
from pathlib import Path


def pytest_configure(config):
    # load dotenv in the base root
    APP_ROOT = os.path.join(os.path.dirname(__file__), '..')   # refers to application_top
    env_path = Path(APP_ROOT) / '.test.env'
    load_dotenv(dotenv_path=env_path, override=True)
    return config

@pytest.fixture
def app(mocker):
    from project.app import create_app
    app = create_app()
    with app.app_context():
        yield app   # Note that we changed return for yield, see below for why

