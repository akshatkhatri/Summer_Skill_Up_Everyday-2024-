from flask import Flask,render_template,abort
from forms import LoginForm
app = Flask(__name__)
app.config['SECRET_KEY'] = 'dfewfew123213rwdsgert34tgfd1234trgf'

pets = [
            {"id": 1, "name": "Nelly", "age": "5 weeks", "bio": "I am a tiny kitten rescued by the good people at Paws Rescue Center. I love squeaky toys and cuddles."},
            {"id": 2, "name": "Yuki", "age": "8 months", "bio": "I am a handsome gentle-cat. I like to dress up in bow ties."},
            {"id": 3, "name": "Basker", "age": "1 year", "bio": "I love barking. But, I love my friends more."},
            {"id": 4, "name": "Mr. Furrkins", "age": "5 years", "bio": "Probably napping."},
            {"id": 5, "name": "Ally", "age": "8 years", "bio": "Probably napping."}
        ]

@app.route("/")
def home():
    return render_template("home.html",pets = pets)

@app.route("/signup",methods = ["POST","GET"])
def signup():
    form = LoginForm()
    if form.validate_on_submit():
        print("Submitted and Valid")
        print(form.data)
    else:
        print(form.errors)
    return render_template("signup.html",form = form)
    
    
@app.route("/details/<int:id>")
def details(id):
    for pet in pets :
        if pet["id"] == id:
            return render_template("details.html",pet = pet)
    abort(404, description="NO PET  FOUND WITH THIS ID")   
    
@app.route("/about")
def About():
    return "WE are still crafting a nice About Page, BUT THANKS FOR VISITING"


if __name__ == '__main__':  
   app.run(debug = True)
