import os
import requests
import json
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from db_config import (
    MYSQL_HOST,
    MYSQL_USER,
    MYSQL_PASSWORD,
    DB_NAME,
    PANEL_USERNAME,
    PANEL_PASSWORD,
)
from flask import (
    Flask,
    render_template,
    request,
    session,
    abort,
    redirect,
    url_for,
)


app = Flask(__name__)
app.secret_key = os.urandom(24)
app.permanent_session_lifetime = timedelta(days=5)

uri = f'mysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}/{DB_NAME}'
app.config["SQLALCHEMY_DATABASE_URI"] = uri
db = SQLAlchemy(app)

limiter = Limiter(
    app,
    key_func=get_remote_address,
)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    platform = db.Column(db.String(15))
    browser = db.Column(db.String(15))
    ip = db.Column(db.String(15))
    country = db.Column(db.String(40))

    def __init__(self, platform, browser, ip, country):
        self.platform = platform
        self.browser = browser
        self.ip = ip
        self.country = country

    def __repr__(self):
        return '<User %s>' % self.ip


db.create_all()


@app.before_first_request
def before_first_req():
    session.permanent = True


@app.route("/")
def home():

    user_platform = request.user_agent.platform
    user_browser = request.user_agent.browser
    user_ip = request.remote_addr
    user_country = ""

    try:
        info = json.loads(
            requests.get(f"http://ip-api.com/json/{user_ip}").text
        )

        user_country = info['country']
    except Exception:
        user_country = "Unknown"

    try:
        new_user = User(user_platform, user_browser, user_ip, user_country)

        db.session.add(new_user)
        db.session.commit()
    except Exception as err:
        print(
            f"""
            Inserting failed...
            ({user_platform}, {user_browser}, {user_ip}, {user_country}).
            Error =>\n{err}
            """
        )

    return render_template(
        "Home_template/index.html",
        platform=user_platform,
        browser=user_browser,
        ip=user_ip,
        country=user_country
    )


# This route is not secure. Change it.
@app.route('/admin', methods=["GET", "POST"])
@limiter.limit("6 per minute")
def admin_login():
    if session.get("username", '') == PANEL_USERNAME:
        # The client logged in before
        return redirect(url_for('dashboard'))
    else:
        if request.method == 'GET':
            # Show login template
            return render_template("Login_template/index.html")
        else:
            # The client entered the username and password
            username = request.form['username']
            password = request.form['password']

            # TODO: Hash PANEL_PASSWORD (and PANEL_USERNAME) (sha256).
            if username == PANEL_USERNAME and password == PANEL_PASSWORD:
                # Username and password is correct.
                session["username"] = username
                return redirect(url_for("dashboard"))
            else:
                # Unauthorized
                return abort(403)


@app.route('/dashboard')
def dashboard():
    return "DASHBOARD"


@app.errorhandler(404)
def error_404(err):
    return render_template("Error_template/404.html"), 404


@app.errorhandler(403)
def error_403(err):
    return render_template("Error_template/403.html"), 403


if __name__ == "__main__":
    app.run("0.0.0.0", 5000, debug=False)
