from flask import Flask, render_template,abort
app = Flask(__name__)	


@app.route('/',methods=["GET","POST"])
def inicio():
	return render_template("inicio.html")

@app.route('/hola/')
@app.route('/hola/<nombre>')
def saluda(nombre=None):
    return render_template("template1.html", nombre=nombre)


@app.route('/suma/<num1>/<num2>')
def suma(num1, num2):
    try:
        resultado = int(num1) + int(num2)
    except:
        abort(404)
    return render_template("template2.html", num1=num1, num2=num2,
resultado=resultado)	
app.run(debug=True)