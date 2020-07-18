#!/usr/bin/env python3

# Sqreen library monitors the security of this application
# It is an In-App Web Application Firewall
# more info: https://sqreen.com/
import sqreen
sqreen.start()

import datetime
import os
from flask import Flask, jsonify, render_template, request, send_from_directory
from flask_sqlalchemy import SQLAlchemy

from project.config.database import db_session, init_db
from project.controllers.events import events_controller
from project.controllers.notifications import notifications_controller

def create_app():
    app = Flask(__name__, static_url_path='', instance_relative_config=True)
    app.config['SQREEN_NOTIFICATIONS_KEY'] = os.environ.get("SQREEN_NOTIFICATIONS_KEY")
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    with app.app_context():
        init_db()

    @app.teardown_appcontext
    def shutdown_session(exception=None):
        db_session.remove()

    @app.route('/')
    def home():
        return render_template('index.html')
    
    app.register_blueprint(notifications_controller)
    app.register_blueprint(events_controller)
    
    return app

