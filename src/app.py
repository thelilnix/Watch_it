from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import requests
import json
from db_config import (
    MYSQL_HOST,
    MYSQL_USER,
    MYSQL_PASSWORD,
    DB_NAME
)

app = Flask(__name__)
uri = f'mysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}/{DB_NAME}'
app.config["SQLALCHEMY_DATABASE_URI"] = uri
db = SQLAlchemy(app)


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


if __name__ == "__main__":
    app.run("0.0.0.0", 5000, debug=False)
