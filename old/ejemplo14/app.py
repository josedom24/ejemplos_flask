from flask import Flask, render_template,request
app = Flask(__name__)	


@app.route('/',methods=["GET"])
def inicio():
	return render_template("formulario.html")

@app.route("/procesar", methods=["post"])
def procesar_formulario():
	passwd = request.form.get("pass_control")
	if passwd == "asdasd":
		return render_template("datos.html", datos=request.form)
	else:
		return render_template("error.html", error="Contraseña incorrecta")

app.run(debug=True)
