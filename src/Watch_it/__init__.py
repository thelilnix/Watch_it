"""
Watch_it
Watch your users while they're watching a clock.
"""
import os
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy
from flask import (
    Flask,
    session,
)
from Watch_it.db_config import (
    MYSQL_HOST,
    MYSQL_USER,
    MYSQL_PASSWORD,
    DB_NAME,
)


def import_views():
    import Watch_it.views
    print(f"{Watch_it.views.__name__} detected")


app = Flask(__name__)
app.secret_key = os.urandom(24)
app.permanent_session_lifetime = timedelta(days=5)

uri = f'mysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}/{DB_NAME}'
app.config["SQLALCHEMY_DATABASE_URI"] = uri
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


# Importing views.py
import_views()


@app.before_first_request
def before_first_req():
    """
    Begore first request function.
    """
    session.permanent = True


if __name__ == "__main__":
    app.run("0.0.0.0", 5000, debug=False)
