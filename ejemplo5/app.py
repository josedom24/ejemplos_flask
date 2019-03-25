from flask import Flask, render_template,abort
app = Flask(__name__)	

@app.route('/',methods=["GET","POST"])
def inicio():
	lista = ["manzana","platano","piña","kiwi"]
	return render_template("inicio.html", lista=lista)
app.run(debug=True)