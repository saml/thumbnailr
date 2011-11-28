import flask

app = flask.Flask(__name__)

import os
import shutil
import contextlib
import sqlite3

app.config.from_object('thumbnailr.settings')
app.config.from_envvar('THUMBNAILR_CONFIG', silent=True)

IMG_DIR = app.config['IMG_DIR']
PREFIX_ORIGINAL = app.config['PREFIX_ORIGINAL']
PARAM_FILE = app.config['PARAM_FILE']
DATABASE = app.config['DATABASE']
DATABASE_SCHEMA = app.config['DATABASE_SCHEMA']


def connect_db():
    return sqlite3.connect(DATABASE)

def init_db():
    with contextlib.closing(connect_db()) as db:
        with app.open_resource(DATABASE_SCHEMA) as f:
            db.cursor().executescript(f.read())
        db.commit()


import thumbnailr.views
