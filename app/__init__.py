from flask import Flask # type: ignore

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'

from app import routes
