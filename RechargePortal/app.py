from flask import Flask,render_template,request
import dbconnect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/submit',methods=['POST','GET'])
def submit():
	if(request.method=="POST"):
		return render_template("submit.html")
	else:
		return render_template("submit.html")

@app.route('/login')
def login():
		return render_template("login.html")

@app.route('/signup')
def signup():
		return render_template("signup.html")

@app.route('/success')
def success():
	return dbconnect()

if __name__ == '__main__':
    app.run()
