from flask import Flask
from flask import render_template, request, redirect, session, g, Response, flash

from apis.classification import classify_api

app = Flask(__name__)
app.register_blueprint(classify_api)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)