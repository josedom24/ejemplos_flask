from flask import Flask, render_template
app = Flask(__name__)	


@app.route('/',methods=["GET","POST"])
@app.route('/persona/<cadena>/<int:edad>',methods=["GET","POST"])
def saluda(cadena="NADIE",edad=0):
	nombre = cadena
	return render_template("inicio.html",nombre=nombre,edad=edad)

@app.route("/articulos/<int:numero>")
def mostrar_ariculo(numero):
    return render_template("articulos.html",id=numero)

app.run(debug=True)