from flask import Flask,render_template
app = Flask(__name__)

name = "Akshat Khatri"

mydict = [
    {
        "name": "Akshat",
        "address": "626 sec 23",
        "age": 19,
        "Superhero": False
    },
    {
        "name": "Ishita",
        "address": "101 Main St",
        "age": 25,
        "Superhero": True
    },
    {
        "name": "John",
        "address": "456 Elm St",
        "age": 30,
        "Superhero": False
    }
]

@app.route("/")
def home():
    return render_template("home.html",user_name = name, mydict = mydict)

@app.route("/About")
def about():
    return render_template("about.html",user_name = name)
@app.route("/<user>")
def welcome(user):
    return "Hello " + user

@app.route("/add/<int:number>/<int:number2>")
def number(number,number2):
    return "result of the addition of two number is " + str(number + number2)

if __name__ == '__main__':  
   app.run(debug = True)