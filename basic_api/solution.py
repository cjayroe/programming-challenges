from flask import Flask
from .simple_views import mod

def create_app(config):
    app = Flask(__name__)

    app.register_blueprint(mod)
    return app

app = create_app('config')



if __name__ == '__main__':
    app.run()