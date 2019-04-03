from flask import Flask, render_template,abort
app = Flask(__name__)	


@app.route('/',methods=["GET","POST"])
def inicio():
	return render_template("inicio.html")

	
app.run(debug=True)