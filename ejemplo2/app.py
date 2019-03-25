from flask import Flask, render_template
app = Flask(__name__)	

@app.route('/',methods=["GET","POST"])
def inicio():
	nombre = "jose"
	return render_template("inicio.html",nombre=nombre)

app.run(debug=True)