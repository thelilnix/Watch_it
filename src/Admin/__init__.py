from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Home"


if __name__ == "__main__":
    app.run("0.0.0.0", 5000, debug=False)
