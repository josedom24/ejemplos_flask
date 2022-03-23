from flask import Flask, render_template, abort, redirect
app = Flask(__name__)	

@app.route('/')
def inicio():
    return render_template("inicio.html")

@app.route('/articulos')
def articulos():
    return render_template("articulos.html")

@app.route('/acercade')
def acercade():
    return render_template("acercade.html")

@app.route('/error')
def error():
    return abort(404)

@app.route('/redireccion')
def redireccion():
    return redirect("/articulos")


app.run("0.0.0.0",5000,debug=True)