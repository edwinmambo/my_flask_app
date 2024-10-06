from flask import Flask
from .app_factory import create_app

app = create_app()
app.secret_key = 'super_secret_key' # Replace with an environment variable

from . import routes