import os
from flask import Flask

from . import db
from .auth import bp as auth_bp
from .home import bp as home_bp

def create_app(test_config=None):
    # create and configure the app
    app=Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(SECRET_KEY='dev', DATABASE=os.path.join(app.instance_path,'flaskr.sqlite') )
    # flaskr.sqlite file will be located in the instance path.
    # instance path/folder will be in the same working dir as this file's dir.
    if test_config is None:
        # load the instance config , if it exists , when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)
    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    db.init_app(app)

    # from . import auth, home
    app.register_blueprint(auth_bp)
    app.register_blueprint(home_bp)

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'hello world'

    return app


    """
    @app.route('/')
    def index():
        repo = Repo(os.path.dirname(os.path.realpath(__file__)))
        tags = sorted(repo.tags, key=lambda t: t.commit.committed_datetime)
        gittag = str(tags[-1])
        return render_template()
    """

    """
    from . import db

    return app
    """
