from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/password")
def password():
    # Get the value from the input field of the homepage
    password_length = int(request.args["password_length"])
    
    # Generate the password using the input length
    final_result = password_generator(password_length)
    return render_template("password.html", final_result=final_result)


def password_generator(password_length):
    pool = string.ascii_letters + string.digits + string.punctuation
    selection = "".join(random.choice(pool) for i in range(password_length))
    return selection