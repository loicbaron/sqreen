#!/usr/bin/env python3
import os
from dotenv import load_dotenv

from project.app import create_app

APP_ROOT = os.path.join(os.path.dirname(__file__), '..')   # refers to application_top
dotenv_path = os.path.join(APP_ROOT, '.env')
load_dotenv(dotenv_path)

app = create_app()