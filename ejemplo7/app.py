from flask import Flask, render_template
app = Flask(__name__)	

@app.route('/',methods=["GET","POST"])
def inicio():
	return render_template("inicio.html")
@app.route('/<nombre>',methods=["GET","POST"])
def nombre(nombre):
	return render_template("inicio.html",nombre=nombre)

@app.route('/<nombre>/<int:edad>',methods=["GET","POST"])
def nombre_edad(nombre,edad):
	return render_template("inicio.html",nombre=nombre,edad=edad)

app.run(debug=True)