from flask import Flask


app = Flask(__name__)


@app.route("/home")
def home():
    return "Hello, world"



@app.route("/admin")
def admin():
    return "admin page"


if __name__ == "__main__":
    app.run(debug=True)