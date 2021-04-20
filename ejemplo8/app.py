from flask import Flask, render_template,abort
app = Flask(__name__)	

@app.route('/inicio',methods=["GET","POST"])
def inicio():
	return render_template("inicio.html")

@app.route('/tablas/<numero>')
def tabla(numero):
	try:
		numero=int(numero)
	except:
		abort(404)
	return render_template("inicio.html",num=numero)

app.run(debug=True)