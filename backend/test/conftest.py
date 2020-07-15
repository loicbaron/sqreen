import os
import pytest
from dotenv import load_dotenv

from project.app import create_app

@pytest.fixture
def app():
    # load dotenv in the base root
    APP_ROOT = os.path.join(os.path.dirname(__file__), '..')   # refers to application_top
    dotenv_path = os.path.join(APP_ROOT, '.env')
    load_dotenv(dotenv_path)
    # override for test
    os.environ['SQREEN_NOTIFICATIONS_KEY'] = '1234'
    app = create_app()
    return app
