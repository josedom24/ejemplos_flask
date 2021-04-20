from flask import Flask, render_template
app = Flask(__name__)	

@app.route('/',methods=["GET","POST"])
def inicio():
	persona = "juan"
	num1=10
	num2=14
	return render_template("inicio.html",nombre=persona,edad=12,numero1=num1,numero2=num2,resultado=num1+num2)

app.run(debug=True)