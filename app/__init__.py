from flask import Flask
from config import config_options
from flask_bootstrap import Bootstrap

from flask_sqlalchemy import SQLAlchemy
# from flask_login import LoginManager
#
# login_manager = LoginManager()
# login_manager.session_protection = 'strong'
# login_manager.login_view = 'auth.login
bootstrap = Bootstrap()
db = SQLAlchemy()

def create_app(config_name):

@@ -13,6 +19,10 @@ def create_app(config_name):

    bootstrap.init_app(app)

    db.init_app(app)

    # login_manager.init_app(app)

    from .main import main as main_blueprint

    app.register_blueprint(main_blueprint)
    # from .request import configure_request
    # configure_request(app)
    return app