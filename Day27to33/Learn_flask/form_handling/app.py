from flask import Flask,render_template,abort,request
from flask_wtf import FlaskForm
from my_forms import Loginform
app = Flask(__name__)
app.config['SECRET_KEY'] = 'dfewfew123213rwdsgert34tgfd1234trgf'
sample_users = {
    "user1@example.com": "password123",
    "user2@example.com": "securePass456",
    "user3@example.com": "myPassword789",
    "user4@example.com": "passWord321",
    "user5@example.com": "password@987",
    "user6@example.com": "123password",
    "user7@example.com": "pass_456word",
    "user8@example.com": "myp@ssw0rd!",
    "user9@example.com": "P@ssword123",
    "user10@example.com": "passWORD!321"
}
@app.route("/",methods = ["GET","POST"])
def home():
    form = Loginform()
    
    # if form.is_submitted():
    #     print("Submitted.")
    # if form.validate():
    #     print("Valid.")
    if form.validate_on_submit():
       print("Submitted and Valid.")
       print(form.email.data)
       print(form.password.data)
    else:
        print(form.errors.items())
        print(form.email.errors)
        print(form.password.errors)
    return render_template("home.html",form = form)

@app.route("/login",methods = ["GET","POST"])
def login():
    
    
    if request.method == 'POST':
        email = request.form["email"]
        password = request.form["password"]
        
        if email in sample_users and sample_users[email] == password:
            return render_template("login.html",message = "Login Succesful")
        else:
            return render_template("login.html",message = "Login UnSuccesful")
        
    else:
        abort(404,"Error encountered")

if __name__ == '__main__':  
   app.run(debug = True)