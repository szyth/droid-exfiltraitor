from flask import Flask,request
from .config import app_config
import os
from werkzeug.utils import secure_filename




def appInit(env_name):

    app = Flask(__name__)

    @app.route("/", methods=['POST'])
    def index():

        # empty file
        if 'file' not in request.files:
            return "failed"

        file = request.files['file']

        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            return "failed"
        if file:
            filename = secure_filename(file.filename)

            # save all data inside /tmp
            file.save(os.path.join('./', filename))

        return "done"
    return app
