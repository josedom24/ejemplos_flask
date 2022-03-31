from flask import Flask, render_template, abort, request
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

@app.route('/acercade/<nombre>/<edad>')
def acercade_con_nombre(nombre,edad):
    return render_template("acercade.html",nombre=nombre,edad=edad)

@app.route('/suma',methods=["POST"])
def suma():
    num1=request.form.get("numero1")
    num2=request.form.get("numero2")
    try:
        resultado = int(num1) + int(num2)
    except:
        return abort(404)
    return render_template("suma.html", num1=num1, num2=num2,
resultado=resultado)	

app.run("0.0.0.0",5000,debug=True)