#!/usr/bin/python3
"""
start Flask web app
"""
from flask import Flask, render_template
from models import storage, State


app = Flask(__name__)


@app.route('/states_lists', strict_slashes=False)
def state_list():
    """ display HTML page """
    return render_template('7-states_list.html', state_stor=storage.all(State))


@app.teardown_appcontext
def close_session(exceptions):
    """ remove SQLAlchemy session """
    storage.close()

if __name__ == "__main__":
    app.run('0.0.0.0', port=5000)
