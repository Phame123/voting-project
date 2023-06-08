from flask import Flask, session
from api import app

run_app = Flask(__name__ + "kofi")
run_app.secret_key = "9*3*2"
run_app.register_blueprint(app, url_prefix="/Kintampo")

if __name__ == '__main__':
    run_app.secret_key = "9*3*2"
    run_app.run(host='0.0.0.0', port='2000', debug=True)
