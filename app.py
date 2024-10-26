from flask import Flask, render_template, request
import random
import string
import requests

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



@app.route("/joke")
def joke():
    user_category = int(request.args["user_category"])
    url = get_url(user_category)
    final_joke = get_joke(url)
    return render_template("joke.html", final_joke=final_joke)


def get_url(number):
    categories = {1: "Programming", 2: "Miscellaneous", 3: "Dark", 4: "Pun", 5: "Any"}
    category = categories[number]
    return f"https://v2.jokeapi.dev/joke/{category}?type=single"


def get_joke(api_url):
    response = requests.get(api_url)
    data = response.json()
    return data["joke"]
