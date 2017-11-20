from flask import Flask
from conf import config
#Import Module
#from modules.signin import *
import subprocess
def create_app(environment):
    app = Flask(__name__)
    app.config.from_object(config[environment])
    # Register Module
    #app.register_blueprint(signin)
    # Prevent from create *.pyc
    subprocess.call("find . | grep -E "+'"'+"(__pycache__|\.pyc|\.pyo$)"+'"' +"| xargs rm -rf", shell=True)
    return app

app = create_app('DEVELOPMENT')
app.run(host='0.0.0.0')
