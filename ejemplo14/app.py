from flask import Flask, render_template,request
app = Flask(__name__)	


@app.route('/',methods=["GET","POST"])
def inicio():
	return render_template("formulario.html")

@app.route("/procesar", methods=["post"])
def procesar_formulario():
	passwd = request.form.get("pass_control")
	if passwd == "asdasd":
		datos = request.form
		print(datos)
		return render_template("datos.html", datos=datos)
	else:
		return render_template("error.html", error="Contraseña incorrecta")

app.run(debug=True)
