from flask import Flask, render_template, request
app = Flask(__name__)	

@app.route('/')
def inicio():
    return render_template("inicio.html")

@app.route('/articulos')
def articulos():
    nombre=request.args.get("nombre")
    precio=request.args.get("precio")
    return render_template("articulos.html",nombre=nombre,precio=precio)

@app.route('/acercade')
def acercade():
    return render_template("acercade.html")

@app.route('/acercade/<nombre>')
def acercade_con_nombre(nombre,edad=0):
    return render_template("acercade.html",nombre=nombre)


app.run("0.0.0.0",5000,debug=True)