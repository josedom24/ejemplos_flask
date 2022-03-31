from flask import Flask, render_template, abort, redirect, request
app = Flask(__name__)	

@app.route('/')
def inicio():
    return redirect("/entrar")

@app.route('/articulos')
def articulos():
    nombre=request.args.get("nombre")
    precio=request.args.get("precio")
    return render_template("articulos.html",nombre=nombre,precio=precio)

@app.route('/acercade')
def acercade():
    return render_template("acercade.html")

@app.route('/acercade/<nombre>/<edad>')
def acercade_con_nombre(nombre,edad):
    return render_template("acercade.html",nombre=nombre,edad=edad)

@app.route('/entrar',methods=["GET","POST"])
def entrar():
    datos=[
    {"valor":1,"texto":"Windows"},
    {"valor":2,"texto":"Linux"},
    {"valor":3,"texto":"MacOs"}
    ]
    if request.method=="GET":
        return render_template("formulario.html",datos=datos)
    else:
        usuario=request.form.get("usuario")
        passwd=request.form.get("pass")
        so=request.form.get("sistema")
        if passwd=="asdasd":
            return render_template("entrar.html")	
        else:
            return render_template("formulario.html",datos=datos,usuario=usuario,seleccionado=int(so),error=True)

app.run("0.0.0.0",5000,debug=True)