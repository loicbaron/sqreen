#!/usr/bin/env python3
import os
from dotenv import load_dotenv

from project.app import create_app

"""
WARNING: This is a development server. Do not use it in a production deployment.
Use a production WSGI server instead.
"""

if __name__ == '__main__':
    # Environment variables are defined in .env
    # load dotenv from the base root
    APP_ROOT = os.path.join(os.path.dirname(__file__), '.')   # refers to application_top
    dotenv_path = os.path.join(APP_ROOT, '.env')
    load_dotenv(dotenv_path)
    # WARNING: This is a development server. Do not use it in a production deployment.
    # Use a production WSGI server instead.
    create_app().run(host='0.0.0.0', port=8000, debug=True)