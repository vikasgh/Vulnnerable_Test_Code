from flask import Flask, request
from auth import login_user
from db import get_user_by_name
from utils import render_page

app = Flask(__name__)

@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    return login_user(username, password)

@app.route("/user")
def user_info():
    name = request.args.get("name")
    user = get_user_by_name(name)
    return f"User info: {user}"

@app.route("/search")
def search():
    query = request.args.get("q")
    return render_page(f"<h1>You searched for: {query}</h1>")

if __name__ == "__main__":
    app.run(debug=True)