import os
from src.app import appInit

env_name = os.getenv('FLASK_ENV')
app = appInit(env_name)


if __name__ == '__main__':
    app.run()
